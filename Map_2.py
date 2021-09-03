from flask import Flask, render_template
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/')
def get_data():
    geolocator = Nominatim(user_agent='map_marker')
    country = geolocator.geocode("Japan")
    loc_list = []
    with open('japan_travel_list', 'r') as file1:
        for line in file1:
            loc_list.append(geolocator.geocode(line))
            loc_dict = {loc.latitude: loc.longitude for loc in loc_list}
        return render_template('map.html', country=country, coordinates=loc_dict)


if __name__ == '__main__':
    app.run(debug=True)