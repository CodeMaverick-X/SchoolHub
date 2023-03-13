$(function() {
// Get the modal
var modal = $('#id01')[0];

$('#login_btn').on('click', function() {
    $('#id01').css("display", "block");
})
$('.cancelbtn').on('click', function() {
    $('#id01').css("display", "none");
})




// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
})