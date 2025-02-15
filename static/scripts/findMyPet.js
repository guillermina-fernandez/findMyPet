$(document).ready(function() {
    $('input:not([type="checkbox"]):not(.plain-obj)').addClass('form-control form-control-sm');
    $('select:not(.plain-obj)').addClass('form-select form-select-sm');
    $('label').addClass('fw-bold');
});

function show_password(password_id, icon_id) {
    let password = document.getElementById(password_id);
    let toggle_icon = document.getElementById(icon_id);

    if (password.type === 'password') {
        password.type = 'text';
        toggle_icon.classList.remove('bi-eye-fill');
        toggle_icon.classList.add('bi-eye-slash-fill');
    } else {
        password.type = 'password';
        toggle_icon.classList.remove('bi-eye-slash-fill');
        toggle_icon.classList.add('bi-eye-fill');
    };
};


document.addEventListener('DOMContentLoaded', function (){
    document.querySelectorAll('form').forEach(function (form){
        form.addEventListener('submit', function (event) {
            
            if (!event.defaultPrevented) {
                showLoading();
                window.onfocus = function(){
                    hideLoading();
                    window.onfocus = null;
                }
            } else {
                hideLoading();
            };
        });
    });
});


function showLoading(){
    document.getElementById('loading').style.display = 'flex';
};

function hideLoading(){
    document.getElementById('loading').style.display = 'none';
};


document.querySelectorAll('.modal').forEach(function(modal) {
    modal.addEventListener('shown.bs.modal', function () {
        let elements = modal.querySelectorAll('input, select');
        for (let i = 0; i < elements.length; i++) {
            let firstInput = elements[i];
            if (firstInput && !firstInput.hidden && firstInput.type !== 'hidden') {
                firstInput.focus();
                break;
            }
        }
    });
});


function reset_form(form_id) {
    document.getElementById(form_id).reset();
    isFormDirty = false;
};