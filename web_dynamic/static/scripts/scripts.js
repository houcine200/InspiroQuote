// scripts.js
document.addEventListener("DOMContentLoaded", function() {
  fetch("http://localhost:5001/api/v1/users")
      .then(response => response.json())
      .then(users => {
          const userList = document.getElementById("user-list");
          users.forEach(user => {
              const userElement = document.createElement("div");
              userElement.textContent = `Name: ${user.first_name} ${user.last_name}, Email: ${user.email}`;
              userList.appendChild(userElement);
          });
      })
      .catch(error => console.error("Error fetching users:", error));
});
