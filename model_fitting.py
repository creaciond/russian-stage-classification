import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

def fit_model_cv(model, model_name, X, y, params):
    """Finds best parameters for a given model prototype and fits it with the
    data passed to the function.

    :args model — (sklearn model) model prototype to fit
    :args model_name — (str) name to print in the output
    :args X — (np.array) feature vectors
    :args y — (np.array) labels
    :args params — (dict) parameters to search over while fitting the model

    :returns grid — (sklearn model) best fitted model by cross-validation results
    """
    grid = GridSearchCV(
        model,
        param_grid=params,
        scoring="f1",
        cv=5,
        n_jobs=-1,
        verbose=1
    )
    grid.fit(X, y)
    print("Model {} scored {:5f} on cross-validation with params:\n{}".format(model_name,
            grid.best_score_, grid.best_params_))
    return grid


def validate_model(model, model_name, X_valid, y_valid):
    """Performs a validation on an already trained model with a small validation
    sample to do a 'sanity check' of the model and check whether it has overfitted.

    :args model — (sklearn model) a fitted model
    :args model_name — (str) name to print in the output
    :args X_valid — (np.array) validation feature vectors
    :args y_valid — (np.array) validation labels
    """
    y_pred = model.predict(X_valid)
    score = f1_score(y_valid, y_pred)
    print("Model {} scored {:5f} on validation set".format(model_name, score))
    return score


def models_for_type(X_train, y_train, X_valid, y_valid, X_test, y_test):
    """Fits all model samples for a direction type, informs about the result, generates a 
    dict convertible into pandas DataFrame for analysis.

    :args X_train, y_train — (np.array, np.array) features and labels of the test set
    :args X_valid, y_valid — (np.array, np.array) features and labels of the test set
    :args X_test, y_test — (np.array, np.array) features and labels of the test set

    :returns total_data_dict — (dict) information on models performance
    :returns fitted_models — (dict) fitted models for latter saving
    """
    total_data_dict = {
        "model": [],
        "cross-val": [],
        "validation": [],
        "test": []
    }

    fitted_models = {}


    proto_data = {
        "LogReg": [LogisticRegression(), 
            {"C": np.linspace(0.1, 100, 100)}
        ],
        "Decision Tree": [DecisionTreeClassifier(random_state=1968), 
            {"criterion": ["gini", "entropy"], "max_depth": np.arange(1, 100)}
        ],
        "Random Forest": [RandomForestClassifier(random_state=1968),
            {"n_estimators": np.arange(1, 101)}
        ],
        "SVC": [SVC(),
        	{"C": np.linspace(0.1, 100, 100)}
        ]
    }

    for model_name in proto_data:
        total_data_dict["model"].append(model_name)

        model_prototype = proto_data[model_name][0]
        model_params = proto_data[model_name][1]

        fitted_model = fit_model_cv(model_prototype, model_name, X_train, y_train, model_params)
        fitted_models[model_name] = fitted_model
        total_data_dict["cross-val"].append(fitted_model.best_score_)

        val_score = validate_model(fitted_model, model_name, X_valid, y_valid)
        total_data_dict["validation"].append(val_score)

        y_pred = fitted_model.predict(X_test)
        test_score = f1_score(y_pred, y_test)
        total_data_dict["test"].append(test_score)
    
    return total_data_dict, fitted_models