let passwordDisplay = document.querySelector('#password-display'),
    passwordUpdateButton = document.querySelector('#passowrd-update-button'),
    passwordHiddenInput = document.querySelector('#id_value'),
    stringSizeRange = document.querySelector('#string-size-range'),
    stringSizeDisplay = document.querySelector('#string-size-display'),
    errorList = document.getElementsByClassName('errorlist');

function generatePasswordValue(passwordSize) {
    const url = `/api/passwords/value/size=${passwordSize}/`

    fetch(url)
        .then(response => response.json())
        .then(password => {
            passwordDisplay.innerHTML = password.value;
            passwordHiddenInput.value = password.value;
        });
}

function copyLinkToClipboard(id) {
    let hostname = window.location.host,
        url = `${hostname}/passwords/${id}/`;

    navigator.clipboard.writeText(url);
}

if (stringSizeDisplay && stringSizeRange) {
    generatePasswordValue(8);
    stringSizeDisplay.value = stringSizeRange.value;

    passwordUpdateButton.addEventListener('click', () => {
        generatePasswordValue(stringSizeRange.value);
    });
    
    stringSizeRange.addEventListener('input', () => {
        stringSizeDisplay.value = stringSizeRange.value;
        generatePasswordValue(stringSizeRange.value);
    });
    
    stringSizeDisplay.addEventListener('focusout', () => {
        stringSizeRange.value = stringSizeDisplay.value;
        generatePasswordValue(stringSizeDisplay.value);
    });
}

