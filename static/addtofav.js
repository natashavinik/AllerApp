'use strict';

document.querySelector('#addtofav').addEventListener('submit', evt => {
    evt.preventDefault();
    const obj_fav = document.querySelector('button[id="favorite"]').value;
    console.log(obj_fav);

    const queryString = new URLSearchParams({name: obj_fav})
    const url = `/addfavorite?${queryString}`;


    fetch(url)
        .then((response) => response.text())
        .then((result) => { console.log(result);
        document.querySelector('#fav-text').innerHTML = result;
        })

    });

    // const queryString = new URLSearchParams({irritants: checkboxes, search: search})
    // const url = `/addfavorite?${queryString}`;