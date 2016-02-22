App.Views.DetailView = Backbone.View.extend({
  el: '#content',
  initialize: function(){
    console.log('detail view initialized');
    $('#content').empty();
  }
})
