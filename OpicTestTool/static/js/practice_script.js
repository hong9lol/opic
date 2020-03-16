//Practice HTML
var play_question_button = document.getElementById("play_question_button");
var add_question_button = document.getElementById("add_question_button");
var add_question_modal = document.getElementById("add_question_modal");
var practice_question_audio = document.getElementById(
  "practice_question_audio"
);

var add_question_modal_span = document.getElementById(
  "add_question_modal_close"
);
var add_question_save_button = document.getElementById(
  "add_question_save_button"
);

play_question_button.onclick = function() {
  practice_question_audio.play();
};

add_question_button.onclick = function() {
  // add_question_save_button.removeAttribute("disabled"); // it is not working due to secure error
  document.getElementById("p_warning").style.visibility = "hidden";
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

function addQeustionValidate() {
  var _title = document.getElementById("id_title").value;
  var _question = document.getElementById("id_question").value;
  var _warning = document.getElementById("p_warning");

  if (_title.length > 30) {
    _warning.innerHTML = "*The title is too long.";
    _warning.style.visibility = "visible";
    return false;
  }

  for (var i in question_titles) {
    if (question_titles[i] == _title) {
      _warning.innerHTML = "*The title already exists.";
      _warning.style.visibility = "visible";
      return false;
    }
  }

  if (_question.length > 500) {
    _warning.innerHTML = "*The question is too long.";
    _warning.style.visibility = "visible";
    return false;
  }

  return true;
}
