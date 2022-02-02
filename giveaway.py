import pandas as pd
import random

df = pd.read_csv(f'wallets.csv',names=['fans'])
fans = df['fans'].unique().tolist()

giveaway = int(input('enter the number to giveaway '))

print(f'\nGenerating a random selection of {giveaway} to giveaway!\n')

lst = [*range(0,df.shape[0]+1)]

for i in range(0,giveaway):
    x = random.choice(lst)
    y = random.choice(fans)
    print(i+1,x,y)
    lst.pop(lst.index(x))
    fans.pop(fans.index(y))

print('\n')
