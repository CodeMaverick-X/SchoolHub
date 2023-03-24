$(function() {

    let year = 0
    let semester = 0
    // get the current school info set from the back end
    // update the drop down with the current info
    $.ajax({
        url: '/api/v1/set',
            method: 'GET',
            success: function(response) {
              year = response.year;
              semester = response.semester
              $('#dropdown2').val($(`#dropdown2 .${year}`).val());
              $('#dropdown1').val($(`#dropdown1 .${semester}`).val());
            },
            error: function(xhr, textstat) {
              let errorMsg = xhr.responseText;
              alert('something happened')
              console.log(textstat);
            },
            complete: load_course()
    })

    // set the selected dropdown settings as defualt in back end
    $('#set').on('click', function() {
        $.ajax({
            url: '/api/v1/set',
            method: 'PUT',
            data: JSON.stringify({
              semester: parseInt($('#dropdown1').val().slice(0,1)),
              year: parseInt($('#dropdown2').val().slice(0,1))
            }),
            success: function(response) {
              load_course()
            },
            error: function(xhr, textstat) {
              let errorMsg = xhr.responseText;
              alert(errorMsg)
            },
            contentType: 'application/json'
        })
    })


    // add-edit modal form
    let modal = $('.edit-add_modal')[0];
    
    $('#edit_button').on('click', function() {
        $('.edit-add_modal').css("display", "block");
    })
    $('.cancelbtn').on('click', function() {
        $('.edit-add_modal').css("display", "none");
    })

    // handle the creation of courses [add/edit] button #edit_form

    selected_courses = []
    $('#edit_form').submit(function(event) {

        event.preventDefault();
        let name = $('#course_name').val();
        let description = $('#course_disc').val();

        $.ajax({
            url: '/api/v1/courses',
            method: 'POST',
            data: {
              name: name,
              description: description
            },
            success: function(response, textstat) {
              $('.edit-add_modal').css("display", "none");
              load_course();
            },
            error: function(xhr, textstat) {
              let errorMsg = xhr.responseText;
              alert('something happened')
              console.log(textstat);
            },
            complete: load_course()
          });
    })

    // load courses
    function load_course() {
        console.log('near');
        $.ajax({
            url: '/api/v1/courses',
            method: 'GET',
            success: function(response, textstat) {
                $('.course_list').empty();
                for (course of response) {
                    let c_box = `<label class="course">${course.name}<input type="checkbox" name="checkbox" value="${course.name}" id="${course.id}"></label>`;
                    $('.course_list').append(c_box);
                }
            },
            error: function(xhr, textstat) {
                let errorMsg = xhr.responseText;
                alert('something happened');
                console.log(textstat);
            }
        });
    }

    load_course();
    // ___delete course___
    
    function delete_course(course_id="") {
        $.ajax({
            url: `/api/v1/courses/${course_id}`,
            method: 'DELETE',
            success: function(response) {
                load_course();
            },
            error: function(xhr, textstat) {
                let errorMsg = xhr.responseText;
                alert('something happened');
                console.log(textstat);
            }
        })
    }
    //___delete courese___

    // function that placed selected course in an object and returns it
    function checker() {
        let checked = {};
        $('input').each(function() {
            let course_id = $(this).attr('id');
            let course_name = $(this).attr('value');

            if ($(this).is(':checked')) {
                checked[course_name] = course_id;
            }
            else {
                delete checked.course_name;
            }
        });

        return checked;
    }

    $('#delete_button').on('click', function() {
        checked = checker();
        let checked_l = Object.values(checked);

        for (course_id of checked_l) {
            delete_course(course_id);
        }
    })
    
    
    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    }
})