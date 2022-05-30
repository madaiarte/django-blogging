let sayHi = function (name: string): void {
    console.log(`Hello ${name}!`);
}

sayHi("Kim");


// Menu user

let userMenu = document.querySelector('#user-menu') as HTMLElement;
let userOptions = document.querySelector('#user-options') as HTMLElement;


userMenu.onclick = function () {
    let userInfo = document.querySelector('#user-info') as HTMLElement;
    toggle(userInfo);
}

userOptions.onclick = function () {
    let userOption = document.querySelector('#user-option') as HTMLElement;
    toggle(userOption);
}



// Toggle Hide Show function with tailwind
let toggle = function (element: HTMLElement) {
    if (element.classList.contains('hidden')) {
        element.classList.remove('hidden');
    } else {
        element.classList.add('hidden');
    }
}


// Text editor
