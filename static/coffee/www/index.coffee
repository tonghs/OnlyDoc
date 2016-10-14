refresh_menu = ->
    $.ajax({
        url: '/j/doc/list'
        method: 'GET'
        success: (r)->
            list_vue.li = r.li
    })

list_vue = new Vue({
    el: '#main-menu'
    data: {
        li: []
    }
    ready: ->
        refresh_menu()

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
                method: 'post'
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
