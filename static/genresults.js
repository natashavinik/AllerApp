'use strict';
// let btns = document.querySelectorAll('.favorite')


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
            document.querySelector('#result-text').innerHTML=result;
        })
    })
            




// var btns = document.getElementsByClassName('favorite');


// Array.from(btns).forEach(function(btns) {
//     btns.addEventListener('click', evt => {
//     evt.preventDefault();
//     const obj_fav = i.value;
//     console.log(obj_fav);

//     const queryString = new URLSearchParams({name: obj_fav})
//     const url = `/addfavorite?${queryString}`;


//     fetch(url)
//         .then((response) => response.json())
//         .then((prodlist) => { console.log(prodlist);
//         let prod_string = "";
//         for (const k of prodlist) {
//             console.log(k);
//             console.log(k["id"]);
//             prod_string = prod_string + '<li>' + (k["id"]) + '</li>';
//             console.log(prod_string);
//         };
//         document.querySelector('.favorite-product').innerHTML=prod_string;
//         })

//     });}
// )



    // const queryString = new URLSearchParams({irritants: checkboxes, search: search})
    // const url = `/addfavorite?${queryString}`;



    // fetch(url)
    //     .then((response) => response.text())
    //     .then((result) => { console.log(result);
    //     document.querySelector('#fav-text').innerHTML = result;
    //     })
