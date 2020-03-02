var play_question_button = document.getElementById("play_question_button");
var add_question_button = document.getElementById("add_question_button");
var add_question_modal = document.getElementById("add_question_modal");
var add_question_modal_span = document.getElementById(
  "add_question_modal_close"
);
var add_question_save_button = document.getElementById(
  "add_question_save_button"
);

play_question_button.onclick = function() {
  question_audio.play();
};

add_question_button.onclick = function() {
  // add_question_save_button.removeAttribute("disabled"); // it is not working due to secure error
  add_question_modal.style.display = "block";
};

add_question_save_button.onclick = function() {
  // add_question_save_button.setAttribute("disabled", true);
};

add_question_modal_close.onclick = function() {
  add_question_modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == add_question_modal) {
    add_question_modal.style.display = "none";
  }
};
