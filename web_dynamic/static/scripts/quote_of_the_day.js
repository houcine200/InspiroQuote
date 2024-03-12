document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:5001/api/v1/daily_quote') // Make sure the endpoint is correct
        .then(response => response.json())
        .then(data => {
            document.getElementById('quote-text').innerText = data.text;
            document.getElementById('quote-author').innerText = '- ' + data.author_name; // Adjust if the key is different
        })
        .catch(error => console.error('Failed to fetch the daily quote', error));
    updateCurrentDateTime();
});


function fetchAuthorName(authorId, callback) {
    fetch('http://localhost:5001/api/v1/authors/' + authorId)
        .then(response => response.json())
        .then(authorData => {
            console.log("Author Data:", authorData); // Debugging line
            callback(authorData.name); // Pass the author's name to the callback
        });
}


function fetchQuotesByAuthor(authorId, callback) {
    fetch('http://localhost:5001/api/v1/authors/' + authorId + '/quotes')
        .then(response => response.json())
        .then(quotesData => {
            callback(quotesData); // Pass the quotes data to the callback
        });
}





function updateCurrentDateTime() {
    const currentDateElement = document.getElementById('current-date-time');

    // Function to update current date and time every second
    function updateTime() {
        const now = new Date();
        const options = {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric',
            hour: 'numeric',
            minute: 'numeric',
            timeZoneName: 'short'
        };
        const formattedDateTime = now.toLocaleString('en-US', options);
        currentDateElement.textContent = formattedDateTime;
    }

    // Initial call to display current date and time
    updateTime();

    // Update current date and time every second
    setInterval(updateTime, 1000);
}