#!/usr/bin/node
import fetch from 'node-fetch';

async function getMovieCharacters (movieId) {
  try {
    const response = await fetch(`https://swapi.dev/api/films/${movieId}/`);
    const movieData = await response.json();
    const characters = movieData.characters;

    const characterNames = await Promise.all(characters.map(async (characterUrl) => {
      const characterResponse = await fetch(characterUrl);
      const characterData = await characterResponse.json();
      return characterData.name;
    }));

    return characterNames;
  } catch (error) {
    console.error(`Error fetching movie data for Movie ID ${movieId}`);
    process.exit(1);
  }
}

async function main () {
  if (process.argv.length !== 3) {
    console.log('Usage: node 0-starwars_characters.js <Movie ID>');
    process.exit(1);
  }

  const movieId = parseInt(process.argv[2]);
  const characterNames = await getMovieCharacters(movieId);
  characterNames.forEach((name) => console.log(name));
}

main();
