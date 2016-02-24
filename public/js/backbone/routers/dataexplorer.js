App.Routers.DataExplorer = Backbone.Router.extend({
  initialize: function(){
    App.Models.country = new App.Models.Country();
    App.Collections.countries = new App.Collections.Countries();
    console.log(App.Collections.countries)
    App.Collections.countries.fetch();
  },

  routes: {
    "": "index",
    "location": "showCountry",
    "principal": "showPrincipal",
    "overview": "showOverview",
    "time": "showTime"
  },

  index: function(){
    App.Views.homeView = new App.Views.HomeView();
  },

  showCountry: function(){
    App.Views.countryView = new App.Views.CountryView({collection: App.Collections.countries});
  },

  showOverview: function(){
    App.Views.detailView = new App.Views.DetailView();
  },

  showPrincipal: function(){
    App.Views.principalView = new App.Views.PrincipalView();
  },

  showTime: function(){
    App.Views.timeView = new App.Views.TimeView({collection: App.Collections.countries});
  }
})
