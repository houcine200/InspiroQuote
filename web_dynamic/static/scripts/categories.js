document.addEventListener('DOMContentLoaded', () => {
    fetchCategories();
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
            
            // Automatically trigger search when categories are fetched
            searchQuotes();
        })
        .catch(error => {
            console.error('Error fetching categories:', error);
        });
}

function searchQuotes() {
    const categoryId = document.getElementById('category-select').value;
    let url;

    if (categoryId) {
        url = `http://localhost:5001/api/v1/categories/${categoryId}/quotes`;
    } else {
        url = 'http://localhost:5001/api/v1/quotes';
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
            
                quoteText.textContent = `${quote.text}`;
                authorName.textContent = `${quote.author}`;
            
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
