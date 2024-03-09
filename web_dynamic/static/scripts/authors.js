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

function fetchQuotesForAuthor(authorId) {
    fetch(`http://localhost:5001/api/v1/authors/${authorId}/quotes`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch quotes for author');
            }
            return response.json();
        })
        .then(quotes => {
            const quotesContainer = document.getElementById('citations-list');
            quotesContainer.innerHTML = '';

            quotes.forEach(quote => {
                const quoteCard = document.createElement('div');
                quoteCard.classList.add('quote-card');

                const quoteText = document.createElement('p');
                quoteText.classList.add('quote-text');
                quoteText.textContent = `"${quote.text}"`;

                quotesContainer.appendChild(quoteCard);
                quoteCard.appendChild(quoteText);
            });

            if (quotes.length === 0) {
                quotesContainer.innerHTML = '<p>No quotes found for this author.</p>';
            }
        })
        .catch(error => {
            console.error('Error fetching quotes for author:', error);
        });
}

document.getElementById('authors-dropdown').addEventListener('change', function() {
    const selectedAuthorId = this.value;
    if (selectedAuthorId) {
        fetchQuotesForAuthor(selectedAuthorId);
    } else {
        const quotesContainer = document.getElementById('citations-list');
        quotesContainer.innerHTML = `
            <p id="placeholder-text-1">"Journey through the Echoes of Wisdom"</p>
            <p id="placeholder-text-2">Welcome to a world where every citation is a gateway to wisdom, a spark of inspiration, and a reflection of the human experience. As you explore the timeless words of remarkable authors, let their insights illuminate your path and enrich your understanding of life's profound mysteries.</p>
            <p id="placeholder-text-3">Prepare to embark on an odyssey through the echoes of wisdom, where each quote is a beacon of light guiding you towards deeper understanding and personal growth. Embrace the journey, for within these citations lie the seeds of transformation, waiting to blossom in the garden of your mind.</p>
        `;
    }
});
