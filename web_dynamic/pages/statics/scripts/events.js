$(function() {
    
    // add-edit modal form
    let modal = $('.edit-add_modal')[0];
    
	// drop down for day
	$("#dropdown-toggle1").click(function() {
		$("#dropdown1").slideToggle();
	});
    // drop down for time
	$("#dropdown-toggle2").click(function() {
		$("#dropdown2").slideToggle();
	});

    // function to load events duhh
    function load_events() {
        $.ajax({
            url: '/api/v1/events',
                method: 'GET',
                success: function(response, textstat) {
                    for (event1 of response) {
                        $(`#${event1.tag}`).text(`${event1.name}`);
                    }
                },
                error: function(xhr, textstat) {
                    let errorMsg = xhr.responseText;
                    console.log('something happened')
                    console.log(textstat);
                }
        })
    }
    load_events();

    // edit add button to display modal
    // and cancel button inside of the mmodal
    $('.edit_button').on('click', function() {
        $('.edit-add_modal').css("display", "block");
    })
    $('.cancelbtn').on('click', function() {
        $('.edit-add_modal').css("display", "none");
    })

    // set-edit event submit action for the form
    $('#dropdown-form').submit(function(event) {

        event.preventDefault();
        let name = $('#event_name').val();
        let day = $('#dropdown1').val();
        let time = $('#dropdown2').val();
        let tag = day + "_" + time;

        set_event(name, day, time, tag);
    })

    // clear event sets the event name to a space char
    $('#clear_event').click(function(event) {

        event.preventDefault();
        let name = " ";
        let day = $('#dropdown1').val();
        let time = $('#dropdown2').val();
        let tag = day + "_" + time;

        set_event(name, day, time, tag);
    })
    
    // sets the event name
    function set_event(name, day, time, tag) {
        $.ajax({
            url: `/api/v1/events`,
            method: 'PUT',
            data: {
              name: name,
              tag: tag
            },
            success: function(response) {
              $('.edit-add_modal').css("display", "none");
              load_events();
            },
            error: function(xhr, textstat) {
              let errorMsg = xhr.responseText;
              console.log('something happened')
              console.log(textstat);
            }
          });
    }
    
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }
})