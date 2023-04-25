#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const movies = JSON.parse(body).results;
    const numMovies = movies.filter(movie => movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')).length;
    console.log(numMovies);
  }
});
