$(function() {
    let day;
    switch (new Date().getDay()) {
        case 0:
            day = "sunday";
            break;
        case 1:
            day = "monday";
            break;
        case 2:
            day = "tuesday";
            break;
        case 3:
            day = "wednesday";
            break;
        case 4:
            day = "thursday";
            break;
        case 5:
            day = "friday";
            break;
        case  6:
            day = "saturday";
    }


    // load todays events

    $.ajax({
        url: '/api/v1/events',
            method: 'GET',
            success: function(response, textstat) {

            for (ev of response) {
                let name = ev.name;
                if (ev.day === day && (name.length > 2)) {
                    let st_time = ev.time.split("-")[0] + ":00";
                    let end_time = ev.time.split("-")[1] + ":00";
                    let card = `
                    <div class="event-card">
                        <div class="event_title">${ev.name}</div>
                        <span class="start_time">From <span class="time">${st_time}</span></span>
                        <span class="end_time">To <span class="time">${end_time}</span></span>
                    </div>`;
                    $('.side-panel').append(card);
                }
            }

            },
            error: function(xhr, textstat) {
            let errorMsg = xhr.responseText;
            console.log('something happened')
            console.log(textstat);
            }
    })
})