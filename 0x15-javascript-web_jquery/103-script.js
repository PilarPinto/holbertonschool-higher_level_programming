// double function
document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function () {
    complete();
  });
  $('INPUT#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      complete();
    }
  });
  function complete () {
    const helloUrl = 'https://fourtonfish.com/hellosalut/?lang=';
    const l = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: `${helloUrl}${l}`,
      success: function (data) {
        $('DIV#hello').text(data.hello);
      }
    });
  }
});
