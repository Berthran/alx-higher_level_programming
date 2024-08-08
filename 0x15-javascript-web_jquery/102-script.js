$(function () {
  $('#btn_translate').click(function () {
    const langCode = $('#language_code').val();
    $.ajax({
      type: 'GET',
      url: 'https://hellosalut.stefanbohacek.dev/?lang=' + langCode,
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  });
});
