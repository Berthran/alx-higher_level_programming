$(function () {
  function getTranslation () {
    const langCode = $('#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;

    $.ajax({
      type: 'GET',
      url,
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  }

  $('#btn_translate').click(function () {
    getTranslation();
  });

  $('#language_code').on('keydown', function (event) {
    if (event.keyCode === 13) {
      getTranslation();
    }
  });
});
