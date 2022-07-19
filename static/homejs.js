'use strict';

console.log('Hello, world!');

$(function() {
    $("#searchBox").autocomplete({
        source : function(request, response) {
            $.ajax({
                type: "POST",
                url : "http://http://35.167.141.238/search",
                dataType : "json",
                cache: false,
                data : {
                    q : request.term
                },
                success : function(data) {
                    //alert(data);
                    //console.log(data);
                    response(data.slice(0,5));
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    console.log(textStatus + " " + errorThrown);
                }
            });
        },
        minLength : 1
    });
});



// const formInputs = {
//     type: document.querySelector('#type-field').value,
//     amount: document.querySelector('#amount-field').value,
// };

// fetch('/new-order', {
//     method: 'POST',
//     body: JSON.stringify(formInputs),
//     headers: {
//     'Content-Type': 'application/json',
//     },
// })
//     .then(response => response.json())
//     .then(responseJson => {
//     alert(responseJson.status);
//     });
  
