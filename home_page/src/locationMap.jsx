import React from 'react';
import {createRoot} from 'react-dom/client';
import {APIProvider, Map} from '@vis.gl/react-google-maps';
import './index.css';

$(document).ready(function() {
    const findMyState = () => {
        const status = $('.status');

            const success = (position) => {
                console.log(position);
                console.log(position.data);
                document.getElementById("mapContainer").setAttribute("src",
                "https://www.google.com/maps/embed/v1/view?key=AIzaSyB6lBBQu2yrWdLZ4qOgWtIx7iCMtRcAeeM" + 
                "&center=" + position.coords.latitude + "," + position.coords.longitude +
                "&zoom=16");
                sendLocation(position.coords.latitude, position.coords.longitude);
            }

            const error = () => {
                status.text('Unable to retrieve location');
            }
            navigator.geolocation.getCurrentPosition(success, error);
        }

    function sendLocation(latitude, longitude) {
        $.ajax({ 
            url: '/', 
            type: 'POST', 
            data: { 'latitude': latitude, 'longitude': longitude}, 
            error: function(error) { 
                console.log(error); 
            } 
        }); 
    } 

    $('.find-state').click(findMyState);
});