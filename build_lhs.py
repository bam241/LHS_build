#!/usr/bin/env python
import sys
import argparse

import matplotlib
matplotlib.use('Agg')

from pyDOE import lhs
import numpy as np
import pandas as pd
from scipy import stats, integrate
import seaborn as sns


def build_LHS(dim, sample, method, it):
    return lhs(dim, samples=sample, criterion=method, iterations=it)


def build_plot(LHS, filename):
    df = pd.DataFrame(LHS)
    g = sns.PairGrid(df)
    g.map_diag(sns.kdeplot)
    cmap = sns.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=True)
    g.map_offdiag(sns.kdeplot, cmap=cmap, n_levels=60, shade=True);
    g.savefig(filename)


def write_LHS(LHS, filename):
    np.savetxt(filename, LHS)


def normalyse_LHS(LHS, boundary):
    if len(LHS[0]) != len(boundary):
        print("Need ", len(LHS[0]),
              "boundary, please fix it, normalization not done!")
        return LHS
    else:
        for i in range(len(LHS)):
            for j in range(len(LHS[i])):
                a, b=boundary[j]
                LHS[i][j]=(b - a) * LHS[i][j] + a
        return LHS

def main():

    parser=argparse.ArgumentParser()
    parser.add_argument("dim", type=int,
                                help="Latin HyperCube dimension")
    parser.add_argument("sample", type=int,
                                help="Latin HyperCube points number")
    parser.add_argument("-i", "--iteration", type=int, default=10,
                                help="number of iteration")
    parser.add_argument("-m", "--method", type=str, default='maximin',
            help="Genration method for the LHS: center(c), maximin(m), centermaximin (cm), correlation(corr) ")
    parser.add_argument("-o", "--outfile", type=str, default='LHS',
            help="output base name, xx.pdf, xx.png")
    parser.add_argument(
        "-p", "--plot", help="Generate a plot with the LHS distribution", action="store_true")
    parser.add_argument("-v", "--verbose",
                        help="Verbose mode...", action="store_true")

    try:
        args=parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)

    # Load argument
    dim=args.dim
    sample=args.sample
    it=args.iteration
    method=args.method

    # generate LHS
    my_LHS=build_LHS(dim, sample, method, it)

    if args.verbose:
        print(my_LHS)

    # Nice LHS ploting
    if args.plot:
        outpng=args.outfile + '.png'
        build_plot(my_LHS, outpng)

    # Write LHS down
    outdat=args.outfile + '.dat'
    write_LHS(my_LHS, outdat)


if __name__ == "__main__":
        main()
