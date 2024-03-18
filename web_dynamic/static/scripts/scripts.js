// Add an event listener to wait for the DOMContentLoaded event, which fires when the HTML content of the page has been fully loaded and parsed
document.addEventListener("DOMContentLoaded", function() {
    // Fetch user data from the specified API endpoint
    fetch("http://localhost:5001/api/v1/users")
        .then(response => response.json()) // Parse the response body as JSON
        .then(users => { // Handle the parsed JSON data (list of users)
            const userList = document.getElementById("user-list"); // Get the element where the user list will be displayed

            // Loop through each user in the list of users
            users.forEach(user => {
                const userElement = document.createElement("div"); // Create a new div element for each user
                // Set the text content of the user element to display user information (name and email)
                userElement.textContent = `Name: ${user.first_name} ${user.last_name}, Email: ${user.email}`;
                userList.appendChild(userElement); // Append the user element to the user list
            });
        })
        .catch(error => console.error("Error fetching users:", error)); // Handle any errors that occur during the fetch
});
