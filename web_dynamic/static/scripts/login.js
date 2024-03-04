document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    const loginData = {
        email: formData.get("email"),
        password: formData.get("password")
    };
    
    fetch("/welcome", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(loginData)
    })
    .then(response => {
        if (response.ok) {
            window.location.href = "/profile/" + encodeURIComponent(loginData.email); // Encode email to handle special characters
        } else {
            document.getElementById("login-message").textContent = "Invalid email or password.";
        }
    })
    .catch(error => {
        console.error("Error logging in:", error);
        document.getElementById("login-message").textContent = "An error occurred. Please try again later.";
    });
  });
  