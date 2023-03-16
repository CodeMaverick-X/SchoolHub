$(function() {
    // semester and year radio click function

    $("#semester").click(function(){
        $(".dropdown-content_semester").slideToggle("fast");
    });
    
    $("#year").click(function(){
        $(".dropdown-content_year").slideToggle("fast");
    });
    
    $(document).on("click", function(event){
        if(!$(event.target).closest("#semester").length){
            $(".dropdown-content_semester").slideUp("fast");
        }
        if(!$(event.target).closest("#year").length){
            $(".dropdown-content_year").slideUp("fast");
        }
    });
    
    //set the value of the school details from the radio checked

    let year = ""
    let semester = ""

    $("input[name='semester_tag']").click(function() {
        $('#semester').text($("input[name='semester_tag']:checked").val());
        semester = $("input[name='semester_tag']:checked").val();
    })

    $("input[name='year_tag']").click(function() {
        $('#year').text($("input[name='year_tag']:checked").val());
        year = $("input[name='year_tag']:checked").val();
    })

    // reload details from back end
    $('#reload_1').on('click', function() {
        console.log('reloaded');
    })

    let default_year = "";
    let default_semester = "";
    $('#set').click(function() {
        default_year = year;
        default_semester = semester;
        console.log(default_semester, default_year)
    })


    // add-edit modal form
    let modal = $('.edit-add_modal')[0];
    
    $('#edit_button').on('click', function() {
        $('.edit-add_modal').css("display", "block");
    })
    $('.cancelbtn').on('click', function() {
        $('.edit-add_modal').css("display", "none");
    })
    
    
    
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }
})