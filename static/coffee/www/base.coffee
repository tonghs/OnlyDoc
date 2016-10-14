setFrameSize = ->
     $('iframe#main-frame').height($('.content-wrapper').height())

loader = (e)->
    if e == 'hide'
        $('.overlay').css('display', 'none')
    else
        $('.overlay').css('display', '')


$(document).ready ->
    $('a.menu').click ->
        loader()
        $('#main-frame').attr('src', $(this).data('href'))
        $('li.treeview').each ->
            $(this).removeClass('active')

        treeview = $(this).parents('li')
        if treeview
            treeview.addClass('active')

    setFrameSize()

    $(window).resize ->
        setFrameSize()


    $('iframe#main-frame').load ->
        loader('hide')

