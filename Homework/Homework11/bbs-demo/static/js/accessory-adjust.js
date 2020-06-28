// smartly adjust sidebar

$(function () {
    let sidebar = $('#sidebar');
    let userSidebar = $('#userSidebar');
    // hide or show sidebar according to size of mainContent and sideContent
    function adjustSidebar() {
        let h1 = sidebar.length === 1 ? sidebar.height() : 0;
        let h2 = userSidebar.length === 1 ? userSidebar.height() : 0;
        if ($('#mainContent').height() <= h1 + h2 + 40) {
            sidebar.hide();
            console.log('hide');
        } else {
            sidebar.show();
            console.log('hide');
        }
    }

    adjustSidebar();
    window.adjustSidebar = adjustSidebar;
});
