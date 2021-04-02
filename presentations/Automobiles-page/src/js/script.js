$( document ).ready(function() {
    
    function collapse (toCollapse) {
        $('.opener__header').on('click', function () {
            const opener = $('.opener');
            
            if (toCollapse.is(':visible')) {
                document.querySelector('.arrow-right').style.cssText = 'transform: rotate(0deg);'
                $(opener).find(toCollapse).stop().slideUp();
            } else {
                document.querySelector('.arrow-right').style.cssText = 'transform: rotate(90deg);'
                $(opener).find(toCollapse).stop().slideDown();
            }
        });
    }

    collapse($('.cards'));
    //MODAL


    //TABS Motores
    $("#content div").hide(); // Скрываем содержание
	$("#tabs li:first").attr("id","current"); // Активируем первую закладку
	$("#content div:first").fadeIn(); // Выводим содержание
    
    $('#tabs a').click(function(e) {
        e.preventDefault();        
        $("#content div").stop().hide(); //Скрыть все сожержание
        $("#tabs li").attr("id",""); //Сброс ID
        $(this).parent().attr("id","current"); // Активируем закладку
        $('#' + $(this).attr('title')).stop().fadeIn(); // Выводим содержание текущей закладки
    });

    //ANIMATIONS
    $('.animation_up').animated('animate__fadeInDown', 'animate__fadeOutUp')
    $('.animation_down').animated('animate__fadeInUp', 'animate__fadeOutDown')

    $(".animation_flip").animated("animate__flipInY", "animate__fadeOutDown");
	$(".animation_left").animated("animate__fadeInLeft", "animate__fadeOutDown");
	$(".animation_right").animated("animate__fadeInRight", "animate__fadeOutDown");

    $('.tabs__pic').animated('animate__slideInLeft', 'animate__slideOutRight');
    $('.tabs__descr').animated('animate__slideInRight', 'animate__slideOutLeft');
    $('.tabs__pic_am').animated('animate__backInRight', 'animate__backOutRight');
    $('.tabs__descr_am').animated('animate__backInLeft', 'animate__backOutLeft');
});