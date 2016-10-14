refresh_menu = ->
    $.ajax({
        url: '/j/doc/list'
        method: 'GET'
        success: (r)->
            list_vue.li = r.li
            mgr_vue.li = r.li

            if r.li.length == 0
                $('#guid-wrapper').css('display', 'block')
                $('iframe').attr('src', '')
                loader('hide')
            else
                $('#guid-wrapper').css('display', 'none')
    })

list_vue = new Vue({
    el: '#main-menu'
    data: {
        li: []
    }
    ready: ->
        refresh_menu()
        setTimeout( ->
            e = $('li.treeview')[0]
            if e
                e.click()
                $('iframe').attr('src', $('li.treeview').children('a').attr('href'))
                loader('hide')
        ,500)

    methods: {
        active: (e)->
            loader()
            $('li.treeview').each ->
                $(this).removeClass('active')

            e.currentTarget.setAttribute('class', 'treeview active')
        
    }
})


add_vue = new Vue({
    el: '#addition-form'
    data: {
        icon: 'book'
        name: ''
        url: ''
    }

    methods: {
        submit: ->
            $._ajax({
                url: '/j/doc'
                method: 'POST'
                data: add_vue.$data
                success: ->
                    refresh_menu()
                    add_vue.icon = 'book'
                    add_vue.name = ''
                    add_vue.url = ''
                    $('.addition-modal').modal('hide')
            })
    }
})

mgr_vue = new Vue({
    el: '#doc-list'
    data: {
        li: []
    }
    methods: {
        rm: (id)->
            BootstrapDialog.confirm(
                title: '确认'
                message: '确定删除吗？'
                type: BootstrapDialog.TYPE_WARNING
                btnCancelLabel: '取消'
                btnOKLabel: '确定'
                callback: (result)->
                    if result
                        $._ajax({
                            url: '/j/doc'
                            method: 'DELETE'
                            data: {id: id}
                            success: ->
                                refresh_menu()
                        })
            )
    }
})
