import pandas as pd
import numpy as np
import random
from itertools import combinations

def sampleeee(objecttt,unique):
    # actually it's random_combination
    index_list = sorted(random.sample(range(len(objecttt)),unique))
    return tuple(objecttt[i] for i in index_list)
def vector_angleN(v1,v2):
    if np.inner(v1,v2) != 0:
        angle = np.degrees(np.arccos(np.inner(v1,v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))))
    return angle
def winning_declare(board,side):
    NiNi_the_best = []
    vector_list = []
    for row in range(len(board)):
        a = df.loc[df[str(row)]==str(side)].index.tolist()
        for i in range(len(a)):
            NiNi_the_best.append(np.array([row, a[i]]))
    comb = [pair for pair in combinations(NiNi_the_best,2)]
    for i in range(len(comb)):
        vector_list.append(comb[i][1]-comb[i][0])
    combb = [pairr for pairr in combinations(vector_list,2)]
    # return combb
    for i in range(len(combb)):
        # why 0 or 180 will return all(C6,2)
        if vector_angleN(combb[i][0],combb[i][1]) == 0:
            print("Win")

df = pd.DataFrame({'0': ['O','X','O'],
                  '1': ['O','X','Na'],
                  '2': ['O','X','Na']})

winning_declare(df)