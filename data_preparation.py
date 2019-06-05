import gensim
import numpy as np
import pandas as pd
import wget
import zipfile

def load_w2v_model(model_path):
    """Loads a word2vec model of choice.

    :args model_path — (str) path to the model

    :returns model — (gensim.models.KeyedVectors) word2vec model to use later
    """
    with zipfile.ZipFile(model_path, "r") as archive:
        stream = archive.open("model.bin")
        model = gensim.models.KeyedVectors.load_word2vec_format(stream, binary=True)
    return model


model = load_w2v_model("./data/models/180.zip")


def compute_vector(model, wv_items_list):
    """Computes a word2vec vector for a given list of tokens in the direction.
    Tokens are preprocessed lemmas combined with their part of speech in 
    Universal Text format.

    :args wv_items_list — (list of str) particular direction tokens
    :args model — (gensim.models.KeyedVectors) word2vec model for getting the vectors

    :returns res_vector — (np.array) vector for the direction with given tokens
    """
    total_counter = 0
    total_vector = np.zeros(300)
    for wv_item in wv_items_list:
        try:
            vector = np.array(model.wv[wv_item])
            total_vector += vector
            total_counter += 1
        except:
            continue
    res_vector = total_vector / total_counter
    return res_vector


def normalize_lemmas(lemmas_raw):
    """Parses a string of lemmas+POS column values to work with it later:
    - separates the values,
    - strips extra characters of values in a given string list,
    so that they do not make extra noise with later preprocessing.
    
    :arg lemmas_raw — (str) list of NER values to parse, all in a single 
    string
    
    :returns ner_cleaned — (list of str) list of NER values as separate objects
    """
    lemmas_separated = lemmas_raw.split(", ")
    lemmas_cleaned = [item.strip(", ''][") for item in lemmas_separated]
    return lemmas_cleaned


def get_clean_df(direction_type, label_type):
    """Reads dataframe source file and returns it with all column values
    converted to appropriate values.

    :arg direction_type — (str) type of directions to open (e.g. setting)
    :arg label_type — (str) type of labels to open (e.g. train)

    :returns df — (pd.DataFrame) parsed dataframe with right types of column
    values
    """
    df = pd.read_csv("./data/ml/{}_X_{}.csv".format(direction_type, label_type), sep=";", encoding="utf-8")
    df["wv_items"] = df["wv_items"].apply(normalize_lemmas)
    df.drop(["Unnamed: 1"], axis=1, inplace=True)
    return df

def get_X_for_rules(direction_type, label_type):
    X_df = pd.read_csv("./data/ml/{}_X_{}.csv".format(direction_type, label_type), sep=";", encoding="utf-8")
    X_df["wv_items"] = X_df["wv_items"].apply(normalize_lemmas)
    X = X_df["wv_items"].values
    return X

pos_cols = ["INTJ", "APRO", "SPRO", "ADVPRO", "PERSN", "NUM", "A", "ANUM", "ADV", "S", "PR", "PART"]


def df_to_X(df):
    """Computes a total feature array from dataframe information on POS count
    and word2vec vectors.
    
    :args df — (pd.DataFrame) a dataframe from processed directions
    
    :returns X — (np.array) feature vector ready for fitting/predicting
    """
    X_pos = df[pos_cols].values
    X_w2v = np.array([compute_vector(model, wv_items) for wv_items in df["wv_items"].values])
    
    X = np.hstack((X_pos, X_w2v))
    X = np.nan_to_num(X)
    return X

def get_labels(direction_type, labels_type):
    """Reads a CSV file and returns list of labels for a certain direction and label.

    :arg direction_type — (str) type of directions to open (e.g. setting)
    :arg label_type — (str) type of labels to open (e.g. train)

    :returns y — (np.array) labels for corresponding items in X
    """
    with open("./data/ml/{}_y_{}.csv".format(direction_type, labels_type), "r", encoding="utf-8") as f:
        y = np.array([int(x.strip("\n")) for x in f.readlines()])
    return y


def get_X_y_type(direction, subset):
    """Returns a pair of feature vectors and their labels.

    :arg direction — (str) type of directions to open (e.g. setting)
    :arg subset — (str) type of labels to open (e.g. train)

    :returns X_type — (np.array) feature vectors
    :returns y_type — (np.array) labels
    """
    df_type = get_clean_df(direction, subset)
    X_type = df_to_X(df_type)
    y_type = get_labels(direction, subset)
    return X_type, y_type
