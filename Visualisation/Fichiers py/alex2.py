#%%
import numpy as np
import json
import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_row',96)
#%%
data[1] = pd.read_json("Visualisation1.json", lines = True)
data[2] = pd.read_json("Visualisation2.json", lines = True)
data[3] = pd.read_json("Visualisation3.json", lines = True)
data[4] = pd.read_json("Visualisation4.json", lines = True)
data[5] = pd.read_json("Visualisation5.json", lines = True)
data[6] = pd.read_json("Visualisation6.json", lines = True)
data[7] = pd.read_json("Visualisation7.json", lines = True)
data[8] = pd.read_json("Visualisation8.json", lines = True)

# %%
loc = {}
df = {}
for i in np.arange (1,9): 
    loc[i] = data[i]['location'][0]
    df[i] = data[i].shape

#%%
def f(df):
    df['date'] = data[df].index
    data[zip]

    for i in np.arange(0,df[i].shape[0]):
        df['date'][i] = data[df].index[i][0:10]
    
    data[df]['date'] = pd.to_datetime(data[df]'date'])
    data[df].index = data[df]['date']

    jour = pd.date_range(start='17/12/2020', end='25/03/2021')

    data[df] = data[df].reindex(jour)
    data[df]['date'] = data[df].index
    data[df] = data[df].fillna(0)


# %%
for i in np.arange(1,9):
    date(i)
# %%
