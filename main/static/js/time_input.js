  document.addEventListener("DOMContentLoaded", function() {
  var timeInput = document.getElementById("mailing_time");

  timeInput.addEventListener("input", function(event) {
    var input = event.target.value.replace(/\D/g, "");
    var formattedInput = "";

    if (input.length > 2) {
      formattedInput += input.substr(0, 2) + ":";
      input = input.substr(2);
    }

    if (input.length > 2) {
      formattedInput += input.substr(0, 2) + ":";
      input = input.substr(2);
    }

    formattedInput += input;

    event.target.value = formattedInput;
  });
});