$(function() {

    grade_id = ""

    // load the current grades for the current semester and year
    function load_grade() {
        $.ajax({
            url: '/api/v1/grades',
                method: 'GET',
                success: function(response) {

                    $('.grade').remove();
                    for (grade of response) {
                        t_row = `<tr class="grade">
                        <td><button class="edit_button" id="${grade.id}">${grade.name}</button></td>
                        <td>${grade.weight}</td>
                        <td>${grade.ca}</td>
                        <td>${grade.exam}</td>
                        <td>${grade.total}</td>
                        <td>${grade.grade}</td>
                    </tr>`

                    $('#grades_table').append(t_row);
                    }
                    $('.edit_button').on('click', function() {
                        grade_id = $(this).attr('id');
                        console.log(grade_id);
                        $('.edit-add_modal').css("display", "block");
                    })
                    $('.cancelbtn').on('click', function() {
                        $('.edit-add_modal').css("display", "none");
                    })
                },
                error: function(xhr, textstat) {
                let errorMsg = xhr.responseText;
                console.log(errorMsg)
                }
        })
    }
    load_grade();


    // edit grade details
    $('.edit_form').submit(function(event) {

        event.preventDefault();
        let weight = $('#weight').val();
        let ca = $('#ca').val();
        let exam = $('#exam').val();

        $.ajax({
            url: `/api/v1/grades/${grade_id}`,
            method: 'PUT',
            data: {
              weight: weight,
              ca: ca,
              exam: exam
            },
            success: function(response) {
              //console.log(response);
              $('.edit-add_modal').css("display", "none");
              load_grade();
            },
            error: function(xhr, textstat) {
              let errorMsg = xhr.responseText;
              alert('something happened')
              console.log(textstat);
            }
          });
    })
    
    // add-edit modal form
    let modal = $('.edit-add_modal')[0];
    
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }
})