#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  for (const char of characters) {
    request(char, (err, res, body) => {
      if (err) {
        console.error('Error:', err);
        return;
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
