// smartly adjust sidebar

$(function () {
    let sidebar = $('#sidebar');
    // hide or show sidebar according to size of mainContent and sideContent
    function adjustSidebar() {
        if ($('#mainContent').height() <= sidebar.height() + $('#userSidebar').height() + 40) {
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
