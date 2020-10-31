const button = document.getElementById('button-menu-username');
const responsive_menu = document.getElementById('responsive_menu');
button.addEventListener('click', function (event) {
    event.preventDefault()
    let menu = document.getElementById('menu-username')
    menu.classList.toggle('hidden')

})

