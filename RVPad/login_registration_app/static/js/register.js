$(document).ready(function () {
  $("#email").keyup(function () {
    var data = $("#regForm").serialize(); // capture all the data in the form in the variable data
    $.ajax({
      method: "POST", // we are using a post request here, but this could also be done with a get
      url: "/email",
      data: data,
    }).done(function (res) {
      $("#emailMsg").html(res); // manipulate the dom when the response comes back
      $("#emailMsg,.success").css("color", "#54f542");
      $("#emailMsg,.error").css("color", "#f5ed05");
    });
  });

  // First Name

  $("#first_name").keyup(function () {
    value = $("#first_name").val();
    if (value.length < 2) {
      $("#first_name_msg").html(
        "<p>First name should be at least 2 characters</p>"
      );
      $("#first_name_msg").css("color", "#f5ed05");
    } else {
      $("#first_name_msg").html("<p>Looks Good!</p>");
      $("#first_name_msg").css("color", "#54f542");
    }
  });

  //Last name

  $("#last_name").keyup(function () {
    value = $("#last_name").val();
    if (value.length < 2) {
      $("#last_name_msg").html(
        "<p>Last name should be at least 2 characters</p>"
      );
      $("#last_name_msg").css("color", "#f5ed05");
    } else {
      $("#last_name_msg").html("<p>Looks Good!</p>");
      $("#last_name_msg").css("color", "#54f542");
    }
  });

  //Password

  $("#password").keyup(function () {
    value = $("#password").val();
    if (value.length < 8) {
      $("#password_msg").html(
        "<p>Password should be at least 8 characters</p>"
      );
      $("#password_msg").css("color", "#f5ed05");
    } else {
      $("#password_msg").html("<p>Looks Good!</p>");
      $("#password_msg").css("color", "#54f542");
    }
  });
});
