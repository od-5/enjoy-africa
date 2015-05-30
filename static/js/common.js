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
    $("#block_4 form").validate();
    $("#block_8 form").validate();
    $("footer form").validate();
    $(".modal form").validate();

    $('form.ticket').ajaxForm({
        success: function(data){
            alert(data)
            $('form.ticket').resetForm();
        }
    });

    // Затемнение фона
    $('header button').click(function(){
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
    $(document).mouseup(function (e) {
        var container = $(".modal");
        if (container.has(e.target).length === 0){
        container.hide();
        $('#overlay').remove();
        }
    });

})