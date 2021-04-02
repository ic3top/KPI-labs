'use strict'
document.addEventListener("DOMContentLoaded", () => { 
	// collapsable block
	const achv = $('.block__achivements'),
		  arrow_block = document.querySelector('.arrow');

	achv.slideUp();
	$('.block').find('.block__opener').on('click', function () {
		if (achv.is(':visible')) {
			achv.slideUp();
			arrow_block.style.cssText = 'transform: rotate(-90deg);'
		} else {
			achv.slideDown();
			arrow_block.style.cssText = 'transform: rotate(0deg);'
		}
    });
    
    $('.block__achivements').on('click', function () {
		if (achv.is(':visible')) {
			achv.slideUp();
			arrow_block.style.cssText = 'transform: rotate(-90deg);'
		} else {
			achv.slideDown();
			arrow_block.style.cssText = 'transform: rotate(0deg);'
		}
	});

	// Hamburger
	const menu = document.querySelector('.menu'),
    menuItem = document.querySelectorAll('.menu__item'),
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
	});

	// scroll
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
})