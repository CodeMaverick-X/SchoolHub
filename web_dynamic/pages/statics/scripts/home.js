$(function() {

    $.ajax({
        url: '/api/v1/quote',
        method: 'GET',
        success: (response) => {
            response = JSON.parse(response);
            $('.quote_text').text(response[0]['quote']);
            $('.author').text(response[0]['author']);
            console.log(response[0]['quote']);
            console.log(response[0]);
            console.log('me');
        },
        error: (xhr) => {
            let errorMsg = xhr.responseText;
            console.log(errorMsg);
        }
    })
})