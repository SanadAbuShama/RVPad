$(document).ready(function () {
  $("#name").keyup(function () {
    var data = $("#restForm").serialize(); // capture all the data in the form in the variable data
    $.ajax({
      method: "POST", // we are using a post request here, but this could also be done with a get
      url: "/rvpad/name",
      data: data,
    }).done(function (res) {
      $("#nameMsg").html(res); // manipulate the dom when the response comes back
      $("#nameMsg,.success").css("color", "#54f542");
      $("#nmaeMsg,.error").css("color", "#f5ed05");
    });
  });

  //Location

  $("#location").keyup(function () {
    value = $("#location").val();
    if (value.length < 2) {
      $("#location_msg").html(
        "<p>Location should be at least 2 characters</p>"
      );
      $("#location_msg").css("color", "#f5ed05");
    } else {
      $("#location_msg").html("<p>Looks Good!</p>");
      $("#location_msg").css("color", "#54f542");
    }
  });

  //Description

  $("#desc").keyup(function () {
    value = $("#desc").val();
    if (value.length < 10) {
      $("#desc_msg").html(
        "<p>Description should be at least 10 characters</p>"
      );
      $("#desc_msg").css("color", "#f5ed05");
    } else {
      $("#desc_msg").html("<p>Looks Good!</p>");
      $("#desc_msg").css("color", "#54f542");
    }
  });
});
