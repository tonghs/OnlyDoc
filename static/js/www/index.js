// Generated by CoffeeScript 1.9.3
(function() {
  var add_vue, list_vue, mgr_vue, refresh_menu;

  refresh_menu = function() {
    return $.ajax({
      url: '/j/doc/list',
      method: 'GET',
      success: function(r) {
        list_vue.li = r.li;
        mgr_vue.li = r.li;
        if (r.li.length === 0) {
          $('#guid-wrapper').css('display', 'block');
          $('iframe').attr('src', '');
          return loader('hide');
        } else {
          return $('#guid-wrapper').css('display', 'none');
        }
      }
    });
  };

  list_vue = new Vue({
    el: '#main-menu',
    data: {
      li: []
    },
    ready: function() {
      refresh_menu();
      return setTimeout(function() {
        var e;
        e = $('li.treeview')[0];
        if (e) {
          e.click();
          $('iframe').attr('src', $('li.treeview').children('a').attr('href'));
          return loader('hide');
        }
      }, 500);
    },
    methods: {
      active: function(e) {
        loader();
        $('li.treeview').each(function() {
          return $(this).removeClass('active');
        });
        return e.currentTarget.setAttribute('class', 'treeview active');
      }
    }
  });

  add_vue = new Vue({
    el: '#addition-form',
    data: {
      icon: 'book',
      name: '',
      url: ''
    },
    methods: {
      submit: function() {
        return $._ajax({
          url: '/j/doc',
          method: 'POST',
          data: add_vue.$data,
          success: function() {
            refresh_menu();
            add_vue.icon = 'book';
            add_vue.name = '';
            add_vue.url = '';
            return $('.addition-modal').modal('hide');
          }
        });
      }
    }
  });

  mgr_vue = new Vue({
    el: '#doc-list',
    data: {
      li: []
    },
    methods: {
      rm: function(id) {
        return BootstrapDialog.confirm({
          title: '确认',
          message: '确定删除吗？',
          type: BootstrapDialog.TYPE_WARNING,
          btnCancelLabel: '取消',
          btnOKLabel: '确定',
          callback: function(result) {
            if (result) {
              return $._ajax({
                url: '/j/doc',
                method: 'DELETE',
                data: {
                  id: id
                },
                success: function() {
                  return refresh_menu();
                }
              });
            }
          }
        });
      }
    }
  });

}).call(this);
