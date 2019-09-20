# Short Text Classification: a Case of Stage Directions in Russian Drama
This is a repository for BA thesis written in School of Linguistics, NRU HSE (Moscow, RU), throughout the 2018/19 academic year. 

## What is this about?

I already did a project on Russian Drama Corpus and its stage directions — it can be found here: [Stage Directions in Russian Drama](https://github.com/creaciond/russian-drama). It dealt more with the quantitative part of the research and exploring corpus trends; at this one, I want to focus on the part which deals more with computational linguistics and machine learning, that is to extract linguistic features and run several different models.

Russian Drama Corpus (or shortly, RusDraCor) can be found at [dracor-org/rusdracor](https://github.com/dracor-org/rusdracor); it is also available in a more user-friendly format at [Dracor website](https://dracor.org/rus).

## What's inside?

### Code

|**Content**|**Notebook**|**Additional**|
|:--:|:--:|:--:|
|retrieving and downloading data|[api-data-preprocessing.ipynb](./api-data-preprocessing.ipynb)|[dracor_api.py](./dracor_api.py), [file_work.py](./file_work.py)|
|annotation description||[annotation_guide.md](./annotation_guide.md)|
|morphology, NER, stopwords, etc.|[linguistic-features.ipynb](./linguistic-features.ipynb)||
|semantics hypothesis + test on 2018 data|[semantic-rules.ipynb](./semantic-rules.ipynb)||
|working with the final dataset|[dataset-separation.ipynb](./dataset-separation.ipynb)||
|model fitting: _entrance_  and _exit_|[fitting-semantic-types.ipynb](./fitting-semantic-types.ipynb)|[data_preparation.py](./data_preparation.py), [model_fitting.py](./model_fitting.py), separate semantic class to come|
|model fitting: other types|[fitting-nonsemantic-types.ipynb](./fitting-nonsemantic-types.ipynb)|[data_preparation.py](./data_preparation.py), [model_fitting.py](./model_fitting.py)|

### Original paper

Is also here in the repo: [pdf](./maksimova_dm_short-text-classification-a-case-of-stage-directions-in-russian-drama.pdf)

### Slides

TEI 2019 (Sep 20, 2019): [Using Machine Learning for the Automated Classification of Stage Directions in TEI-Encoded Drama Corpora](https://shorturl.at/jEFJR)

Thesis defence (Jun 17, 2019): [Short Text Classification: a Case of Stage Directions in Russian Drama](./2019-06-17_presentation.pdf)

## Important dates

|**Module**|**Event**                    |**Date**             |
|:--------:|:---------------------------:|:-------------------:|
|3rd       |Project Proposal presentation|March 26, 2019|
|4th       |Written paper deadline       |June 4, 2019|
|4th       |Final thesis presentation    |June 18, 2019|
