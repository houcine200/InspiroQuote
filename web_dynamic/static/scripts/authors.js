function fetchAuthors() {
  fetch('http://localhost:5001/api/v1/authors')
      .then(response => {
          if (!response.ok) {
              throw new Error('Failed to fetch authors');
          }
          return response.json();
      })
      .then(data => {
          const authorsList = document.getElementById('authors-list');
          authorsList.innerHTML = ''; // Clear previous authors

          data.forEach(author => {
              const listItem = document.createElement('li');
              listItem.textContent = `${author.name}`;
              
              const viewCitationsButton = document.createElement('button');
              viewCitationsButton.textContent = 'View Citations';
              viewCitationsButton.addEventListener('click', () => fetchCitationsForAuthor(author.id));
              
              listItem.appendChild(viewCitationsButton);
              authorsList.appendChild(listItem);
          });
      })
      .catch(error => {
          console.error('Error fetching authors:', error);
      });
}

function fetchCitationsForAuthor(authorId) {
  fetch(`http://localhost:5001/api/v1/authors/${authorId}/citations`)
      .then(response => {
          if (!response.ok) {
              throw new Error('Failed to fetch citations for author');
          }
          return response.json();
      })
      .then(data => {
          const citationsList = document.getElementById('citations-list');
          citationsList.innerHTML = ''; // Clear previous citations

          data.forEach(citation => {
              const listItem = document.createElement('li');
              listItem.textContent = `${citation.text}`;
              citationsList.appendChild(listItem);
          });
      })
      .catch(error => {
          console.error('Error fetching citations for author:', error);
      });
}
