document.addEventListener('DOMContentLoaded', () => {
    fetchCategories();
    // Bind the searchQuotes function to the search button's click event
    document.getElementById('search-button').addEventListener('click', searchQuotes);
});

function fetchCategories() {
    fetch('http://localhost:5001/api/v1/categories')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch categories');
            }
            return response.json();
        })
        .then(data => {
            const categorySelect = document.getElementById('category-select');

            data.forEach(category => {
                const option = document.createElement('option');
                option.value = category.id;
                option.textContent = category.name;
                categorySelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching categories:', error);
        });
}

function searchQuotes() {
    const categoryId = document.getElementById('category-select').value;
    let url;

    // Ensure the function fetches and displays quotes only when a valid category is selected
    if (categoryId) {
        url = `http://localhost:5001/api/v1/categories/${categoryId}/quotes`;
    } else {
        // If no category is selected, clear the quotes list and alert the user
        document.getElementById('quotes-list').innerHTML = '';
        alert('Please select a category to search for quotes.');
        return; // Exit the function early
    }

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch quotes');
            }
            return response.json();
        })
        .then(data => {
            const quotesList = document.getElementById('quotes-list');
            quotesList.innerHTML = ''; // Clear previous quotes

            data.forEach(quote => {
                const listItem = document.createElement('li');
                const quoteText = document.createElement('div');
                const authorName = document.createElement('div');
            
                quoteText.textContent = `"${quote.text}"`;
                // Adjust according to your actual API response structure
                authorName.textContent = `- ${quote.author_name}`;
            
                quoteText.classList.add('quote-text');
                authorName.classList.add('quote-author');
            
                listItem.appendChild(quoteText);
                listItem.appendChild(authorName);
            
                quotesList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error fetching quotes:', error);
        });
}
