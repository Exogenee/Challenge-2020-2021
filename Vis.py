#%%
import pandas as pd
import json
from download import download
import folium

#%%
df = pd.read_json("MMM_EcoCompt_X2H19070220_Archive2020.json")
# %%
df.drop_duplicates(subset=['dateObserved'], keep='last')
# %%
#df1 = df.copy()
#del df1 ['type']
#del df1 ['reversedLane']
#del df1 ['vehicleType']
#del df1 ['id']
#del df1 ['laneId']
# %%
url = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_MMM_GeolocCompteurs.geojson"
download(url,path = "./MMM_MMM_GeolocCompteurs.geojson", )
#df = pd.read_json(url)
#%%
#url = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220_archive.json"
#df = pd.read_json(url)
# %%
mtp = folium.Map(location=[43.610782, 3.876153], zoom_start=12)
mtp.add_child(folium.GeoJson('MMM_MMM_GeolocCompteurs.geojson'))
display(mtp)
# %%
folium.Choropleth(geo_data = 'MMM_MMM_GeolocCompteurs.geojson', data = df1, columns = ['','intensity'], key_on = 'feature.geometry.coordinates').add_to(mtp)
# %%
