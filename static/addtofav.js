'use strict';
// let btns = document.querySelectorAll('.favorite')


document.body.addEventListener('click', function (evt) {
    if (evt.target.classList.contains('favorite')) {
        evt.preventDefault();
        const obj_fav = evt.target.value;
        console.log(obj_fav);
     
        const queryString = new URLSearchParams({name: obj_fav})
        const url = `/addfavorite?${queryString}`;
    
    
        fetch(url)
            .then((response) => response.json())
            .then((prodlist) => { console.log(prodlist);
            let prod_string = "";
            for (const k of prodlist) {
                console.log(k);
                console.log(k["name"]);
                prod_string = prod_string + '<div class="card"><div class="card-body" id="favprodsbod"><h7 class="card-title">' + (k["name"]) + '<p>' + '<button class="favorite btn btn-outline-secondary btn-sm" value="' + (k["id"]) + '">Remove</button>' + '</div></div>';
                console.log(prod_string);
            };
            document.querySelector('#thefavorites').innerHTML=prod_string;
        })
    }})
            



//     for (const k of prodlist) {
//         console.log(k);
//         console.log(k["name"]);
//         prod_string = prod_string + '<li>' + (k["name"]) + ' ' + '<button class="favorite btn btn-outline-secondary btn-sm" value="' + (k["id"]) + '">Remove</button>' + '</li>';
//         console.log(prod_string);
//     };
//     document.querySelector('.favorite-product').innerHTML=prod_string;
// })
// }})



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
