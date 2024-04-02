const $ = window.$;

$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (let i = 0; i <= data.resuls.length; i++) {
    $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
