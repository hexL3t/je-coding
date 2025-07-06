let is24HourFormat = false; // Default is 12-hour format

// Update World Clock for selected city with DST consideration
function updateWorldClock(timeZone, is24HourFormat) {
    const options = { 
        hour: '2-digit', 
        minute: '2-digit', 
        second: '2-digit',
        hour12: !is24HourFormat, 
        timeZone: timeZone 
    };
    
    const now = new Date().toLocaleTimeString('en-AU', options);

    // Set the time in the corresponding elements
    const timeParts = now.split(':');
    document.getElementById('selected-time').textContent = timeParts[0]; // Hours
    document.getElementById('selected-minutes').textContent = timeParts[1]; // Minutes
    document.getElementById('selected-seconds').textContent = timeParts[2].split(' ')[0]; // Seconds
    document.getElementById('selected-period').textContent = now.includes('AM') || now.includes('PM') ? now.split(' ')[1] : ''; // AM/PM (for 12-hour format)
}

// Update the date for the selected city with DST consideration
function updateDate(timeZone) {
    const today = new Date().toLocaleDateString('en-AU', { 
        timeZone: timeZone, 
        weekday: 'long', 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric' 
    });
    
    // Split the date and update each part
    const [dayName, dayNumber, monthName, year] = today.split(' ');
    document.getElementById('selected-day-name').textContent = dayName;
    document.getElementById('selected-day-number').textContent = dayNumber;
    document.getElementById('selected-month-name').textContent = monthName;
    document.getElementById('selected-year').textContent = year;
}

// Function to update the city, country, time, and date
function updateTimeAndDateForCity(selectedTimeZone) {
    const cityName = selectedTimeZone.split('/')[1]; // Extract the city name
    const country = selectedTimeZone.split('/')[0]; // Extract the country name
    
    // Display the city and country
    document.getElementById('selected-city').textContent = cityName + ', ' + country;
    
    // Update the time and date for the selected city
    updateWorldClock(selectedTimeZone, is24HourFormat); // This will update the time with the correct format
    updateDate(selectedTimeZone); // This will update the date
}

// Get the city selector element
const citySelector = document.querySelector('.city-selector');

// Event listener for city selection change
citySelector.addEventListener('change', (event) => {
    const selectedTimeZone = event.target.value;  // Get the selected timezone
    updateTimeAndDateForCity(selectedTimeZone);   // Update city, country, time, and date
});

// Initial clock update when page loads (for Brisbane as default)
const defaultTimeZone = 'Australia/Brisbane'; // Default timezone on page load
updateTimeAndDateForCity(defaultTimeZone);     // Set the default city and country on load

// Set interval to update the clock every second
setInterval(() => {
    const selectedTimeZone = citySelector.value || defaultTimeZone; // Get the current selected timezone or default if none selected
    updateWorldClock(selectedTimeZone, is24HourFormat); // Update the time for the selected city
}, 1000); // Update every second

// Format Switch
const formatSwitchBtn = document.querySelector('.format-switch-btn');
formatSwitchBtn.addEventListener('click', () => {
    formatSwitchBtn.classList.toggle("active");

    // Get current format value, toggle between '12' and '24'
    is24HourFormat = !is24HourFormat; // Toggle between 12 and 24-hour format

    // Update format in the button
    formatSwitchBtn.setAttribute('data-format', is24HourFormat ? '24' : '12');

    // Re-call the clock function to update the format
    const selectedTimeZone = citySelector.value || defaultTimeZone;
    updateWorldClock(selectedTimeZone, is24HourFormat); // Pass the updated format
});

// Dot Menu Toggle
const dotMenuBtn = document.querySelector('.dot-menu-btn');
const dotMenu = document.querySelector('.dot-menu');

dotMenuBtn.addEventListener('click', () => {
    dotMenu.classList.toggle('active');
});

document.addEventListener('click', (e) => {
    if (!dotMenu.contains(e.target) && !dotMenuBtn.contains(e.target)) {
        dotMenu.classList.remove('active');
    }
});
