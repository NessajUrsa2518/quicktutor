$(document).ready(function () {
  if ($(document).scrollTop() != 0) {
    $("header").addClass("is-scrolled");
    $("nav").addClass("navbar-back");
    $(".navbar-brand img").attr("src", "static/images/logo-scroll.svg");
  }
  var flag = 0;
  $("#mobile-btn").click(function () {
    if (flag == 0) {
      $(this).find("img").attr("src", "static/images/cross@1x.svg");
      $("header").addClass("open");
      $("nav").addClass("navbar-back");
      flag = 1;
    }
    else if (flag == 1) {
      $(this).find("img").attr("src", "static/images/burger@1x.svg");
      $("header").removeClass("open");
      if ($(document).scrollTop() == 0)
        $("nav").removeClass("navbar-back");
      flag = 0;
    }
  });

  $(document).scroll(function () {
    var scrollTop = $(document).scrollTop();
    if (scrollTop == 0 && flag == 0) {
      $("header").removeClass("is-scrolled");
      $("nav").removeClass("navbar-back");
      $(".navbar-brand img").attr("src", "static/images/logo.svg");
    }
    else {
      $("header").addClass("is-scrolled");
      $("nav").addClass("navbar-back");
      $(".navbar-brand img").attr("src", "static/images/logo-scroll.svg");
    }
  });

  $('#signup_btn').click(function (e) {
    e.preventDefault();
    $('#signup_btn').attr('disabled', 'disabled');
    $.ajax({
      type: $('#signUpForm').attr('method'),
      url: $('#signUpForm').attr('action'),
      data: $('#signUpForm').serialize(),
      success: function (res) {
        if (res.success) window.location.href = "/";
        else $('#sign-form-wrapper').html(res.form);
        $('#signup_btn').removeAttr('disabled');
      }
    });
  });

  $('#login_btn').click(function (e) {
    e.preventDefault();
    $('#login_btn').attr('disabled', 'disabled');
    $.ajax({
      type: $('#logInForm').attr('method'),
      url: $('#logInForm').attr('action'),
      data: $('#logInForm').serialize(),
      success: function (res) {
        if (res.success) window.location.href = "/";
        else $('#login-form-wrapper').html(res.form);
        $('#login_btn').removeAttr('disabled');
      }
    });
  });

  $('#reset_btn').click(function (e) {
    e.preventDefault();
    $('#loginModal').modal('hide');
    $('#resetModal').modal('show');
  });

  $('#send_btn').click(function (e) {
    e.preventDefault();
    $('#send_btn').attr('disabled', 'disabled');
    $.ajax({
      type: $('#resetForm').attr('method'),
      url: $('#resetForm').attr('action'),
      data: $('#resetForm').serialize(),
      success: function (res) {
        if (res.success) window.location.href = "/";
        else $('#reset-form-wrapper').html(res.form);
        $('#send_btn').removeAttr('disabled');
      }
    });
  });
});