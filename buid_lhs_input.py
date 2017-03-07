from pyDOE import lhs
import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

import build_lhs as bh


def main():

    IS = [ [0, 0.02], #U5
           [0.03, 0.2], #Pu+MA fraction
           [0,0.01],    #Pu236
           [0,0.02],    #Pu238
           [0,0.2],     #Pu240
           [0,0.04],    #Pu241+Am241
           [0,1],       #Pu241/(Pu241+Am241)
           [0,0.01],    #Pu242
           [0,0.06],    #Np237
           [0,0.001],   #Am242m
           [0,0.001],   #Am243
           [0,0.001],   #Cm242
           [0,0.001],   #Cm243
           [0,0.001],   #Cm244
           [0,0.001],   #Cm245
           [0,0.001]    #Cm246
         ]

    myLHS = bh.build_LHS(16, 1000, 'corr', 20, 'outdat', plot=False,
        verbose=False)
    nm_LHS = bh.normalyse_LHS(myLHS, IS)
    bh.plot(nm_LHS, 'myLHS')
    bh.write(nm_LHS,'myLHS')
    bh.plot(myLHS, 'myLHS_raw')






if __name__ == "__main__":
    main()
