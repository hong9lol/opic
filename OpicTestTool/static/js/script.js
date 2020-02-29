var play_question_button = document.getElementById("play_question_button");
var add_question_button = document.getElementById("add_question_button");
var add_question_modal = document.getElementById("add_question_modal");
var add_question_modal_span = document.getElementById(
  "add_question_modal_close"
);

play_question_button.onclick = function() {
  question_audio.play();
};

add_question_button.onclick = function() {
  add_question_modal.style.display = "block";
};

add_question_modal_span.onclick = function() {
  add_question_modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == add_question_modal) {
    add_question_modal.style.display = "none";
  }
};
