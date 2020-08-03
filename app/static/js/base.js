(function () {
    url = window.location.pathname
    if (url == '/equipment/equipment'){
        $('#equipment').addClass('linking');
    }
    if (url == '/equipment/'){
        $('#user').addClass('linking');
    }
    if (url == '/'){
        $('#user').addClass('linking');
    }
    if (url== '/equipment/data/temperature'){
        $('#temperature').addClass('linking');
    }
    if (url== '/equipment/data/switch'){
        $('#switch').addClass('linking');
    }
    if (url== '/equipment/data/humidity'){
        $('#humidity').addClass('linking');
    }
    var t=/^\/equipment\/data\/temperature\/[0-9]*$/;
    var s=/^\/equipment\/data\/switch\/[0-9]*$/;
    var h=/^\/equipment\/data\/humidity\/[0-9]*$/;
    if (t.test(url)) {
        $('#temperature').addClass('linking');
    }
    if (s.test(url)) {
        $('#switch').addClass('linking');
    }
    if (h.test(url)) {
        $('#humidity').addClass('linking');
    }

})();