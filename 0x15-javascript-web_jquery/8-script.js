$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      const movies = data.results;
      console.log(movies);
      $.each(movies, function (i, movie) {
        $('#list_movies').append($('<li></li>').text(movie.title));
      });
    }
  });
});
