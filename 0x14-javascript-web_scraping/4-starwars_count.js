#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const movies = JSON.parse(body).results;
    const numMovies = movies.filter(movie => movie.characters.some(characterUrl => characterUrl.includes('/18/')));
    console.log(numMovies.length);
  }
});
