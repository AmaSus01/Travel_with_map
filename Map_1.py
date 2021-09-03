import geopy
import plotly.graph_objects as go

map_access_token = open(".mapbox_token").read()
latti = []
longi = []
full_text = []

with open('japan_travel_list', 'r') as file1:
    for line in file1:
        if line == '\n':
            pass
        else:
            geoTag = line
            locator = geopy.Nominatim(user_agent='myGeocoder')
            location = locator.geocode(geoTag)

        #print("Latitude={}, Longitude={}".format(location.latitude, location.longitude)) # проверка координат
            latti.append(location.latitude)
            longi.append(location.longitude)
            full_text.append(line)

    fig = go.Figure(go.Scattermapbox(
        lat= latti,
        lon= longi,
        mode='markers',
        marker= go.scattermapbox.Marker(
            size=14,
            color= 'rgb(128, 0, 128)',
        ),
        text=full_text,
    ))

    fig.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=map_access_token,
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=int(location.latitude),
                lon=int(location.longitude)
            ),
            pitch=0,
            zoom=5
                )
            )
    fig.show()