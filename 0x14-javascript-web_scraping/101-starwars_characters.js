#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    const requests = characters.map((url) => {
      return new Promise((resolve, reject) => {
        request(url, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });
    Promise.all(requests).then((names) => {
      names.forEach((name) => console.log(name));
    }).catch((error) => console.error(error));
  }
});
