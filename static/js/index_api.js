var setup = function() {
    $('.vi-tab > a').on('click', function() {
        var self = $(this);
        $('.active').removeClass('active');
        self.addClass('active');
    });

    var tabAction = function(position, showLogin) {
        $('.vi-block').animate({
            "left": position
        }, "fast");
        $('#id-div-login').toggle(showLogin);
        $('#id-div-signup').toggle(!showLogin);
    };

    $('#id-a-signup').on('click', function() {
        var position = '110px';
        var showLogin = false;
        tabAction(position, showLogin);
    });
    $('#id-a-login').on('click', function() {
        var position = '165px';
        var showLogin = true;
        tabAction(position, showLogin);
    });
};

var loginFrom = function() {
    var keys = {
        'username',
        'password',
    };
    var loginPrefix = 'id-input-login-'；
    var form = formFormKeys(keys, loginPrefix);
    return form;
};

var registerForm = function() {
    var keys = [
        'username',
        'password',
    ];
    var registerPrefix = 'id-input-';
    var form = formFormKeys(keys, registerPrefix);
    return form;
};

var register = function() {
    var form = registerForm();
    var success = function(r) {
        if (r.success) {
            window.location.herf = r.next;
        } else {
            alert(r.message);
        }
    };
    var error = function(err) {

    };
    vip.register(form, success, error);
};

var login = function() {
    var form = loginFrom();
    var success = function(r) {
        log('login, ', r);
        if (r.success) {
            log(r.next);
            window.location.herf = r.next;
        } else {
            alert(r.message);
        }
    };
    var error = function(err) {
        log('login,  ', err);
        alert(err);
    }
    vip.login(form, success, error);
};
var bindActions = function() {
    $('#id-button-register').on('click', function() {
        register();
    });

    $('#id-button-login').on('click', function() {
        login();
    });
};

var __main = function() {
    setup();
    bindActions();
    $('#id-a-login').click();
}

$(document).ready(function() {
    __main();
});
