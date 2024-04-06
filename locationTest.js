// locationTest.js

import { Loader } from '@googlemaps/js-api-loader';

// const apiOptions = {
//     apiKey: "AIzaSyB6lBBQu2yrWdLZ4qOgWtIx7iCMtRcAeeM"
// }

/*
const loader = new Loader(apiOptions);

loader.load().then(() => {
    console.log('Maps JS API Loaded');
});

function displayMap(latitude, longitude) {
    
    const mapOptions = {
      center: { lat: latitude, lng: longitude },
      zoom: 14
    };
    const mapDiv = document.getElementById('userLocation');
    const map = new google.maps.Map(mapDiv, mapOptions);
    return map;
  }
*/



    $(document).ready(function() {
        const findMyState = () => {
            const status = $('.status');

            const success = (position) => {
                console.log(position);
                sendLocation(position.coords.latitude, position.coords.longitude);
            }

            const error = () => {
                status.text('Unable to retrieve location');
            }

            navigator.geolocation.getCurrentPosition(success, error);
        }

        function sendLocation(latitude, longitude) {
            $.ajax({ 
                url: '/getLocation', 
                type: 'POST', 
                data: { 'latitude': latitude, 'longitude': longitude}, 
                error: function(error) { 
                    console.log(error); 
                } 
            }); 
        } 

        $('.find-state').click(findMyState);
    });