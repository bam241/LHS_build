from pyDOE import lhs
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

import build_lhs as bh


def main():

    IS = [ [0, 0.001], #U4
           [0.03, 0.2], #u5
           [0.03, 0.05], #u6
           [0,0.01],    #Pu238
           [0,0.2],    #Pu239
           [0,0.1],     #Pu240
           [0,0.02],    #Pu241
           [0,0,02],       #Pu242
           [0,0.01],    #Np237
           [0,0.01],    #Am241
           [0,0.001],   #Am242m
           [0,0.01],   #Am243
           [0,0.0001],   #Cm242
           [0,0.0001],   #Cm243
           [0,0.01],   #Cm244
           [0,0.001],   #Cm245
           [0,0.001]    #Cm246
         ]

    myLHS = bh.build_LHS(17, 5000, 'corr', 20, 'outdat', plot=False,
        verbose=False)
    nm_LHS = bh.normalyse_LHS(myLHS, IS)
    bh.plot(nm_LHS, 'myLHS')
    bh.write(nm_LHS,'myLHS')
    bh.plot(myLHS, 'myLHS_raw')






if __name__ == "__main__":
    main()
