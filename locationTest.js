// Used to test getting location from user
// Will be deleted in future - robert

const findMyState = () => {
    const status = document.querySelector('.status');

    const success = (position) => {
        console.log(position);
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        document.getElementById("map").src = "https://maps.google.com/maps?center=" + latitude + "," + longitude + "&output=embed";

        sendLocation();
    }

    const error = () => {
        status.textContent = 'Unable to retrieve location';
    }

    navigator.geolocation.getCurrentPosition(success, error);

}

function sendLocation() {
    $.ajax({ 
        url: '/getLocation', 
        type: 'POST', 
        data: { 'latitude': latitude, 'longitude': longitude}, 
        error: function(error) { 
            console.log(error); 
        } 
    }); 
} 

document.querySelector('.find-state').addEventListener('click', findMyState)