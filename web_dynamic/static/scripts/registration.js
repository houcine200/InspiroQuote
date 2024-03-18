// Add an event listener to wait for the DOMContentLoaded event, which fires when the HTML content of the page has been fully loaded and parsed
document.addEventListener("DOMContentLoaded", function() {
    const registrationForm = document.getElementById("registration-form"); // Get the registration form element
    const registrationMessage = document.getElementById("registration-message"); // Get the registration message element

    // Add a submit event listener to the registration form
    registrationForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent the default form submission behavior

        // Create a FormData object from the form data
        const formData = new FormData(registrationForm);

        // Extract user data (email, password, first_name, last_name) from the form data
        const userData = {
            email: formData.get("email"),
            password: formData.get("password"),
            first_name: formData.get("first_name"),
            last_name: formData.get("last_name")
        };

        // Send a POST request to the "/api/v1/users" endpoint with the user data
        fetch("http://localhost:5001/api/v1/users", {
            method: "POST", // Use the POST method for the request
            headers: {
                "Content-Type": "application/json" // Set the content type header to JSON
            },
            body: JSON.stringify(userData) // Convert the user data to JSON and send it as the request body
        })
        .then(response => {
            if (response.ok) { // Check if the response is OK (status code 200-299)
                registrationMessage.textContent = "Registration successful!"; // Update the registration message with a success message
                registrationForm.reset(); // Reset the form fields
            } else {
                registrationMessage.textContent = "Registration failed. Please try again."; // Update the registration message with an error message
            }
        })
        .catch(error => {
            console.error("Error registering user:", error); // Log the error message to the console
            registrationMessage.textContent = "An error occurred. Please try again later."; // Update the registration message with an error message
        });
    });
});
