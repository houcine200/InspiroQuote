// Function to fetch authors from an API endpoint and populate a dropdown list
function fetchAuthors() {
    fetch('http://localhost:5001/api/v1/authors') // Fetch data from the specified API endpoint
        .then(response => { // Handle the response from the fetch request
            if (!response.ok) { // Check if the response is not OK (HTTP status code outside 200-299 range)
                throw new Error('Failed to fetch authors'); // Throw an error if fetching authors fails
            }
            return response.json(); // Parse the response body as JSON and return a promise with the JSON data
        })
        .then(data => { // Handle the parsed JSON data
            const authorsDropdown = document.getElementById('authors-dropdown'); // Get the authors dropdown element
            authorsDropdown.innerHTML = ''; // Clear the existing content of the authors dropdown

            const defaultOption = document.createElement('option'); // Create a new option element
            defaultOption.textContent = "Select an author"; // Set the text content of the default option
            defaultOption.value = ""; // Set the value of the default option
            authorsDropdown.appendChild(defaultOption); // Append the default option to the authors dropdown

            data.sort((a, b) => a.name.localeCompare(b.name)); // Sort the authors alphabetically by name

            data.forEach(author => { // Loop through each author in the sorted data
                const option = document.createElement('option'); // Create a new option element for each author
                option.value = author.id; // Set the value of the option to the author's ID
                option.textContent = author.name; // Set the text content of the option to the author's name
                authorsDropdown.appendChild(option); // Append the option to the authors dropdown
            });
        })
        .catch(error => { // Handle any errors that occur during the fetch or data processing
            console.error('Error fetching authors:', error); // Log the error message to the console
        });
}


// Function to fetch quotes for a specific author ID from an API endpoint and display them
function fetchQuotesForAuthor(authorId) {
    fetch(`http://localhost:5001/api/v1/authors/${authorId}/quotes`) // Fetch quotes for the specified author ID
        .then(response => { // Handle the response from the fetch request
            if (!response.ok) { // Check if the response is not OK (HTTP status code outside 200-299 range)
                throw new Error('Failed to fetch quotes for author'); // Throw an error if fetching quotes fails
            }
            return response.json(); // Parse the response body as JSON and return a promise with the JSON data
        })
        .then(quotes => { // Handle the parsed JSON data containing quotes
            const quotesContainer = document.getElementById('citations-list'); // Get the quotes container element
            quotesContainer.innerHTML = ''; // Clear the existing content of the quotes container

            quotes.forEach(quote => { // Loop through each quote in the quotes data
                const quoteCard = document.createElement('div'); // Create a new div for each quote (quote card)
                quoteCard.classList.add('quote-card'); // Add a CSS class to the quote card

                const quoteText = document.createElement('p'); // Create a new paragraph element for the quote text
                quoteText.classList.add('quote-text'); // Add a CSS class to the quote text paragraph
                quoteText.textContent = `"${quote.text}"`; // Set the text content of the quote text paragraph

                quotesContainer.appendChild(quoteCard); // Append the quote card to the quotes container
                quoteCard.appendChild(quoteText); // Append the quote text to the quote card
            });

            if (quotes.length === 0) { // Check if no quotes were found for the author
                quotesContainer.innerHTML = '<p>No quotes found for this author.</p>'; // Display a message in the quotes container
            }
        })
        .catch(error => { // Handle any errors that occur during the fetch or data processing
            console.error('Error fetching quotes for author:', error); // Log the error message to the console
        });
}

// Event listener for changes in the authors dropdown
document.getElementById('authors-dropdown').addEventListener('change', function() {
    const selectedAuthorId = this.value; // Get the selected author ID from the dropdown
    if (selectedAuthorId) { // Check if a valid author ID is selected
        fetchQuotesForAuthor(selectedAuthorId); // Fetch quotes for the selected author ID
    } else { // If no author is selected (default option)
        const quotesContainer = document.getElementById('citations-list'); // Get the quotes container element
        // Display placeholder text in the quotes container
        quotesContainer.innerHTML = `
            <p id="placeholder-text-1">"Journey through the Echoes of Wisdom"</p>
            <p id="placeholder-text-2">Welcome to a world where every citation is a gateway to wisdom, a spark of inspiration, and a reflection of the human experience. As you explore the timeless words of remarkable authors, let their insights illuminate your path and enrich your understanding of life's profound mysteries.</p>
            <p id="placeholder-text-3">Prepare to embark on an odyssey through the echoes of wisdom, where each quote is a beacon of light guiding you towards deeper understanding and personal growth. Embrace the journey, for within these citations lie the seeds of transformation, waiting to blossom in the garden of your mind.</p>
        `;
    }
});