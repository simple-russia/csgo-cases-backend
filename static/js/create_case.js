const upload_btn = document.querySelector('.upload-btn')
const upload_inp = document.querySelector('#img-upload')
const create_btn = document.querySelector('.create-weapon')
const img = document.querySelector('.photo > img')

const price = document.querySelector('.price-cont > input');
const name = document.querySelector('.name-cont > input');

let active_weapon_img;

const validCheck = () => {
    const isImg = !!active_weapon_img;
    const isPrice =  price.value !== '';
    const isName = name.value !== '';
    const isPrice2 = document.querySelectorAll(':invalid').length === 0

    if (isImg && isPrice && isName && isPrice2) {
        create_btn.classList.remove('blocked')
    } else {
        create_btn.classList.add('blocked')
    }
}
validCheck()

upload_inp.addEventListener('change', _ => setTimeout(validCheck, 150));
name.addEventListener('input', validCheck);
price.addEventListener('input', validCheck);

upload_btn.addEventListener('click', () => {
    upload_inp.click();
})

upload_inp.addEventListener('change', (event) => {
    const file = upload_inp.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = () => {
            const result = reader.result;
            img.src = result;
            active_weapon_img = result;
        }
        reader.readAsDataURL(file)
    }
})

const displayMessage = (message) => {
    const text = `${message.action} ${message.status}: ${message.status_message}`;

    const msg_cont = document.querySelector('.message-cont');

    const msg_element = document.createElement('div');
    msg_element.classList.add('message');
    msg_element.classList.add(message.isError ? 'error' : 'success');
    msg_element.innerText = text;

    msg_cont.appendChild(msg_element);

    setTimeout( _ => { try { msg_element.remove() } catch(e) {null} }, 5000);
}



const createWeapon = () => {

    const data = {}
    data.obj_ = 'case';

    data.price = parseInt(price.value);
    data.name = name.value;
    data.image = active_weapon_img;

    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const url = "http://127.0.0.1:2000/api/create"
    fetch(url, {
        method: 'POST',
        body: JSON.stringify( {...data} ),
        headers: {
            'X-CSRFToken':  csrf_token,
        }
    })
    .then(response => response.json())
    .then(data => {
        displayMessage(data);
        if (!data.isError) {
            console.log('redirect in 5 seconds');
            setTimeout( _ => window.location = `/admin-panel/?weapon=${data.payload}` , 5000);
        }
    });
}

create_btn.addEventListener('click', createWeapon);