$.extend({
    tip: (msg)->
        $('#msg').attr('class', 'alert alert-info')
        $('#msg').css('display', 'block')
        $('#msg').html(msg)

    alert: (msg)->
        $('#msg').attr('class', 'alert alert-danger')
        $('#msg').css('display', 'block')
        $('#msg').html(msg)

    _ajax: (option)->
        target = option.target

        $.ajax({
            method: option.method,
            url: option.url,
            data: option.data,
            type: option.type or 'POST'
            success: (r)->
                $('.err').each ->
                    $(this).removeClass('err')

                if r.result
                    option.success(r)
                else
                    for k, v of r
                        p = $("##{k}").parents("div.form-group")
                        p.addClass('err')

                        msg = v
                        if Array.isArray(v)
                            msg = v[0]
                            if Array.isArray(v[0])
                                msg = v[0][0]
                        p.children('.error-msg').html(msg)

                    if option.fail
                        option.fail()

                if target
                    target.attr('disabled', '')
                    target.removeClass('disabled')

            fail: ->
                if option.fail
                    option.fail()

                if target
                    target.attr('disabled', '')
                    target.removeClass('disabled')
        })
})
