#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (err, res, body) => {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
