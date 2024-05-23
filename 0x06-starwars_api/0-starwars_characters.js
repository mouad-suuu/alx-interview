#!/usr/bin/env node

const request = require("request");

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// URL for the Star Wars API
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error("Error:", error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error("Failed to retrieve data:", response.statusCode);
    return;
  }

  // Parse the JSON response
  const filmData = JSON.parse(body);

  // Get the list of characters
  const characters = filmData.characters;

  // Fetch each character's details and print their names
  characters.forEach((characterUrl) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.error("Error:", error);
        return;
      }
      if (response.statusCode !== 200) {
        console.error("Failed to retrieve data:", response.statusCode);
        return;
      }

      // Parse the JSON response
      const characterData = JSON.parse(body);

      // Print the character's name
      console.log(characterData.name);
    });
  });
});
