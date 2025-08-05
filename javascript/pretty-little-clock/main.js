// Default to 12-hour format
let is24HourFormat = false;

// Update the time for a given timezone
function updateWorldClock(timeZone, is24HourFormat) {
   const options = { 
      hour: '2-digit', 
      minute: '2-digit', 
      second: '2-digit',
      // Toggle between 12-hour and 24-hour format
      hour12: !is24HourFormat,
      // Set the timezone to use
      timeZone: timeZone
   };

   // Format time based on options
   const now = new Date().toLocaleTimeString(is24HourFormat ? 
    'en-AU' : 'en-US', options);
   // Split the time into parts (hours, minutes, seconds)
   const timeParts = now.split(':');

   // Set hours, minutes, seconds
   document.getElementById('selected-time').textContent = timeParts[0];                        
   document.getElementById('selected-minutes').textContent = timeParts[1];                    
   document.getElementById('selected-seconds').textContent 
        = timeParts[2].split(' ')[0];
   document.getElementById('selected-period').textContent 
        = now.includes('AM') || now.includes('PM') 
        ? now.split(' ')[1]     // Set AM/PM for 12-hour format
        : '';                   // Clear if using 24-hour format
}

// Update the date for a given timezone
function updateDate(timeZone) {
   const today = new Date().toLocaleDateString('en-AU', { 
      timeZone: timeZone, 
      weekday: 'long', 
      year: 'numeric', 
      month: 'short', 
      day: 'numeric' 
   });

   // Example format: "Monday 7 Jul 2025"
   const [dayName, dayNumber, monthName, year] = today.split(' ');

   // Update individual date fields
   document.getElementById('selected-day-name').textContent = dayName;
   document.getElementById('selected-day-number').textContent = dayNumber;
   document.getElementById('selected-month-name').textContent = monthName;
   document.getElementById('selected-year').textContent = year;
}

// Update both time and date based on selected city
function updateTimeAndDateForCity(selectedTimeZone) {
   // Extract the city name from timezone
   const cityName = selectedTimeZone.split('/')[1];
   // Extract the country/region
   const country = selectedTimeZone.split('/')[0];

   // Display the selected city and country
   document.getElementById('selected-city').textContent 
     = cityName + ', ' + country;

   // Update both time and date
   updateWorldClock(selectedTimeZone, is24HourFormat);
   updateDate(selectedTimeZone);
}

// City Selector Event Handling
const citySelector = document.querySelector('.city-selector');

// When the user selects a new city, update the clock and date
citySelector.addEventListener('change', (event) => {
   // Get selected timezone from dropdown
   const selectedTimeZone = event.target.value;
   // Update UI
   updateTimeAndDateForCity(selectedTimeZone);
});

// Set Default Timezone on Page Load
// Default city on initial load
const defaultTimeZone = 'Australia/Brisbane';
// Display default time and date
updateTimeAndDateForCity(defaultTimeZone);

// Continuously Update Clock Every Second
setInterval(() => {
   // Use selected city or fallback to default
   const selectedTimeZone = citySelector.value || defaultTimeZone;
   // Refresh time display
   updateWorldClock(selectedTimeZone, is24HourFormat);
}, 1000); // Run every 1000 milliseconds (1 second)

// Format Toggle Button (12/24-Hour)
const formatSwitchBtn = document.querySelector('.format-switch-btn');

formatSwitchBtn.addEventListener('click', () => {
   // Add or remove 'active' class (for style change)
   formatSwitchBtn.classList.toggle("active");
   // Switch between true (24h) and false (12h)
   is24HourFormat = !is24HourFormat;

   // Update the button’s data-format attribute for accessibility/debugging
   formatSwitchBtn.setAttribute('data-format', is24HourFormat ? '24' 
      : '12');

   // Re-render the time display with the new format
   const selectedTimeZone = citySelector.value || defaultTimeZone;
   updateWorldClock(selectedTimeZone, is24HourFormat);
});

// Dot Menu (⋮) Toggle Handling
const dotMenuBtn = document.querySelector('.dot-menu-btn');
const dotMenu = document.querySelector('.dot-menu');

// Show/hide the menu when the dot button is clicked
dotMenuBtn.addEventListener('click', () => {
   dotMenu.classList.toggle('active');
});

// Hide the menu when clicking outside of it
document.addEventListener('click', (e) => {
   if (!dotMenu.contains(e.target) && !dotMenuBtn.contains(e.target)) {
      dotMenu.classList.remove('active');
   }
});