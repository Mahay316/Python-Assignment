// 用户验证的功能，登录、注册、注销等

$(function () {
    const inputAccount = $('#inputAccount');
    const inputPassword = $('#inputPassword');
    const loginBtn = $('#loginBtn');
    // 初始化登录框提示信息
    inputAccount.popover({
        content: '用户名不能为空',
        placement: 'top',
        trigger: 'manual',
    });
    inputAccount.focus(function () {
        inputAccount.popover('hide');
    });

    inputPassword.popover({
        content: '密码不能为空',
        placement: 'top',
        trigger: 'manual',
    });
    inputPassword.focus(function () {
        inputPassword.popover('hide');
    });

    // login button event listener
    loginBtn.click(function () {
        loginBtn.attr('disabled', true);
        loginBtn.popover('hide');

        // 数据校验
        let username = $.trim(inputAccount.val());
        let password = $.trim(inputPassword.val());
        if (username.length === 0) {
            inputAccount.popover('show');
            $('.popover').removeClass('popover-success popover-success-left')
                .removeClass('popover-danger-left')
                .addClass('popover-danger popover-danger-top');
            loginBtn.removeAttr('disabled');

            return false;
        }
        if (password.length === 0) {
            inputPassword.popover('show');
            $('.popover').removeClass('popover-success popover-success-left')
                .removeClass('popover-danger-left')
                .addClass('popover-danger popover-danger-top');
            loginBtn.removeAttr('disabled');

            return false;
        }

        // encrypt password with MD5
        password = hex_md5(password);
        $.ajax({
            url: '/login',
            method: 'post',
            data: {
                'username': username,
                'password': password,
                'auto_login': $('#remember').prop('checked')
            },
            success: function (data) {
                if (data === 'success') {
                    loginBtn.popover('dispose').popover({
                        offset: '0,10',
                        content: '登陆成功',
                        placement: 'left',
                        trigger: 'manual'
                    });
                    loginBtn.popover('show');
                    $('.popover').removeClass('popover-danger popover-danger-top')
                        .addClass('popover-success popover-success-left');
                    // 提示成功后刷新页面
                    setTimeout(function () {
                        const from_url = $('#from');
                        if (from_url.length > 0) {
                            // redirect to original page when complete
                            location.href = from_url.text();
                        } else {
                            location.reload();
                        }
                    }, 500);
                } else {
                    loginBtn.removeAttr('disabled');
                    loginBtn.popover('dispose').popover({
                        offset: '0,10',
                        content: '用户名或密码错误',
                        placement: 'left',
                        trigger: 'manual'
                    });
                    loginBtn.popover('show');
                    $('.popover').removeClass('popover-danger-top')
                        .addClass('popover-danger popover-danger-left');
                }
            }
        });
    });
});

// register, when complete go back to original page
function doRegister() {
    // prevent clicking register on register page
    if (location.pathname === '/register') {
        location.reload();
    } else {
        location.href = '/register?from=' + location.href;
    }
}

// logout, when complete go back to original page
function doLogout() {
    location.href = '/logout?from=' + location.href;
}
