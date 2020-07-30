(function () {
    url = window.location.pathname
    if (url == '/equipment/equipment'){
        $('#equipment').addClass('linking')
    }
    if (url == '/equipment/'){
        $('#user').addClass('linking')
    }
    if (url == '/'){
        $('#user').addClass('linking')
    }
    if (url== '/equipment/data/temperature'){
        $('#temperature').addClass('linking')
    }
    if (url== '/equipment/data/swich'){
        $('#swich').addClass('linking')
    }
    if (url== '/equipment/data/humidity'){
        $('#humidity').addClass('linking')
    }
})()