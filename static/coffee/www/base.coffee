$(document).ready ->
    $('li.treeview').click ->
        $('#main-frame').attr('src', $(this).data('href'))
        $('li.treeview').each ->
            $(this).removeClass('active')

        $(this).addClass('active')
