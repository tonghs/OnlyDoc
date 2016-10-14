new Vue(
    el: '#login-form'
    data: {
        user_name: '',
        password: ''
    }
    methods: {
        submit: ->
            if this.user_name and this.password
                $._ajax(
                    url: '/j/login'
                    method: 'POST'
                    data: this.$data
                    success: ->
                        window.location.href = '/'
                )
    }
)
