#%%
import folium

# %%
m = folium.Map(location=[43.616482, 3.874153], zoom_start = 20)
m.save("index.html")

#%%
folium.Marker(
    location=[43.616482, 3.873125],
    popup="Mt. Hood Meadows",
    icon=folium.Icon(icon="cloud"),
).add_to(m)

# %%
folium.Map(location=[45.372, -121.6972],
           zoom_start=12)
           
# %%
z = folium.Map(location=[43.616482, 3.874153], 
zoom_start=20, tiles="Stamen Toner")

folium.Circle(
    radius=10,
    location=[43.616489, 3.874159],
    popup="The Waterfront",
    color="crimson",
    fill=False,
).add_to(z)

folium.CircleMarker(
    location=[43.616482, 3.878153],
    radius=5,
    popup="Laurelhurst Park",
    color="#3186cc",
    fill=True,
    fill_color="#3186cc",
).add_to(z)

z

#quand on baisse la premiere décimale, le point descend bcp
# %%
