// registration.js
document.addEventListener("DOMContentLoaded", function() {
  const registrationForm = document.getElementById("registration-form");
  const registrationMessage = document.getElementById("registration-message");

  registrationForm.addEventListener("submit", function(event) {
      event.preventDefault();

      const formData = new FormData(registrationForm);
      const userData = {
          email: formData.get("email"),
          password: formData.get("password"),
          first_name: formData.get("first_name"),
          last_name: formData.get("last_name")
      };

      fetch("http://localhost:5001/api/v1/users", {
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: JSON.stringify(userData)
      })
      .then(response => {
          if (response.ok) {
              registrationMessage.textContent = "Registration successful!";
              registrationForm.reset();
          } else {
              registrationMessage.textContent = "Registration failed. Please try again.";
          }
      })
      .catch(error => {
          console.error("Error registering user:", error);
          registrationMessage.textContent = "An error occurred. Please try again later.";
      });
  });
});
