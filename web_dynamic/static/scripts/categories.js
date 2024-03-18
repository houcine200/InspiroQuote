// Add an event listener to wait for the DOMContentLoaded event, which fires when the HTML content of the page has been fully loaded and parsed
document.addEventListener('DOMContentLoaded', () => {
    fetchCategories(); // Call the fetchCategories function to fetch and populate categories on the page
    // Add a click event listener to the button with the ID 'search-button' to listen for clicks
    document.getElementById('search-button').addEventListener('click', searchQuotes);
});

// Function to fetch categories from an API endpoint and populate a select dropdown
function fetchCategories() {
    fetch('http://localhost:5001/api/v1/categories') // Fetch data from the specified API endpoint
        .then(response => { // Handle the response from the fetch request
            if (!response.ok) { // Check if the response is not OK (HTTP status code outside 200-299 range)
                throw new Error('Failed to fetch categories'); // Throw an error if fetching categories fails
            }
            return response.json(); // Parse the response body as JSON and return a promise with the JSON data
        })
        .then(data => { // Handle the parsed JSON data
            const categorySelect = document.getElementById('category-select'); // Get the select dropdown element for categories

            // Sort categories alphabetically by name
            data.sort((a, b) => a.name.localeCompare(b.name));

            // Loop through each category in the sorted data
            data.forEach(category => {
                const option = document.createElement('option'); // Create a new option element for each category
                option.value = category.id; // Set the value of the option to the category's ID
                option.textContent = category.name; // Set the text content of the option to the category's name
                categorySelect.appendChild(option); // Append the option to the select dropdown for categories
            });
        })
        .catch(error => { // Handle any errors that occur during the fetch or data processing
            console.error('Error fetching categories:', error); // Log the error message to the console
        });
}

// Function to search for quotes based on the selected category
function searchQuotes() {
    const categoryId = document.getElementById('category-select').value; // Get the selected category ID from the dropdown
    let url; // Declare a variable to hold the API endpoint URL

    if (categoryId) { // Check if a category ID is selected
        url = `http://localhost:5001/api/v1/categories/${categoryId}/quotes`; // Construct the URL to fetch quotes for the selected category
    } else { // If no category is selected
        document.getElementById('quotes-list').innerHTML = ''; // Clear the quotes list
        alert('Please select a category to search for quotes.'); // Show an alert asking the user to select a category
        return; // Exit the function early
    }

    fetch(url) // Fetch quotes from the constructed URL
        .then(response => { // Handle the response from the fetch request
            if (!response.ok) { // Check if the response is not OK (HTTP status code outside 200-299 range)
                throw new Error('Failed to fetch quotes'); // Throw an error if fetching quotes fails
            }
            return response.json(); // Parse the response body as JSON and return a promise with the JSON data
        })
        .then(data => { // Handle the parsed JSON data containing quotes
            const quotesList = document.getElementById('quotes-list'); // Get the quotes list element
            quotesList.innerHTML = ''; // Clear the existing content of the quotes list

            // Loop through each quote in the quotes data
            data.forEach(quote => {
                const listItem = document.createElement('li'); // Create a new list item for each quote
                const quoteText = document.createElement('div'); // Create a div for the quote text
                const authorName = document.createElement('div'); // Create a div for the author name
            
                quoteText.textContent = `"${quote.text}"`; // Set the text content of the quote text div
                authorName.textContent = `- ${quote.author_name}`; // Set the text content of the author name div
            
                quoteText.classList.add('quote-text'); // Add a CSS class to the quote text div
                authorName.classList.add('quote-author'); // Add a CSS class to the author name div
            
                listItem.appendChild(quoteText); // Append the quote text div to the list item
                listItem.appendChild(authorName); // Append the author name div to the list item
            
                quotesList.appendChild(listItem); // Append the list item to the quotes list
            });
        })
        .catch(error => { // Handle any errors that occur during the fetch or data processing
            console.error('Error fetching quotes:', error); // Log the error message to the console
        });
}