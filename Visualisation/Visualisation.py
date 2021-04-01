# %%
import numpy as np
import pandas as pd
import folium
import matplotlib.pyplot as plt
import json
pd.set_option('display.max_rows',6)
#%%
#Création de mes dataframes
data = {}
data[1] = pd.read_json("Visualisation1.json", lines = True)
data[2] = pd.read_json("Visualisation2.json", lines = True)
data[3] = pd.read_json("Visualisation3.json", lines = True)
data[4] = pd.read_json("Visualisation4.json", lines = True)
data[5] = pd.read_json("Visualisation5.json", lines = True)
data[6] = pd.read_json("Visualisation6.json", lines = True)
data[7] = pd.read_json("Visualisation7.json", lines = True)
data[8] = pd.read_json("Visualisation8.json", lines = True)
#%%
loc = {}
for i in np.arange(1,9):
    data[i] = data[i].groupby(by='dateObserved').sum('intensity')
    loc[i] = data[i]['location'][0]
# %%
f={}
for i in np.arange(1,9):
    f[i] = data[i].shape
f
#%%
def df(f):

    data[f]['date'] = data[f].index
    data[f]

    for i in np.arange(0,data[f].shape[0]):
        data[f]['date'][i] = data[f].index[i][0:10]

    data[f]['date'] = pd.to_datetime(data[f]['date'])
    data[f].index = data[f]['date']
    jour = pd.date_range(data[f]['date'].min(), data[f]['date'].max(), freq='D')  
    data[f] = data[f].reindex(jour)
    data[f]['date'] = data[f].index
    data[f] = data[f].fillna(0)
# %%
for i in np.arange(1,9):
    df(i)
# %%
w = []
Montpellier = {}
for k in np.arange(0,data[1].shape[0]):
    Montpellier[k] = folium.Map(location =[43.610782, 3.876153], #localisation de Montpellier centre
    zoom_start=12)
    for l in np.arange(1,9):
        w = list(loc[l].values())[0]
        f = w[0]
        w[0] = w[1]
        w[1] = f
        folium.CircleMarker(radius=data[l]['intensity'][k]/50, location=w, fill=True, popup=f"Intensité:{data[l]['intensity'][k]} Jour:{str(data[l]['date'][k])[0:10]}").add_to(Montpellier[k])
    Montpellier[k].save(f"Montpellier{str(data[l]['date'][k])[0:10]}.html")
Montpellier[0]

#Pour la création du gif, j'ai converti mes fichiers html en fichiers png pour faire le gif mais malgré ça je n'ai pas réussi à le créer via python, je l'ai quand 
#même fait avec un site gratuit pour en avoir un.