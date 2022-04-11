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
            resulttext = `<div class="alert alert-success" role="alert">` + "Yay! You're <b>not allergic</b> to " + prodname + "!</div>";
            for (const k of prodlist) {
                console.log(k["name"]);
                console.log(k["id"]);
                let each_id = (k["id"])
                prod_string = `${prod_string}<li>${k["name"]} <button class="favorite btn btn-outline-secondary btn-sm" value="${each_id}"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
              </svg>Add</button></li>`;
            };

        }else{
            for (const k of prodlist) {
                console.log(k["name"]);
                prod_string = `${prod_string}<li>${k["name"]}</li>`;
            };
            resulttext = `<div class="alert alert-danger" role="alert">` + "Oh no! <b>You're allergic</b> to " + prodname + "! <br><br> These are the culprits: " + bad_ings + "</div>";
        }
        
            document.querySelector(`.${site_area}`).innerHTML = prod_string;
            document.querySelector('#result-text').innerHTML = resulttext + `<div class="accordion-item"><h2 class="accordion-header" id="headingOne"><button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne"> <strong>Ingredients List: &nbsp;</strong>  ` + prodname + `</button></h2><div id="collapseOne" class="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#accordionExample"><div class="accordion-body">` + all_ings + `</div></div></div>`;
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

