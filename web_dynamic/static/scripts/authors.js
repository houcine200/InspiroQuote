function fetchAuthors() {
    fetch('http://localhost:5001/api/v1/authors')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch authors');
            }
            return response.json();
        })
        .then(data => {
            const authorsDropdown = document.getElementById('authors-dropdown');
            authorsDropdown.innerHTML = ''; 

            const defaultOption = document.createElement('option');
            defaultOption.textContent = "Select an author";
            defaultOption.value = "";
            authorsDropdown.appendChild(defaultOption);

            data.forEach(author => {
                const option = document.createElement('option');
                option.value = author.id;
                option.textContent = author.name;
                authorsDropdown.appendChild(option);
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
            const citationsContainer = document.getElementById('citations-list');
            citationsContainer.innerHTML = '';

            data.forEach(citation => {
                const table = document.createElement('table');
                const row = table.insertRow();
                const cell = row.insertCell();
                cell.textContent = citation.text;
                citationsContainer.appendChild(table);
            });
        })
        .catch(error => {
            console.error('Error fetching citations for author:', error);
        });
}

document.getElementById('authors-dropdown').addEventListener('change', function() {
    const selectedAuthorId = this.value;
    if (selectedAuthorId) {
        fetchCitationsForAuthor(selectedAuthorId);
    } else {
        const citationsContainer = document.getElementById('citations-list');
        citationsContainer.innerHTML = '<p id="placeholder-text">Welcome to InspiroQuotes Categories! Explore the diverse range of topics and themes to discover profound insights, wisdom, and inspiration from renowned thinkers and leaders.</p>';
    }
});
