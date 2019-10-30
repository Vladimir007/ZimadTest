function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie.length) {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = $.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method))
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            let csrftoken = getCookie('csrftoken');
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ajaxError(function () {
    $('#dimmer_of_page').removeClass('active');
    err_notify('Unknown error happened!');
});

window.err_notify = function (message) {
    let notify_opts = {autoHide: false, style: 'bootstrap', className: 'error'};
    $.notify(message, notify_opts);
    return false;
};

window.success_notify = function (message) {
    $.notify(message, {
        autoHide: true,
        autoHideDelay: 2500,
        style: 'bootstrap',
        className: 'success'
    });
    return true;
};

$(document).ready(function () {
    $('.note-popup').popup();
});
