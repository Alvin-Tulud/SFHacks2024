# FILE: webscraper.py
# DESC: Receive coordinate data from page,
#       Access restaurants in that area
#       Create a JSON for each restaurant
#       Compile JSONs to one JSON and send to DB

# GOOGLE API KEY : AIzaSyANkTF_7wo_8s38cNPil-miLez52QerTzU

import requests
import json
import googlemaps
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__,template_folder="templates") 

CORS(app)

@app.route('/getLocation', methods=['POST'])

def getLocation():
    # Receive latitude and longitude from JavaScript
    data = request.get_json()
    ltd = data.get('ltd')
    lng = data.get('lng')

    if ltd is not None and lng is not None:
        main(ltd, lng)
        return "Data received successfully."
    else:
        return "Latitude or longitude data is missing."

# Initialize Google Maps client
api_key = 'AIzaSyANkTF_7wo_8s38cNPil-miLez52QerTzU'
gmaps = googlemaps.Client(key=api_key)

def get_reviews(place_id):
    try:
        place_details = gmaps.place(place_id)
        if 'reviews' in place_details['result']:
            reviews = place_details['result']['reviews']
            review_strings = [review['text'] for review in reviews]
            return review_strings
        else:
            return []
    except Exception as e:
        print("Error:", e)
        return []

def get_restaurants(latitude, longitude, radius=2, keyword='restaurant'):
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={radius * 1609.34}&keyword={keyword}&key={api_key}'
    response = requests.get(url)
    data = response.json()
    return data['results']

def create_restaurant_json(restaurant):
    name = restaurant.get('name', 'Unknown')
    rating = restaurant.get('rating', 0.0)
    about = restaurant.get('vicinity', 'No information available.')
    
    # Get place_id
    place_id = restaurant.get('place_id')
    # Get reviews for the restaurant
    reviews = get_reviews(place_id)

    restaurant_json = {
        "Name": name,
        "Rating": rating,
        "About": about,
        "Reviews": reviews
    }
    return restaurant_json

def main(ltd, lng):
    # TODO: Receive ltd & lng from Javascript
    restaurants = get_restaurants(ltd, lng)
    all_restaurants = []
    for restaurant in restaurants:
        restaurant_info = create_restaurant_json(restaurant)
        all_restaurants.append(restaurant_info)

    with open('restaurants.json', 'w', encoding='utf-8') as json_file:
        json.dump(all_restaurants, json_file, indent=4, ensure_ascii=False)  # Set ensure_ascii to False

if __name__ == "__main__":
    main()
