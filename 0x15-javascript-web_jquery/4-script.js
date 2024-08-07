// Add a click event to the element with the id toggle_header
$(function () {
  if (!$('header').hasClass('red') && !$('header').hasClass('green')) { $('header').addClass('red'); }
  $('#toggle_header').click(function () {
    $('header').toggleClass('green red');
  });
});
