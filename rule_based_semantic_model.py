# encoding: utf-8

import gensim
import numpy as np
import pandas as pd
import wget
import zipfile

from sklearn.metrics.pairwise import cosine_similarity

class SemanticRuleClassfier:

    def __init__(self):
        """Initiates a classifier.
        """
        print("Started loading w2v model")
        with zipfile.ZipFile("./data/models/180.zip", "r") as archive:
            stream = archive.open("model.bin")
            model = gensim.models.KeyedVectors.load_word2vec_format(stream,
                binary=True)
        self.model = model
        print("Loaded w2v model")
        self.similar_entrance = set([v[0] for v in model.most_similar("входить_VERB")])
        self.similar_exit = set([v[0] for v in model.most_similar("уходить_VERB")])
        print("Stored most similar verbs")

    def check_for_similar(self, direction_verbs):
        """Easiest prediction case — direction contains a verb from the list
        of most similar verbs either for entrance or for exit.

        :args direction_verbs — (list of str) verbs to check

        :returns direction type — (str) one of the values: "entrance", "exit", or an empty string
        """
        for verb in direction_verbs:
            if verb in self.similar_entrance:
                return "entrance"
            elif verb in self.similar_exit:
                return "exit"
            else:
                return ""
    
    def compute_vector(self, direction_verbs):
        """Computes a word2vec vector for a given list of tokens in the direction.
        Tokens are preprocessed lemmas combined with their part of speech in 
        Universal Text format.

        :args direction_verbs — (list of str) direction verbs

        :returns res_vector — (np.array) vector for the direction with given tokens
        """
        total_counter = 0
        total_vector = np.zeros(300)
        for verb in direction_verbs:
            try:
                vector = np.array(self.model.wv[verb])
                total_vector += vector
                total_counter += 1
            except:
                continue
        res_vector = np.array(total_vector / total_counter)
        return res_vector

    def non_similar_case(self, direction_vector):
        """Decides on a direction type based on overall w2v vector for a direction.

        :args direction_vector — (np.ndarray) pre-computed vector for a direction to 
        classify

        :returns dir_type — (str) chosen type
        """
        sim_entrance = cosine_similarity(direction_vector, self.model.wv["входить_VERB"])
        sim_exit = cosine_similarity(direction_vector, self.model.wv["уходить_VERB"])
        if sim_entrance > sim_exit:
            dir_type = "entrance"
        elif sim_entrance < sim_exit:
            dir_type = "exit"
            return dir_type
    
    def single_prediction(self, direction_verbs):
        """Unites all types of classifying and predicts the label for a single passed
        direction based on the rules.

        :args direction_verbs — (list of str) direction verbs

        :returns dir_type — (str) assigned type
        """
        dir_type = self.check_for_similar(direction_verbs)
        print("frequency check: {}".format(dir_type))
        if dir_type == "":
            print("computing vector")
            direction_vector = self.compute_vector(direction_verbs)
            dir_type = self.non_similar_case(direction_vector)
        print("final decision: {}".format(dir_type))
        return dir_type
    
    def predict(self, directions, goal_label):
        """Overall prediction function.

        :args directions — (list of [list of strs]) all directions to classify

        :goal_label — (str) the type which is under question. Model will return 1
        if the predicted label matches the goal label, otherwise 0
        """
        labels_pred = []
        for direction in directions:
            print(direction)
            label_pred = self.single_prediction(direction)
            print("Preicted: ", label_pred)
            print("Goal: ", goal_label)
            if label_pred == goal_label:
                labels_pred.append(1)
            else:
                labels_pred.append(0)
        return np.array(labels_pred)
