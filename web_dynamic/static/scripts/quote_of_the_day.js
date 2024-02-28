document.addEventListener('DOMContentLoaded', function() {
  // Make an AJAX request to fetch the daily quote
  var xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://localhost:5001/api/v1/daily_quote', true);
  xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
          if (xhr.status === 200) {
              // Parse the JSON response
              var quoteData = JSON.parse(xhr.responseText);
              
              // Update the HTML content with the retrieved quote
              document.getElementById('quote-text').innerText = quoteData.text;
              document.getElementById('quote-author').innerText = '- ' + quoteData.author;
          } else {
              console.error('Failed to fetch the daily quote');
          }
      }
  };
  xhr.send();
});
