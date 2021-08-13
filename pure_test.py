import pandas as pd
import numpy as np
from itertools import combinations
import pygame
df = pd.DataFrame({'0':[],'1':[],'2':[]},columns={'0','1','2'})
df.loc['0'].append('O')
print(df)