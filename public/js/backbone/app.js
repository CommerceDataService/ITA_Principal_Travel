App = {
  Models: {},
  Collections: {},
  Views: {},
  Routers : {}
}

$(document).ready(function(){
  App.Routers.dataExplorer = new App.Routers.DataExplorer();
  Backbone.history.start();
})
