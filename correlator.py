import pandas as pd
from pandas import DataFrame
import seaborn as sns

data = {
    'Runs Scored': [1107,1101,1011,1016,1017,1104,1023,837],
    'Home Runs': [392,324,312,303,342,334,319,252],
    'Total Bases': [3329,3296,3057,2975,3159,3273,3152,2625],
    'RBI': [1068,988,983,912,1038,1000,1017,832],
    'Game Winning RBI': [138,100,120,104,127,105,110,85],
    'Walks': [874,683,704,624,637,711,674,527],
    'Int Walks': [50,40,39,21,50,48,42,20],
    'Struck out': [1575,1525,1496,1503,1283,1474,1548,1411],
    'Hit By Pitch': [100,99,72,67,82,65,65,71],
    'Steals': [46,118,139,77,95,117,154,96],
    'Caught S': [20,38,33,25,30,40,46,42],
    'Cycles': [0,0,0,1,0,0,2,0],
    'GSHR': [8,7,4,7,5,9,8,2],
    'IP': [1497.2,1202.2,1469.2,1335.0,1331.1,961.1,781.1,1089.2],
    'H Allowed': [1392,1092,1341,1175,1259,981,696,961],
    'ER': [674,513,627,564,613,440,353,474],
    'Walks Issued': [431,352,406,328,396,311,301,381],
    'Strikeouts': [1598,1199,1700,1493,1342,994,952,1284],
    'QS': [128,95,133,116,111,63,42,96],
    'Complete Games': [3,2,6,6,2,0,1,2],
    'Shutouts': [3,1,4,3,1,0,0,2],
    'No Hitters': [0,0,0,1,0,0,0,0],
    'Perfect': [0,0,0,0,0,0,0,0],
    'Saves': [0,70,6,63,8,102,91,51],
    'Holds': [1,11,2,6,2,4,1,9],
    'Wins': [16,12,12,11,10,9,7,7]
}

df = pd.DataFrame(data)
corr = df[df.columns[1:]].corr()

heatmap = sns.heatmap(corr,
                      vmin=-1, vmax=1, center=0,
                      cmap=sns.diverging_palette(20, 220, n=200),
                      square=True
                      )

heatmap.get_figure().savefig("output.png")

print(corr['Wins'][:].sort_values(ascending=False))
