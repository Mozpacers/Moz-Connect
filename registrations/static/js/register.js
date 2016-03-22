$(document).ready(function() {
  $('#ajaxProgress').hide();
  $(document).on('submit', '#registration-form', function(e) {
    e.preventDefault();
    $('#ajaxProgress').show();
    $.ajax({
      type: 'POST',
      url: '/save_registeration_form/',
      dataType: "json",
      async: true,
      data: {
        first_name: $('#id_first_name').val(),
        last_name: $('#id_last_name').val(),
        is_mozillian: $('#id_is_mozillian').is(':checked'),
        phone_number: $('#id_phone_number').val(),
        email: $('#id_email').val(),
        want_to_contribute: $('#id_want_to_contribute').is(':checked'),
        contribution_area: $('#id_contribution_area').val(),
        query_or_suggestions: $('#id_query_or_suggestions').val(),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      }
    })
    .done(function(data) {
      $('#ajaxProgress').hide();
      if(data.message=="Success") {
        $('#status').text("Thanks for connecting! We'll get back to you soon");
      }
      if(data.message=="Fail") {
        $('#status').text("Sorry, your response could not be saved due to some technical glitch!");
      }
      $('#registration-form input').val('');
      $('label').removeClass('active');
      $('i').removeClass('active');
    })
    .error(function(data) {
      $('#ajaxProgress').hide();
      $('#status').text("Our servers are experiencing some difficulty at the moment! Please try again later.");
    });
  });
});
