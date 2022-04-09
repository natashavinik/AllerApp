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
        .then((response) => response.json())
        .then((result) => { console.log(result);
        console.log(result[0]["canhave"]);
        console.log(result[1]["cp"]);
        console.log(result[2]["allprods"]);
        let site_area = (result[0]["canhave"]);
        let prod_id = (result[1]["cp"]);
        let prodlist = (result[2]["allprods"]);
        let prod_string = "";
        for (const k of prodlist) {
            console.log(k["name"]);
            prod_string = `${prod_string}<li>${k["name"]}<button class="favorite" value="${prod_id}">Add to favorites</button></li>`;
            console.log(prod_string);
        };

        
        
            document.querySelector('#result-text').innerHTML = prod_string;
        })

    });




    // fetch(url)
    //     .then((response) => response.json())
    //     .then((result) => { console.log(result);
    //     console.log(result[0]["canhave"]);
    //     console.log(result[1]["cp"]);
    //     console.log(result[2]["allprods"]);
    //     let site_area = (result[0]["canhave"]);
    //     let prodlist = (result[2]["allprods"]);
    //     let prod_string = "";
    //     for (const k of prodlist) {
    //         console.log(k["name"]);
    //         prod_string = prod_string + '<li>' + (k["name"]) + '</li>';
    //         console.log(prod_string);
    //     };

        
        
    //         document.querySelector('#result-text').innerHTML = prod_string;
    //     })

    // });

