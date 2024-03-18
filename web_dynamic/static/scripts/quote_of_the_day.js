document.addEventListener('DOMContentLoaded', function () {
  fetch('http://localhost:5001/api/v1/daily_quote')
    .then(response => response.json())
    .then(data => {
      document.getElementById('quote-text').innerText = data.text;
      document.getElementById('quote-author').innerText = '- ' + data.author_name;
    })
    .catch(error => console.error('Failed to fetch the daily quote', error));
  updateCurrentDateTime();
});

function fetchAuthorName (authorId, callback) {
  fetch('http://localhost:5001/api/v1/authors/' + authorId)
    .then(response => response.json())
    .then(authorData => {
      console.log('Author Data:', authorData);
      callback(authorData.name);
    });
}

function fetchQuotesByAuthor (authorId, callback) {
  fetch('http://localhost:5001/api/v1/authors/' + authorId + '/quotes')
    .then(response => response.json())
    .then(quotesData => {
      callback(quotesData);
    });
}

function updateCurrentDateTime () {
  const currentDateElement = document.getElementById('current-date-time');

  function updateTime () {
    const now = new Date();
    const options = {
      weekday: 'long',
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: 'numeric',
      minute: 'numeric',
      timeZoneName: 'short'
    };
    const formattedDateTime = now.toLocaleString('en-US', options);
    currentDateElement.textContent = formattedDateTime;
  }

  updateTime();

  setInterval(updateTime, 1000);
}
