import folium
map = folium.Map(location=[51.1657, 10.4515],
                 zoom_start=6, tiles="Stamen Terrain")
map.save("MapDEU11.html")
