import numpy as np
import pandas as pd

# gen seed
# reachout(int peepSample, int howManyDays)
# cntcs['num_legs'].sample(n=3, random_state=1)
def reachout(cntcsDf, peepSample, howManyDays):
    for d in range(howManyDays):
        print(f'`~..... Day {d+1} .....~`')
        samp = cntcsDf.sample(n=peepSample)
        for p in range(peepSample):
            name, numb = samp['Name'].iloc[p], samp['Number'].iloc[p]
            print(f'@@@ Reachout to {name} @@@')
            print(f'!!! Their number is {numb} !!!')
            
    
if __name__ == "__main__":
    cntcs = pd.read_csv('CNTCTS.csv')
    reachout(cntcs, 3, 90)