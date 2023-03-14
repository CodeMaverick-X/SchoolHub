$(function() {
    // Get the modal
    $('#semester').on('click', function() {
        $('.dropdown-content_semester').css("display", "block")
    })


    var modal = $('#set-edit_id')[0];
    
    $('#edit_button').on('click', function() {
        $('.edit-add_modal').css("display", "block");
    })
    $('.cancelbtn').on('click', function() {
        $('#set-edit_id').css("display", "none");
    })
    
    
    
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }
})