// Add an event listener to the login form to handle form submission
document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Create a FormData object from the form data
    const formData = new FormData(this);

    // Extract the email and password from the form data
    const loginData = {
        email: formData.get("email"),
        password: formData.get("password")
    };

    // Send a POST request to the "/welcome" endpoint with the login data
    fetch("/welcome", {
        method: "POST", // Use the POST method for the request
        headers: {
            "Content-Type": "application/json" // Set the content type header to JSON
        },
        body: JSON.stringify(loginData) // Convert the login data to JSON and send it as the request body
    })
    .then(response => {
        if (response.ok) { // Check if the response is OK (status code 200-299)
            // Redirect the user to the profile page with the encoded email in the URL
            window.location.href = "/profile/" + encodeURIComponent(loginData.email);
        } else {
            // Update the login message element with an error message
            document.getElementById("login-message").textContent = "Invalid email or password.";
        }
    })
    .catch(error => { // Handle any errors that occur during the fetch or data processing
        console.error("Error logging in:", error); // Log the error message to the console
        // Update the login message element with an error message
        document.getElementById("login-message").textContent = "An error occurred. Please try again later.";
    });
});
