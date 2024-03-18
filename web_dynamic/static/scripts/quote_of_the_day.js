// Add an event listener to wait for the DOMContentLoaded event, which fires when the HTML content of the page has been fully loaded and parsed
document.addEventListener('DOMContentLoaded', function() {
    // Fetch the daily quote data from the specified API endpoint
    fetch('http://localhost:5001/api/v1/daily_quote')
        .then(response => response.json()) // Parse the response body as JSON
        .then(data => {
            // Update the quote text and author elements with the fetched data
            document.getElementById('quote-text').innerText = data.text; // Set the text content of the quote text element
            document.getElementById('quote-author').innerText = '- ' + data.author_name; // Set the text content of the quote author element
        })
        .catch(error => console.error('Failed to fetch the daily quote', error)); // Handle any errors that occur during the fetch
    updateCurrentDateTime(); // Call the updateCurrentDateTime function to update the current date and time on the page
});


// Function to fetch the name of an author based on the author ID and execute a callback function with the author's name
function fetchAuthorName(authorId, callback) {
    // Fetch data about the author from the specified API endpoint using the provided author ID
    fetch('http://localhost:5001/api/v1/authors/' + authorId)
        .then(response => response.json()) // Parse the response body as JSON
        .then(authorData => {
            console.log("Author Data:", authorData); // Log the author data to the console for debugging purposes
            callback(authorData.name); // Execute the provided callback function with the author's name as an argument
        });
}

// Function to fetch quotes by a specific author based on the author ID and execute a callback function with the quotes data
function fetchQuotesByAuthor(authorId, callback) {
    // Fetch quotes data for the specified author ID from the API endpoint
    fetch('http://localhost:5001/api/v1/authors/' + authorId + '/quotes')
        .then(response => response.json()) // Parse the response body as JSON
        .then(quotesData => {
            callback(quotesData); // Execute the provided callback function with the quotes data as an argument
        });
}

// Function to update the current date and time on the page in real-time
function updateCurrentDateTime() {
    const currentDateElement = document.getElementById('current-date-time'); // Get the element where the current date and time will be displayed

    // Function to update the time
    function updateTime() {
        const now = new Date(); // Create a new Date object representing the current date and time
        const options = {
            weekday: 'long', // Display the full weekday name (e.g., Monday)
            year: 'numeric', // Display the year in numeric format (e.g., 2023)
            month: 'long', // Display the full month name (e.g., January)
            day: 'numeric', // Display the day of the month (e.g., 15)
            hour: 'numeric', // Display the hour (e.g., 13 for 1 PM)
            minute: 'numeric', // Display the minute (e.g., 30)
            timeZoneName: 'short' // Display the short name of the time zone (e.g., EST)
        };
        const formattedDateTime = now.toLocaleString('en-US', options); // Format the date and time according to the specified options
        currentDateElement.textContent = formattedDateTime; // Update the text content of the element with the formatted date and time
    }

    updateTime(); // Call updateTime function initially to set the current date and time

    // Set up a timer to call updateTime function every second (1000 milliseconds) to keep the date and time updated in real-time
    setInterval(updateTime, 1000);
}