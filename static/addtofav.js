'use strict';
let btns = document.querySelectorAll('.favorite')
// let favs = document.querySelector('favproducts')
// const fav_prods = favs.name

btns.forEach(function (i) {i.addEventListener('click', evt => {
    evt.preventDefault();
    const obj_fav = i.value;
    console.log(obj_fav);

    const queryString = new URLSearchParams({name: obj_fav})
    const url = `/addfavorite?${queryString}`;


    fetch(url)
        .then((response) => response.json())
        .then((prodlist) => { console.log(prodlist);
        let prod_string = "";
        for (const k of prodlist) {
            console.log(k);
            console.log(k["id"]);
            prod_string = prod_string + '<li>' + (k["id"]) + '</li>';
            console.log(prod_string);
        };
        document.querySelector('.favorite-product').innerHTML=prod_string;
        })

    });})

    // const queryString = new URLSearchParams({irritants: checkboxes, search: search})
    // const url = `/addfavorite?${queryString}`;



    // fetch(url)
    //     .then((response) => response.text())
    //     .then((result) => { console.log(result);
    //     document.querySelector('#fav-text').innerHTML = result;
    //     })

    // });})