// 实现一些常用特效

$(function () {
    // 侧边栏跟随
    const topPadding = 15;
    const sidebar = $("#sidebar");
    const offset = sidebar.offset();
    const documentHeight = $(document).height();
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
});

// 回到页面顶部
function scrollToTop() {
    document.body.scrollTop = document.documentElement.scrollTop = 0;
}