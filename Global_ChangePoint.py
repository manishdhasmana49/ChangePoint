#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 08:54:32 2020

@author: manish
"""
import numpy as np
import pyhomogeneity as hg
import pandas as pd

data=np.genfromtxt("/media/manish/Other/IMD_data/JJAS/Domain_IMD.txt")
df=pd.DataFrame(data[:,3],index = pd.date_range('01.01.1901',periods = len(data[:,3]),freq ='Y', name = 'date'),columns=["JJAS_IMD"])
roll=df.rolling(10).mean() 
roll.plot()
roll=roll.dropna()

h, cp, p, U, mu = hg.pettitt_test(roll,0.05)