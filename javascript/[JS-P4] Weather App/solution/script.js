// ------ Selecting HTML Elements ------
// Grab references to the search box input and button
const searchBox = document.querySelector('.search input');  // Input where the user types the city name
const searchBtn = document.querySelector('.search button'); // Button to trigger the search

// Grab elements inside the weather card that will be updated dynamically
const weatherIcon = document.querySelector('.weather-icon'); // Image showing the weather condition
const cityElement = document.querySelector('.city');         // Displays the city name
const tempElement = document.querySelector('.temp');         // Displays the temperature
const humidityElement = document.querySelector('.humidity'); // Displays the humidity percentage
const windElement = document.querySelector('.wind');         // Displays the wind speed
const weatherDetails = document.querySelector('.weather-details'); // The container holding all weather info

// Initially hide the weather details card so it only appears after a search
weatherDetails.style.display = 'none';

// ------ Event Listeners ------
// When the search button is clicked, call getCoordinates with the city typed in the input
searchBtn.addEventListener('click', () => {
    getCoordinates(searchBox.value);
            setTimeout(() => {
            searchBox.value = '';  // Clears input after 600ms
        }, 600);
});

// When the "Enter" key is pressed while typing in the search box, also call getCoordinates
searchBox.addEventListener('keypress', (e) => {
     if (e.key === 'Enter') {
        getCoordinates(searchBox.value);
        setTimeout(() => {
            searchBox.value = '';  // Clears input after 600ms
        }, 600);
    }
});

// ------ Fetch Coordinates ------
// This function converts a city name into latitude and longitude
async function getCoordinates(city) {
    // Construct the API URL to get geographic coordinates for the city
    const geoUrl = `https://geocoding-api.open-meteo.com/v1/search?name=${city}&count=1`;

    try {
        const response = await fetch(geoUrl);  // Request location data from the geocoding API
        const data = await response.json();    // Convert the response to JSON

        // If no matching city is found, hide the weather card and alert the user
        if (!data.results || data.results.length === 0) {
            weatherDetails.style.display = 'none';
            alert("City not found!");
            return;
        }

        // Take the first matching city and pass its coordinates to get the weather
        const { latitude, longitude, name, country } = data.results[0];
        getWeather(latitude, longitude, name, country);

    } catch (error) {
        // If the fetch fails due to network or API issues, hide the card and show an alert
        weatherDetails.style.display = 'none';
        alert("Error fetching location!");
        console.error(error);
    }
}

// ------ Fetch Weather Data ------
// This function fetches the current weather for a specific latitude and longitude
async function getWeather(lat, lon, cityName, country) {
    // Construct the API URL to get current weather and hourly humidity
    const weatherUrl = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true&hourly=relativehumidity_2m`;

    try {
        const response = await fetch(weatherUrl);  // Request data from the weather API
        const data = await response.json();        // Convert the response to JSON

        // If no current weather data is returned, hide the weather card and alert the user
        if (!data.current_weather) {
            weatherDetails.style.display = 'none';
            alert("Weather data not available!");
            return;
        }

        // Extract humidity from hourly data by finding the current UTC hour
        const date = new Date();
        const currentHour = date.getUTCHours();
        const humidity = data.hourly.relativehumidity_2m[currentHour];

        // Pass the fetched data to the function that updates the weather card
        displayWeather(data.current_weather, cityName, country, humidity);

    } catch (error) {
        // If there’s an error fetching data, hide the card and log the error
        weatherDetails.style.display = 'none';
        alert("Error fetching weather!");
        console.error(error);
    }
}

// ------ Display Weather Update ------
// This function updates the weather card and changes the entire page background
function displayWeather(weather, city, country, humidity) {
    const { temperature, windspeed, weathercode } = weather;

    // Fill in text on the card
     cityElement.innerHTML = `${city}, ${country}`;
     tempElement.innerHTML = Math.round(temperature) + '°C';
     windElement.innerHTML = Math.round(windspeed) + ' km/h';
     humidityElement.innerHTML = humidity ? humidity + '%' : 'N/A';

    // Find the matching icon for the current weather code, or use the default if not found
     const weatherData = weatherCodeMap[weathercode] || weatherCodeMap[0];

    // Update the weather icon image on the card
     weatherIcon.src = weatherData.icon;

    // Change the entire page's background to match the current weather
     document.body.style.background = weatherData.bg;             // Apply the gradient from the weather code map
     document.body.style.backgroundAttachment = "fixed";          // Keep the background in place when scrolling
     document.body.style.backgroundSize = "cover";                // Make the background cover the entire page

    // Show the weather details card
     weatherDetails.style.display = 'block';
}

// ------ Weather Icon ------
// Map Open-Meteo's numeric weather codes to icons for the card
const weatherCodeMap = {
    0: { icon: '/img/egg-sunny-side-up-svgrepo-com.svg', bg: 'linear-gradient(to top, #fbc2eb, #a6c1ee)' }, // Clear
    1: { icon: '/img/egg-sunny-side-up-svgrepo-com.svg', bg: 'linear-gradient(to top, #fbc2eb, #a6c1ee)' },
    2: { icon: '/img/cloudy-forecast-svgrepo-com.svg', bg: 'linear-gradient(to top, #d7d2cc, #304352)' }, // Partly cloudy
    3: { icon: '/img/cloudy-forecast-svgrepo-com.svg', bg: 'linear-gradient(to top, #757f9a, #d7dde8)' }, // Cloudy
    45: { icon: '/img/mist-svgrepo-com.svg', bg: 'linear-gradient(to top, #3e5151, #decba4)' }, // Fog
    48: { icon: '/img/mist-svgrepo-com.svg', bg: 'linear-gradient(to top, #3e5151, #decba4)' },
    51: { icon: '/img/cloud-drizzle-svgrepo-com.svg', bg: 'linear-gradient(to top, #89f7fe, #66a6ff)' }, // Drizzle
    53: { icon: '/img/cloud-drizzle-svgrepo-com.svg', bg: 'linear-gradient(to top, #89f7fe, #66a6ff)' },
    55: { icon: '/img/cloud-drizzle-svgrepo-com.svg', bg: 'linear-gradient(to top, #89f7fe, #66a6ff)' },
    61: { icon: '/img/rain-svgrepo-com (2).svg', bg: 'linear-gradient(to top, #373b44, #4286f4)' }, // Rain
    63: { icon: '/img/rain-svgrepo-com (2).svg', bg: 'linear-gradient(to top, #373b44, #4286f4)' },
    65: { icon: '/img/rain-svgrepo-com (2).svg', bg: 'linear-gradient(to top, #373b44, #4286f4)' },
    71: { icon: '/img/snowing-forecast-svgrepo-com.svg', bg: 'linear-gradient(to top, #e6dada, #274046)' }, // Snow
    73: { icon: '/img/snowing-forecast-svgrepo-com.svg', bg: 'linear-gradient(to top, #e6dada, #274046)' },
    75: { icon: '/img/snowing-forecast-svgrepo-com.svg', bg: 'linear-gradient(to top, #e6dada, #274046)' },
    95: { icon: '/img/rain-svgrepo-com (2).svg', bg: 'linear-gradient(to top, #0f2027, #203a43, #2c5364)' }, // Thunderstorm
};