/**
 * Created by alexy on 28.05.15.
 */
$(window).load(function() {

  var current_url = '/'+location.href.split('/')[3]+'/'
  $('nav > ul > li >a').each(function () {
    if($(this).attr('href') == current_url) $(this).addClass('active');
  });

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

  // сбрасываем поля форм при закрытии модального окна
  $('.popupbutton').fancybox({
    afterClose: function(e){
      $('.ticket').trigger('reset');
    }
  });

  // заполненяем поля модальной формы
  $('.popupbutton').on('click', function(e){
    var form = $(this).parent('form');

    if ($(this).data('group')){
      var group = $(this).data('group');
      //alert(group);
      $('.pop-form__group').val(group);
    }

    if (form.length != 0) {
      var name = form.find('.ticket__name').val();
      var email = form.find('.ticket__email').val();
      $('.pop-form__name').val(name);
      $('.pop-form__email').val(email);
    }
  });

  $.validator.messages.required = "* поле обязательно для заполнения";

  // валидация модальной формы
  $( ".pop-form" ).validate({
    rules: {
      name: {
        required: true
      },
      email: {
        required: true
      }
    },
    submitHandler: function(e) {
      $('.pop-form').ajaxSubmit({
          success: function(data){
            $.fancybox.close();
          }
      });
    }
  });

  $(".video-button").click(function() {
    $.fancybox({
      'padding'	: 0,
      'autoScale'	: false,
      'transitionIn'	: 'none',
      'transitionOut'	: 'none',
      'title'	: this.title,
      'width'	: 640,
      'height'	: 385,
      'href'	: this.href.replace(new RegExp("watch\\?v=", "i"), 'v/'),
      'type'	: 'swf',
      'swf'	: {
        'wmode'	: 'transparent',
        'allowfullscreen'	: 'true'
      }
    });
    return false;
  });

  $('.auth-button').fancybox();

  $( "#login_form" ).validate({
    rules: {
      username: {
        required: true
      },
      password: {
        required: true
      }
    },
    submitHandler: function(e) {
      $('#login_form').ajaxSubmit({
          success: function(data){
            var error = data.error;
            if (error) {
              $('#login_form').trigger('reset');
              $.notify(error, 'error');
            } else {
              $.fancybox.close();
              location.reload(true);
            }
          }
      });
    }
  });

  $( "#registration_form" ).validate({
    rules: {
      username: {
        required: true
      },
      password: {
        required: true
      }
    },
    submitHandler: function(e) {
      $('#registration_form').ajaxSubmit({
          success: function(data){
            var error = data.error;
            if (error) {
              $('#registration_form').trigger('reset');
              $.notify(error, 'error');
            } else {
              $.notify(data.success, 'success');
              $.fancybox.close();
              location.reload(true);
            }
          }
      });
    }
  });

  // валидация формы профиля
  $("#personal_info_form" ).validate({
    rules: {
      email: {
        required: true
      },
      first_name: {
        required: true
      },
      last_name: {
        required: true
      }
    }
  });

  // валидация формы добавления статьи
  $(".travels-review-add-form" ).validate({
    rules: {
      travel: {
        required: true
      },
      title: {
        required: true
      },
      text: {
        required: true
      },
      image: {
        required: true
      }
    }
  });

  $('.group-select').click(function(e){
    $(this).find('.group-select-list').toggle();
  });

  VK.init({
    apiId: 5095724
  });
  function authInfo(response) {
      if (response.session) {
          var id = response.session.mid;
      }
      VK.Api.call('users.get', {uids: id, fields: 'domain, first_name, last_name, home_town, city'}, function(r) {
          var city_id = 0;
          if (r.response) {
              //if (r.response[0].first_name) {
              //    jQuery("#name").val(r.response[0].first_name + ' ' + r.response[0].last_name);
              //}
              //if (r.response[0].mobile_phone) {
              //    jQuery("#phone").val(r.response[0].mobile_phone);
              //} else if (r.response[0].home_phone) {
              //    jQuery("#phone").val(r.response[0].home_phone);
              //}
              console.log('https://vk.com/' + r.response[0].domain);
              console.log(r.response[0].first_name);
              console.log(r.response[0].last_name);
              city_id = r.response[0].city;
              getCityById(city_id);
          }
      });
  }
  function getCityById(city) {
      VK.api('database.getCitiesById', {city_ids: city}, function(data) {
          if (data.response) {
              console.log(data.response[0].name);
          }
      });
  }

  VK.Auth.getLoginStatus(authInfo);


});
