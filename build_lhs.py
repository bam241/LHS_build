#!/usr/bin/env python

import matplotlib
matplotlib.use('Agg')

from pyDOE import lhs
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def main():
    dim = int(sys.argv[1])
    sample = int(sys.argv[2])
    it = int(sys.argv[3])
    method = sys.argv[4]

    my_LHS = lhs(dim, samples=sample, criterion=method, iterations=it)
    df = pd.DataFrame(my_LHS)
    g = sns.PairGrid(df)
    g.map_diag(sns.kdeplot)
    cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
    g.map_offdiag(sns.kdeplot, cmap=cmap, n_levels=60, shade=True);
    g.savefig("output.png")

if __name__ == "__main__":
        main()
