'use strict'
window.addEventListener('DOMContentLoaded', () => {
    const menu = document.querySelector('.menu'),
    menuItem = document.querySelectorAll('.menu_item'),
    hamburger = document.querySelector('.hamburger');

    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('hamburger_active');
        menu.classList.toggle('menu_active');
    });

    menuItem.forEach(item => {
        item.addEventListener('click', () => {
            hamburger.classList.toggle('hamburger_active');
            menu.classList.toggle('menu_active');
        })
    })

    //scroll
    const links = document.querySelectorAll('a[href*="#"]');
    links.forEach(link => {
        link.addEventListener("click", event => {
            event.preventDefault();
            const id = link.getAttribute('href');
            document.querySelector(`${id}`).scrollIntoView({
                behavior: "smooth",
                block: "start"
            });
        });
    });

    
});