import gensim
import numpy as np
import warnings
import wget
import zipfile

# globals
warnings.simplefilter("ignore")


def vec_similarity(v1, v2):
    v1_norm = gensim.matutils.unitvec(np.array(v1).astype(float))
    v2_norm = gensim.matutils.unitvec(np.array(v2).astype(float))
    return np.dot(v1_norm, v2_norm)


def get_w2v_vectors(text, model):
    total_counter = 0
    total_vector = np.zeros(300)
    for word in text:
        try:
            vector = np.array(model.wv[word])
            total_vector += vector
            total_counter += 1
        except:
            continue
    res_vector = total_vector / total_counter
    return res_vector


def assign_tei_type(direction):
    tei_type = ""

    with zipfile.ZipFile("./data/models/180.zip", "r") as archive:
        stream = archive.open("model.bin")
        model = gensim.models.KeyedVectors.load_word2vec_format(stream, binary=True)
    
    most_similar_entrance = set([similar[0] for similar in model.most_similar("входить_VERB")])
    most_similar_exit = set([similar[0] for similar in model.most_similar("уходить_VERB")])

    verbs_list = [item for item in direction if item.endswith("VERB")]
    print(verbs_list)
    for verb in verbs_list:
        # case 1 -- verb in most_common for a type
        # in this case, we return the type immediately
        if verb in most_similar_entrance:
            print("found {}, it's entrance!".format(verb))
            tei_type = "entrance"
            return tei_type
        elif verb in most_similar_exit:
            print("found {}, it's exit!".format(verb))
            tei_type = "exit"
            return tei_type
        # case 2 -- verb is unknown
        else:
            direction_vector = get_w2v_vectors(verbs_list, model)
            similarity_entrance = vec_similarity(direction_vector, model.wv["войти_VERB"])
            similarity_exit = vec_similarity(direction_vector, model.wv["выйти_VERB"])
            if similarity_entrance > similarity_exit:
                tei_type = "entrance"
            else:
                tei_type = "exit"
    print("final decision: {}".format(tei_type))
    return tei_type