(function() {
  new Vue({
    el: '#addition-form',
    data: {
      name: '',
      parent: 0
    },
    methods: {
      submit: function() {
        return console.log('submit');
      }
    }
  });

}).call(this);
