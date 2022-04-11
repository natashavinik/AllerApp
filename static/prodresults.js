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
        console.log(result[3]["productname"]);
        console.log(result[4]["badingname"]);
        console.log(result[5]["allings"]);
        let site_area = (result[0]["canhave"]);
        let prod_id = (result[1]["cp"]);
        let prodlist = (result[2]["allprods"]);
        let prodname = (result[3]["productname"]);
        let bad_ings = (result[4]["badings"]);
        let all_ings = (result[5]["allings"]);
        let prod_string = "";
        let resulttext = "";
        if(site_area==="notallergic") {
            resulttext = "Yay! You're <b>not allergic</b> to " + prodname + "! <br><br> Full ingredient list: " + all_ings ;
            for (const k of prodlist) {
                console.log(k["name"]);
                console.log(k["id"]);
                let each_id = (k["id"])
                prod_string = `${prod_string}<li>${k["name"]} <button class="favorite" value="${each_id}">Add to favorites</button></li>`;
            };

        }else{
            for (const k of prodlist) {
                console.log(k["name"]);
                prod_string = `${prod_string}<li>${k["name"]}</li>`;
            };
            resulttext = "Oh no! <b>You're allergic</b> to " + prodname + "! <br><br> These are the culprits: " + bad_ings + "<br><br>Full ingredient list: " + all_ings ;
        }
        
            document.querySelector(`.${site_area}`).innerHTML = prod_string;
            document.querySelector('#result-text').innerHTML = resulttext;
        })

    });

//     for (const k of prodlist) {
//         console.log(k["name"]);
//         prod_string = `${prod_string}<li>${k["name"]}<button class="favorite" value="${prod_id}">Add to favorites</button></li>`;
//         console.log(prod_string);
//     };
    
//         document.querySelector(`.${site_area}`).innerHTML = prod_string;
//     })

// });



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

