# FILE: webscraper.py
# DESC: Receive coordinate data from page,
#       Access restaurants in that area
#       Create a JSON for each restaurant
#       Compile JSONs to one JSON and send to DB

# GOOGLE API KEY : AIzaSyANkTF_7wo_8s38cNPil-miLez52QerTzU

import requests
import json
import googlemaps


import Flask,render_template, request 
  
app = Flask(__name__,template_folder="templates") 
  
@app.route("/") 
  
@app.route('/getLocation', methods=['POST']) 


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

def main():
    # TODO: Receive ltd & lng from Javascript
    ltd = 37.565094
    lng = -122.321859
    restaurants = get_restaurants(ltd, lng)
    all_restaurants = []
    for restaurant in restaurants:
        restaurant_info = create_restaurant_json(restaurant)
        all_restaurants.append(restaurant_info)

    with open('restaurants.json', 'w') as json_file:
        json.dump(all_restaurants, json_file, indent=4)

if __name__ == "__main__":
    main()
