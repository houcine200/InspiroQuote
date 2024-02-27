import React, { useState } from 'react';

function App() {
  const [categories, setCategories] = useState([]);
  const [quotes, setQuotes] = useState([]);

  const fetchCategories = () => {
    fetch('http://localhost:5001/api/v1/categories')
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch categories');
        }
        return response.json();
      })
      .then(data => {
        setCategories(data);
      })
      .catch(error => {
        console.error('Error fetching categories:', error);
      });
  };

  const fetchQuotesForCategory = (categoryId) => {
    fetch(`http://localhost:5001/api/v1/categories/${categoryId}/quotes`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to fetch quotes for category');
        }
        return response.json();
      })
      .then(data => {
        setQuotes(data);
      })
      .catch(error => {
        console.error('Error fetching quotes for category:', error);
      });
  };

  return (
    <div>
      <h1>Categories</h1>
      <button onClick={fetchCategories}>Fetch Categories</button>
      <ul>
        {categories.map(category => (
          <li key={category.id}>
            {category.name}{' '}
            <button onClick={() => fetchQuotesForCategory(category.id)}>View Quotes</button>
          </li>
        ))}
      </ul>
      <h2>Quotes</h2>
      <ul>
        {quotes.map(quote => (
          <li key={quote.id}>{quote.text} - {quote.author}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
