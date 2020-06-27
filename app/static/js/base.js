(function () {
    url = window.location.pathname
    if (url == '/equipment'){
        $('#equipment').addClass('linking')
    }
    if (url == '/'){
        $('#user').addClass('linking')
    }
    if (url== '/equipment/data'){
        $('#equ_data').addClass('linking')
    }
    if (url == '/my/wish'){
        $('#wishes').addClass('linking')
    }
    if (url == '/pending'){
        $('#pending').addClass('linking')
    }
})()