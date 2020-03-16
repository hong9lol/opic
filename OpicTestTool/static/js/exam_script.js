// Exam HTML
var isNewQuestion = true;
var timer;

var start_button = document.getElementById("start_button");
var question_number = document.getElementById("question_number");
var speak_time = document.getElementById("speak_time");
var exam_play_button = document.getElementById("exam_play_button");
var exam_end_button = document.getElementById("exam_end_button");
var exam_next_button = document.getElementById("exam_next_button");

var exam_question_audio = document.getElementById("exam_question_audio");
var exam_question_audio_src = document.getElementById(
  "exam_question_audio_src"
);

var question_idx = 0;

start_button.onclick = function() {
  question_idx = 0;
  help_modal.style.display = "none";
  exam_end_button.style.visibility = "hidden";
  exam_question_audio_src.src =
    "http://220.88.28.198/~jake/" + questions[0] + ".mp3";
};

exam_play_button.onclick = function() {
  if (isNewQuestion) {
    setTimer();
    isNewQuestion = false;
  }
  exam_question_audio.load();
  exam_question_audio.play();
};

exam_next_button.onclick = function() {
  clearInterval(timer);
  exam_question_audio.pause();
  exam_question_audio_src.src =
    "http://220.88.28.198/~jake/" + questions[++question_idx] + ".mp3";
  speak_time.innerHTML = "Time: 0:00";
  isNewQuestion = true;

  // When last question
  if (question_idx >= 14) {
    exam_next_button.disabled = "disabled";
    exam_end_button.style.visibility = "visible";
  }

  question_number.innerHTML = "[Question " + (question_idx + 1) + "]";
};

function setTimer() {
  var num = 0;
  var font_color_start = "";
  var font_color_end = "";
  var minute = 0;
  var second = 0;

  timer = setInterval(function() {
    minute = parseInt(num / 60);
    second = num % 60;

    if (num >= 120) {
      font_color_start = '<font color="red">';
      font_color_end = "</font>";
    }
    if (second > 9) {
      speak_time.innerHTML =
        "Time: " + font_color_start + minute + ":" + second + font_color_end;
    } else {
      speak_time.innerHTML =
        "Time: " + font_color_start + minute + ":0" + second + font_color_end;
    }
    num++;
  }, 1000);
}
