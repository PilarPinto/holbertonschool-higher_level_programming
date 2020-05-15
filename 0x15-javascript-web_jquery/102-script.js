// name in the api
document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function () {
    const helloUrl = 'https://fourtonfish.com/hellosalut/?lang=';
    const l = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: `${helloUrl}${l}`,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
