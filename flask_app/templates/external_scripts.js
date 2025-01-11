

var button = document.getElementById("submit");
button.addEventListener("click", set_before_path);

function set_before_path() {
  var bp = document.getElementById("before_path")
  bp.value = "111"
}
