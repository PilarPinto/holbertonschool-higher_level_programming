// name list in the api
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      const rtd = data.results;
      for (const i in rtd) {
        $('UL#list_movies').append('<li>' + rtd[i].title + '</li>');
      }
    }
  });
});
