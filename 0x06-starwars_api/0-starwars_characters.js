#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const movieId = process.argv[2];
  const filmUrl = `${API_URL}/films/${movieId}/`;

  // Request movie data
  request(filmUrl, (err, res, body) => {
    if (err) {
      console.error('Error:', err);
      return;
    }
    if (res.statusCode !== 200) {
      console.error(`Failed to fetch data: ${res.statusCode}`);
      return;
    }

    const filmData = JSON.parse(body);
    const charactersURLs = filmData.characters;

    // Fetch character names
    const charactersPromises = charactersURLs.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, (charErr, charRes, charBody) => {
          if (charErr) {
            reject(charErr);
            return;
          }
          if (charRes.statusCode !== 200) {
            reject(new Error(`Failed to fetch data: ${charRes.statusCode}`));
            return;
          }
          resolve(JSON.parse(charBody).name);
        });
      });
    });

    // Print character names
    Promise.all(charactersPromises)
      .then((names) => {
        console.log(names.join('\n'));
      })
      .catch((allErr) => {
        console.error('Error fetching character names:', allErr);
      });
  });
} else {
  console.error('Please provide a Movie ID as an argument.');
}
