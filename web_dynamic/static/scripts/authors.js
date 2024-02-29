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
            citationsContainer.innerHTML = ''; // Clear previous citations

            data.forEach(citation => {
                // Create a table for each citation
                const table = document.createElement('table');
                table.style.width = '100%'; // Set the table width
                table.style.marginBottom = '20px'; // Space between tables
                table.style.borderCollapse = 'collapse'; // Optional: for styling
                
                // Create a row for the citation text
                const row = table.insertRow();
                const cell = row.insertCell();
                cell.textContent = citation.text; // Assuming citation object has a 'text' property
                cell.style.padding = '10px'; // Optional: for styling
                cell.style.border = '1px solid #ddd'; // Optional: for styling

                // Append the table to the container
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
        document.getElementById('citations-list').innerHTML = '';
    }
});

