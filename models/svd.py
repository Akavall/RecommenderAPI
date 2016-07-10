import numpy as np

class SVD_Model(object):
    def __init__(self, actions, n_singular_values):
        self.actions = actions
        self.n_singular_values = n_singular_values

    def calc_scores(self):
        u, s, vt = np.linalg.svd(self.actions, full_matrices=self.n_singular_values)

        diag_s = np.zeros((len(u), len(vt)), dtype=complex)
        s[self.n_singular_values:] = np.zeros(len(s) - self.n_singular_values)
        np.fill_diagonal(diag_s, s)

        return np.dot(u, np.dot(diag_s, vt))
