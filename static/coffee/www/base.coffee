setFrameSize = ->
     $('iframe#main-frame').height($('.content-wrapper').height())

window.loader = (e)->
    if e == 'hide'
        $('.overlay').css('display', 'none')
    else
        $('.overlay').css('display', '')


$(document).ready ->
    setFrameSize()

    $(window).resize ->
        setFrameSize()


    $('iframe#main-frame').load ->
        loader('hide')

    $('.overlay').click ->
        loader('hide')
