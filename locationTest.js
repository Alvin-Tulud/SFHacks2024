// locationTest.js

$(document).ready(function() {
    const findMyState = () => {
        const status = $('.status');

    const success = (position) => {
        console.log(position);
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        
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