App.Routers.DataExplorer = Backbone.Router.extend({
  initalize: function(){
    console.log('router is initialized')
  },

  routes: {
    "": "index",
    "country": "showCountry",
    "principal": "showPrincipal",
    "overview": "showOverview"
  },

  showCountry: function(){
    App.Views.countryView = new App.Views.CountryView();
  },

  showOverview: function(){
    App.Views.detailView = new App.Views.DetailView();
  }
})
