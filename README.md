# Random movie generator

## About

The Random Movie Generator program helps you discover new movies to watch, whether you're looking for a completely random movie or a movie within a specific genre.

## Features

1. **Generate Random Movies**: Get a completely random movie suggestion.

2. **Generate Movies by Genre**: Select a genre, and the program will suggest a random movie from that genre.

3. **Create and Manage Your Watchlist**: Keep track of all the movies you've discovered by easily adding movies you want to watch to your watchlist, you can also remove them.

4. **Set a minimum rating for movies**

![image](https://github.com/miglemr/random-movie-generator/assets/113340648/1669c655-c6d0-468e-b401-081c7f2d72fd)

![image](https://github.com/miglemr/random-movie-generator/assets/113340648/38425520-784b-4450-b5ec-a91a4d125236)

## Built With

<code><img width="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/></code>

## API reference

- [TMDB](https://developer.themoviedb.org/docs/getting-started): The Movie Database (TMDB) API

## Getting started

1. Install all required modules by typing _pip install -r requirements.txt_ in the command line
2. To be able to get the movies you need an API key from TMDB, store it in .env file (like in .env.example)
3. Run program by typing _python main.py_
4. Choose a mode

**Additionally**
you have the option to set a minimum rating for the movies you'd like to generate through the command line. By default minimum rating is 7.5 E.g.:
_python main.py **-r 8.1**_
