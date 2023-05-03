$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const movies = data.results;
    for (const movie of movies) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    }
  });
});
