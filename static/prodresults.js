'use strict';

console.log('Hello, world!');


document.querySelector('#Check').addEventListener('submit', evt => {
    evt.preventDefault();
    let checkboxes = [];
    for (const checkbox of document.querySelectorAll('input[type="checkbox"]')) {
        if (checkbox.checked) {
            checkboxes.push(checkbox.value);
        }
    }
    console.log(checkboxes);
    const search = document.querySelector('input[type="text"]').value;
    console.log(search);

    const queryString = new URLSearchParams({irritants: checkboxes, search: search})
    const url = `/submitirritants?${queryString}`;


    fetch(url)
        .then((response) => response.text())
        .then((result) => { console.log(result);
        document.querySelector('#result-text').innerHTML = result;
        })

    });