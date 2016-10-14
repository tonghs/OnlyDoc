$(document).ready ->
    $('a.menu').click ->
        $('#main-frame').attr('src', $(this).data('href'))
        $('li.treeview').each ->
            $(this).removeClass('active')

        treeview = $(this).parents('li')
        if treeview
            treeview.addClass('active')
