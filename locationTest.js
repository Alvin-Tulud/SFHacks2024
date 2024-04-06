// locationTest.js

    $(document).ready(function() {
        const findMyState = () => {
            const status = $('.status');

            const success = (position) => {
                console.log(position);
                document.getElementById("mapContainer").setAttribute("src",
                "https://www.google.com/maps/embed/v1/view?key=AIzaSyB6lBBQu2yrWdLZ4qOgWtIx7iCMtRcAeeM" + 
                "&center=" + position.coords.latitude + "," + position.coords.longitude +
                "&zoom=19");
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