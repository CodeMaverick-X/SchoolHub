$(function() {
    
    // add-edit modal form
    let modal = $('.edit-add_modal')[0];
    
    $('.edit_button').on('click', function() {
        $('.edit-add_modal').css("display", "block");
    })
    $('.cancelbtn').on('click', function() {
        $('.edit-add_modal').css("display", "none");
    })

    
		
		$("#dropdown-toggle1").click(function() {
			$("#dropdown1").slideToggle();
		});

		$("#dropdown-toggle2").click(function() {
			$("#dropdown2").slideToggle();
		});
    
    
    
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }
})