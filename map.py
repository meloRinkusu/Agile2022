# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Import library

import folium
from flask import Flask

#%%
"""

coords_dep = [42.6585, 9.4151]
coords_end = [42.7017, 9.4466]
ville = ""
tooltip = "clique ici"


m = folium.Map(location = coords_dep)

#Make marker
folium.Marker(coords_dep, popup=f"<i>Depart</br>{coords_dep}</i>", 
              tooltip = tooltip, 
              icon=folium.Icon(color="green")).add_to(m)
folium.Marker(coords_end, popup=f"<i>Arrivée</br>{coords_end}</i>", 
              tooltip = tooltip, 
              icon=folium.Icon(color="red")).add_to(m)


#save page .html
m.save("C:/Users/Utilisateur/Desktop/gps.html")"""
#%%


app = Flask(__name__)


@app.route('/')
def index():
    coords_dep = [42.6585, 9.4151]
    coords_end = [42.7017, 9.4466]
    ville = ""
    tooltip = "clique ici"
    
    m = folium.Map(location=coords_end, zoom_start=5)
    
    #Make marker
    folium.Marker(coords_dep, popup=f"<i>Depart</br>{coords_dep}</i>", 
                  tooltip = tooltip, 
                  icon=folium.Icon(color="green")).add_to(m)
    folium.Marker(coords_end, popup=f"<i>Arrivée</br>{coords_end}</i>", 
                  tooltip = tooltip, 
                  icon=folium.Icon(color="red")).add_to(m)
    
    
    return m._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)