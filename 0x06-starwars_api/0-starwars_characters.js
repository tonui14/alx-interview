#!/usr/bin/node

const request = require('request');

// Retrieve the movie ID from command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie ID as an argument.');
  process.exit(1);
}

// Star Wars API URL for the specified film
const url = `https://swapi.dev/api/films/${movieId}/`;

// Fetch movie data
request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie. Status code: ${response.statusCode}`);
    return;
  }

  // Parse the response body
  const filmData = JSON.parse(body);

  // Fetch and print each character in the order given in the API
  const characterURLs = filmData.characters;

  const printCharacterNames = (urls, index = 0) => {
    if (index >= urls.length) return;

    request(urls[index], (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
        printCharacterNames(urls, index + 1);
      } else {
        console.error('Error fetching character data:', error);
      }
    });
  };

  printCharacterNames(characterURLs);
});

