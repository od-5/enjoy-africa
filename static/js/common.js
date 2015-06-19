/**
 * Created by alexy on 28.05.15.
 */
$(window).load(function() {
    $('.slider_1').flexslider({
        animation: "slide",
        selector: ".slides_1 > li",
        animationLoop: true,
        controlNav: false,
        itemWidth: 800,
        itemMargin: 1
    });
    $('.slider_2').flexslider({
        animation: "slide",
        animationLoop: true,
        controlNav: false,
        itemWidth: 190,
        itemMargin: 4
    });

    $.validator.messages.required = "* поле обязательно для заполнения";
    $("input[type='text'], input[type='email']").addClass("required");
    //$("#block_4 form").validate();
    //$("#block_8 form").validate();
    //$("footer form").validate();
    $(".modal form").validate();

    $('form.ticket').ajaxForm({
        success: function(data){
            $('.modal').fadeOut();
            if ($('#overlay')) {
                console.log(data);
                $('#overlay').remove();
            }
            $('form.ticket').resetForm();

        }
    });

    // текс кнопки формы в footer и в #block_8
    $('#block_8 .button').html('Узнайте стоимость<br /><span class="underline">получив актуальную информацию на Ваш e-mail</span>');
    //$('#block_8 .button').html('Узнайте стоимость' + '<br />' + 'asd');
    $('footer .button').text('Да! Я хочу на сафари!');

    // Затемнение фона
    $('header button, form .button').click(function(){
        username = $(this).parent('form').find('input[name="name"]').val();
        email = $(this).parent('form').find('input[name="email"]').val();
        if (username) {
            $('.modal input[name="name"]').val(username);
        }
        if (email) {
            $('.modal input[name="email"]').val(email);
        }
        $('.modal').fadeIn();
        var docHeight = $(document).height();
        $("body").append("<div id='overlay'></div>");
        $("#overlay")
           .height(docHeight)
           .css({
              'opacity' : 0.4,
              'position': 'fixed',
              'top': 0,
              'left': 0,
              'background-color': 'black',
              'width': '100%',
              'z-index': 9
           });
    });

    // Закрытие модального окна
    //$(document).mouseup(function (e) {
    //    var container = $(".modal");
    //    if (container.has(e.target).length === 0){
    //        container.hide();
    //        $('#overlay').remove();
    //    }
    //});
    $('.modal .close').click(function (e) {
        var container = $(".modal");
        if ($('#overlay')){
            container.hide();
            $('#overlay').remove();
        }
    });

})