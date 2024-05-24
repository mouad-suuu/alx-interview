#!/usr/bin/node

const request = require('request');

// Function to get character names
const getCharacterNames = (url, index, characters) => {
  if (index === characters.length) return;
  request(characters[index], (err, res, body) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(JSON.parse(body).name);
    getCharacterNames(url, index + 1, characters);
  });
};

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  getCharacterNames(apiUrl, 0, characters);
});
