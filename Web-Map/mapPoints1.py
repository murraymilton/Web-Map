import folium
map = folium.Map(location=[51.1657, 10.4515],
                 zoom_start=6, tiles="Stamen Terrain")
map.add_child(folium.Marker(
    location=[51.0, 10.1], popup="POI: List here", icon=folium.Icon(color="red")))
map.save("MapDEU11.html")
