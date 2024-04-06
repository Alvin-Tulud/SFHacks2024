// locationTest.js

$(document).ready(function() {
    const findMyState = () => {
        const status = $('.status');

    const success = (position) => {
        console.log(position);
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        
        initMap(latitude, longitude);
        sendLocation(latitude, longitude);
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

//thanks google
// Initialize and add the map
let map;

async function initMap(latitude, longitude) {
  // The location of Uluru
  const position = { lat: latitude, lng: longitude };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("userLocation"), {
    zoom: 4,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned at Uluru
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "Your Location",
  });
}