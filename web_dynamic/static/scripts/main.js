function fetchCategories() {
    fetch('http://localhost:5001/api/v1/categories')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch categories');
            }
            return response.json();
        })
        .then(data => {
            const categoriesList = document.getElementById('categories-list');
            categoriesList.innerHTML = ''; // Clear previous categories

            data.forEach(category => {
                const listItem = document.createElement('li');
                listItem.textContent = `${category.name}`;
                
                const viewQuotesButton = document.createElement('button');
                viewQuotesButton.textContent = 'View Quotes';
                viewQuotesButton.addEventListener('click', () => fetchQuotesForCategory(category.id));
                
                listItem.appendChild(viewQuotesButton);
                categoriesList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error fetching categories:', error);
        });
}

function fetchQuotesForCategory(categoryId) {
    fetch(`http://localhost:5001/api/v1/categories/${categoryId}/quotes`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch quotes for category');
            }
            return response.json();
        })
        .then(data => {
            const quotesList = document.getElementById('quotes-list');
            quotesList.innerHTML = ''; // Clear previous quotes

            data.forEach(quote => {
                const listItem = document.createElement('li');
                listItem.textContent = `${quote.text} - ${quote.author}`;
                quotesList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error fetching quotes for category:', error);
        });
}
