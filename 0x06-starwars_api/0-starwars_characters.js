#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (movieId === undefined) process.exit(1);

const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(url, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(2);
  }

  const movieData = JSON.parse(body);

  const characters = movieData.characters;

  for (const each of characters) {
    const name = await getName(each);
    if (name) console.log(name);
  }
});

function getName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        reject(error);
      }

      const characterData = JSON.parse(body);
      resolve(characterData.name);
    });
  });
}
