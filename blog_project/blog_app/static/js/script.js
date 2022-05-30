"use strict";
let sayHi = function (name) {
    console.log(`Hello ${name}!`);
};
sayHi("Kim");
// Menu user
let userMenu = document.querySelector('#user-menu');
let userOptions = document.querySelector('#user-options');
userMenu.onclick = function () {
    let userInfo = document.querySelector('#user-info');
    toggle(userInfo);
};
userOptions.onclick = function () {
    let userOption = document.querySelector('#user-option');
    toggle(userOption);
};
// Toggle Hide Show function with tailwind
let toggle = function (element) {
    if (element.classList.contains('hidden')) {
        element.classList.remove('hidden');
    }
    else {
        element.classList.add('hidden');
    }
};
// Text editor
