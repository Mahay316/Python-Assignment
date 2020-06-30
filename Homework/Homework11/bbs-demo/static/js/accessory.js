// 实现一些常用特效

$(function () {
    // 侧边栏跟随
    const topPadding = 15;
    const sidebar = $("#sidebar");
    const offset = sidebar.offset();
    const documentHeight = $(document).height();

    if (sidebar.length > 0) {
        $(window).scroll(function () {
            const sideBarHeight = sidebar.height();
            if ($(window).scrollTop() > offset.top) {
                let newPosition = ($(window).scrollTop() - offset.top) + topPadding;
                const maxPosition = documentHeight - (sideBarHeight + 368);
                if (newPosition > maxPosition) {
                    newPosition = maxPosition;
                }
                sidebar.stop().animate({
                    marginTop: newPosition
                });
            } else {
                sidebar.stop().animate({
                    marginTop: 15
                });
            }
        });
    }

    // 用户中心下拉菜单
    $('#loginCenter').hover(
        function () {
            $('.menu .userControl').css('display', 'block');
        }, function () {
            $('.menu .userControl').css('display', 'none');
        }
    );
});

// 回到页面顶部
function scrollToTop() {
    document.body.scrollTop = document.documentElement.scrollTop = 0;
}
