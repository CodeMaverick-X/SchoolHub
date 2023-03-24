$(function() {
// Get the modal
var modal = $('#id01')[0];
var modal_2 = $('#id02')[0];

$('#login_btn').on('click', function() {
    $('#id01').css("display", "block");
})
$('.cancelbtn').on('click', function() {
    $('#id01').css("display", "none");
    $('#id02').css("display", "none");
})


$('#signin_btn').on('click', function() {
    $('#id02').css("display", "block");
})

 $('#login-form').submit(function(event) {
    event.preventDefault(); // prevent default form submission

    var username = $('#login-username').val();
    var password = $('#login-password').val();

    $.ajax({
      url: '/',
      method: 'POST',
      data: {
        username: username,
        password: password
      },
      success: function(response, textstat) {
        // redirect to dashboard on successful login
        console.log(textstat);
        window.location.href = '/home';
      },
      error: function(xhr, textstat) {
        var errorMsg = xhr.responseText;
        alert('wrong user name or password')
        console.log(textstat);
        $('#error-msg').html(errorMsg);
      }
    });
  });
  // registration

  $('#register-form').submit(function(event) {
    event.preventDefault(); // prevent default form submission

    var username = $('#username').val();
    var password = $('#password').val();
    var confirmPassword = $('#confirm-password').val();
    if (password !== confirmPassword) {
      //alert('Passwords do not match!');
      $("#hide_str").css('display', 'block');
      event.preventDefault();
    }
    else {
        $.ajax({
        url: '/register',
        method: 'POST',
        data: {
            username: username,
            password: password
        },
        success: function(response) {
            // redirect to login on successful login
            if (response.success) {
                window.location.href = '/home';
            } else {
                console.log(response.message);
                $(".hide_str").css('display', 'block')
            }
        },
        error: function(xhr) {
            var errorMsg = xhr.responseText;
            $('.error-msg').html(errorMsg);
        }
        });
    }
  });


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
  else if (event.target == modal_2) {
    modal_2.style.display = "none";
  }
}
})