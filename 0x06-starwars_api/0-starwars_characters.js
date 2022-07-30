#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const url = 'https://swapi-api.hbtn.io/api/films/' + movieId + '/';

function printMovieCharacters (url) {
  request(url, async function (error, response, body) {
    if (error) return console.log('There's an error');

    const characters = JSON.parse(body).characters;
    if (!characters) return;

    const promises = [];

    for (const character of characters) {
      let promise = null;

      promise = new Promise(function (resolve, reject) {
        request(character, function (error, response, body) {
          if (error) return console.log('Error fetching the character');
          resolve(JSON.parse(body).name);
        });
      });
      promises.push(promise);
    }

    const data = await Promise.all(promises);
    for (const item of data) {
      console.log(item);
    }
  });
}

printMovieCharacters(url);
