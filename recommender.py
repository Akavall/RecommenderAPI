import numpy as np
import pandas as pd

class Recommender(object):
    def __init__(self):
        self.actions = None
        self.user_id_to_ind = None
        self.ind_to_user_id = None
        self.item_id_to_ind = None
        self.ind_to_item_id = None 

    def initialize_matrices(self, long_format_df):
        print "Initializing Matrices"
        temp = long_format_df.set_index([long_format_df.columns[0], long_format_df.columns[1]])
        user_item = temp.index.tolist()
        
        user_ids = {u for u, i in user_item}
        item_ids = {i for u, i in user_item}

        self.user_id_to_ind = {u: ind for ind, u in enumerate(user_ids)}
        self.item_id_to_ind = {i: ind for ind, i in enumerate(item_ids)}
        self.ind_to_user_id = {v: k for k, v in self.user_id_to_ind.iteritems()}
        self.ind_to_item_id = {v: k for k, v in self.item_id_to_ind.iteritems()}

        user_item_inds = []
        for user_id, item_id in user_item:
            user_item_inds.append((self.user_id_to_ind[user_id], self.item_id_to_ind[item_id]))

        user_item_inds = np.array(user_item_inds)

        actions = np.zeros((len(self.user_id_to_ind), len(self.item_id_to_ind)))
        actions[user_item_inds[:, 0], user_item_inds[:,1]] = 1.0
        self.actions = actions 

    def make_recs(self, scores, n_recs):
        rec_inds = np.argsort(-scores)[:, :n_recs].tolist()
        recs = {}
        for ind, ele in enumerate(rec_inds):
            recs[self.ind_to_user_id[ind]] = (map(self.ind_to_item_id.get, ele))
        self.recs = recs
        return self.recs 

    def convert_recs_to_csv_string(self):
        df = pd.DataFrame(self.recs)
        self.csv_string_recs = df.T.to_csv(header=None)
