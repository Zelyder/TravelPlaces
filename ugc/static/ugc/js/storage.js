
window.onload = function () {
var lang = gettext('lang')
localStorage.setItem('lang', lang);
console.log("Language: " + lang);

var langBtn = document.getElementById("langBtn")

  var dateText = document.getElementById("date")
  var date = localStorage.getItem('date');
  if (date == null) {
      dateText.text = new Date().toLocaleString();
  } else {
    dateText.text = date;
  }
  localStorage.setItem('date', new Date().toLocaleString());
}
