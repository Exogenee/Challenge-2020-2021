# %%
import numpy as np
import pandas as pd
import folium
import matplotlib.pyplot as plt
import json
import imageio
import os
pd.set_option('display.max_rows',6)
#%%
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
    data[i] = pd.read_json(f'Visualisation{i}.json',lines=True)
    loc[i] = data[i]['location'][0]
    data[i] = data[i].groupby(by='dateObserved').sum('intensity')
    data[i].drop(columns=['laneId','reversedLane'], inplace=True)
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
points = []
Montpellier = {}
for k in np.arange(0,data[1].shape[0]):
    Montpellier[k] = folium.Map(location =[43.610782, 3.876153], 
    zoom_start=12)
    for l in np.arange(1,9):
        points = list(loc[l].values())[0]
        f = points[0]
        points[0] = points[1]
        points[1] = f
        folium.CircleMarker(radius=data[l]['intensity'][k]/50, location=points, fill=True, popup=f"Intensité:{data[l]['intensity'][k]} Jour:{str(data[l]['date'][k])[0:10]}").add_to(Montpellier[k])
    Montpellier[k].save(f"Montpellier{str(data[l]['date'][k])[0:10]}.html")
Montpellier[0]
# %%
dossier = 'C:/Users/HP/Projet_vélo/Visualisation/Photos_html'
dossiers = [f"{dossier}\\{file}" for file in os.listdir(dossier)]

images = [imageio.imread(file) for file in dossiers]
imageio.mimwrite('Visualization_gif', images, fps=1)
# %%
