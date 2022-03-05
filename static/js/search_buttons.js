
const filter = document.querySelector('.filter-btn');
const search_btn = document.querySelector('.search-btn');
const filter_modal = document.querySelector('.filters-modal');
const close_filter = document.querySelector('.close-filter-modal');
const clear_search = document.querySelector('.clear');

const case_options = document.querySelector('.case-options');
const weapon_options = document.querySelector('.weapon-options');

let pick_case = document.querySelector('.pick-cases > .pick-checkbox');
let pick_weapon = document.querySelector('.pick-weapon > .pick-checkbox');

// filter options
const filter_options = {
    pick: 'cases',

    filter_cases: {
        min_price: 10,
        max_price: 20,
    },

    filter_weapons: {
        min_price: 5,
        max_price: 30,
        colors: [],
        types: [],
        collections: [],
    }
}

const renderValues = () => {
    let min, max;

    min = document.querySelector('.case-options .min-range');
    max = document.querySelector('.case-options .max-range');
    min.value = filter_options.filter_cases.min_price;
    max.value = filter_options.filter_cases.max_price;

    min = document.querySelector('.weapon-options .min-range');
    max = document.querySelector('.weapon-options .max-range');
    min.value = filter_options.filter_weapons.min_price;
    max.value = filter_options.filter_weapons.max_price;
}
renderValues();




const clearSearchbox = () => {
    document.querySelector('.search-box input').value = '';
}
clear_search.addEventListener('click', clearSearchbox);

const filterToggle = () => {
    filter_modal.classList.toggle('hidden');
}


const pickToggle = (e) => {
    const picked_id = e.target.getAttribute('id')

    if (picked_id === 'cases') {
        pick_case.classList.add('active');
        pick_weapon.classList.remove('active');
        
        case_options.classList.remove('hidden');
        weapon_options.classList.add('hidden');

        filter_options.pick = 'cases';

    } else {
        pick_weapon.classList.add('active');
        pick_case.classList.remove('active');

        case_options.classList.add('hidden');
        weapon_options.classList.remove('hidden');

        filter_options.pick = 'weapons';
    }
}

pick_case.addEventListener('click', pickToggle);
pick_weapon.addEventListener('click', pickToggle);

filter.addEventListener('click', filterToggle);
close_filter.addEventListener('click', filterToggle);




for (let i of document.querySelectorAll('.pick-grid')) {
    i.addEventListener('click', (e) => {
        if (!e.target.classList.contains('pick-checkbox')) { return }

        // handle checkbox click
        e.target.classList.toggle('active');
    })
}


const applyFilters = () => {
    if (filter_options.pick === 'weapons') {
        // weapons options
        const min = document.querySelector('.weapon-options .min-range');
        const max = document.querySelector('.weapon-options .max-range');

        const colors = [];
        const types = [];
        const collections = [];

        for (let i of document.querySelectorAll('.color-options .pick-checkbox.active') ) {
            const id = i.getAttribute('data-id');
            colors.push(parseInt(id));
        }
        for (let i of document.querySelectorAll('.type-options .pick-checkbox.active') ) {
            const id = i.getAttribute('data-id');
            types.push(parseInt(id));
        }
        for (let i of document.querySelectorAll('.collection-options .pick-checkbox.active') ) {
            const id = i.getAttribute('data-id');
            collections.push(parseInt(id));
        }


        filter_options.filter_weapons.min_price = parseInt(min.value ? min.value : filter_options.filter_weapons.min_price);
        filter_options.filter_weapons.max_price = parseInt(max.value ? max.value : filter_options.filter_weapons.max_price);
        filter_options.filter_weapons.colors = colors;
        filter_options.filter_weapons.types = types;
        filter_options.filter_weapons.collections = collections;
    }
    else {
        // case options
        const min = document.querySelector('.case-options .min-range');
        const max = document.querySelector('.case-options .max-range');
        filter_options.filter_cases.min_price = parseInt(min.value ? min.value : filter_options.filter_cases.min_price);
        filter_options.filter_cases.max_price = parseInt(max.value ? max.value : filter_options.filter_cases.max_price);
    }

    filterToggle();
}

const applyButton = document.querySelector('.apply-filters');
applyButton.addEventListener('click', applyFilters);


document.querySelector('#add-weapon').addEventListener('click', _ => window.location = window.location.pathname + '?create=weapon');
document.querySelector('#add-case').addEventListener('click', _ => window.location = window.location.pathname + '?create=case');



const search = () => {
    console.log(filter_options)
    
    const url = "http://192.168.43.247:80/api/search"
    fetch(url, {
        method: 'POST',
        body: JSON.stringify( filter_options ),
    })
    .then(response => response.json())
    .then(data => console.log(data));
}
search_btn.addEventListener('click', search);


