App.Views.HomeView = Backbone.View.extend({
  el: '#content',

  initialize: function(){
    $('#content').empty();
    this.template = Handlebars.compile($('#welcome').html())
    this.render();
  },

  render: function(){
    this.$el.append(this.template)
  }
})
