(function() {
  $(document).ready(function() {
    var pager, v_add, v_edit, v_list;
    v_add = new Vue({
      el: '#addition-form',
      data: {
        name: '',
        parent: 0,
        top_category: []
      },
      ready: function() {
        var self;
        self = this;
        return $.ajax({
          url: '/j/category/top',
          method: 'GET',
          success: function(r) {
            return self.top_category = r.li;
          }
        });
      },
      methods: {
        submit: function(e) {
          return $._ajax({
            url: '/j/category',
            data: this.$data,
            success: function(r) {
              v_add.name = '';
              v_add.parent = 0;
              $('.addition-modal').modal('hide');
              return $.ajax({
                url: '/j/category/top',
                method: 'GET',
                success: function(r) {
                  return pager(v_list.page);
                }
              });
            }
          });
        }
      }
    });
    pager = function(page) {
      return $.ajax({
        url: '/j/category/list',
        method: 'GET',
        data: {
          page: page
        },
        success: function(r) {
          v_list.$data = r;
          v_add.top_category = r.li;
          return v_edit.top_category = r.li;
        }
      });
    };
    v_edit = new Vue({
      el: '#edition-form',
      data: {
        id: 0,
        name: '',
        parent: 0,
        top_category: []
      },
      ready: function() {
        var self;
        self = this;
        return $.ajax({
          url: '/j/category/top',
          method: 'GET',
          success: function(r) {
            return self.top_category = r.li;
          }
        });
      },
      methods: {
        submit: function() {
          return $._ajax({
            url: '/j/category/edit',
            method: 'POST',
            data: this.$data,
            success: function(r) {
              pager(v_list.page);
              return $('.edition-modal').modal('hide');
            }
          });
        }
      }
    });
    return v_list = new Vue({
      el: '#category-list',
      data: {
        li: [],
        count: 0,
        total_page: 0,
        page: 1
      },
      methods: {
        pager: function(page) {
          return pager(page);
        },
        next: function() {
          return pager(++this.page);
        },
        prev: function() {
          return pager(--this.page);
        },
        add_sub: function(id) {
          return v_add.parent = id;
        },
        edit: function(id) {
          return $.ajax({
            url: '/j/category',
            method: 'GET',
            data: {
              id: id
            },
            success: function(r) {
              v_edit.id = r.id;
              v_edit.name = r.name;
              return v_edit.parent = r.parent;
            }
          });
        },
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
                  url: '/j/category/rm',
                  method: 'POST',
                  data: {
                    id: id
                  },
                  success: function(r) {
                    return pager(this.page);
                  }
                });
              }
            }
          });
        }
      },
      ready: function() {
        return pager(1);
      }
    });
  });

}).call(this);
