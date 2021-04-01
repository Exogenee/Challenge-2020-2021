#%%
from zipfile import ZipFile
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from pandas.io json import json_normalize
import matplotlib.pyplot as plt
%matplotlib notebook
# %%
file = "MMM_EcoCompt_Archives.zip"

with ZipFile (file, "r") as zip:
    zip.printdir()      #contenu du fichier
    zip.extract("MMM_EcoCompt_X2H19070220_Archive2020.json", r"C:\Users\HP\Projet_vélo")
    zip.close()

#%%
url = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220_archive.json"
df = pd.read_json(url)
# %%
df.drop_duplicates(subset=['dateObserved'], keep='last')

#%%
df1 = df.copy()
del df1 ['type']
del df1 ['reversedLane']
del df1 ['vehicleType']
del df1 ['id']
del df1 ['laneId']
#%%
mtp = folium.Map(location=[43.610782, 3.876153], zoom_start=12)
mtp.add_child(folium.GeoJson('MMM_MMM_GeolocCompteurs.geojson'))
display(mtp)
# %%
folium.Choropleth(geo_data = 'MMM_MMM_GeolocCompteurs.geojson', data = df1, columns = ['','intensity'], key_on = 'feature.geometry.coordinates').add_to(mtp)
# %%
