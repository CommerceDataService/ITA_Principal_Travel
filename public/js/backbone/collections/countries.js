App.Collections.Countries = Backbone.Collection.extend({
  url:'../../../db/principal_travel.json',
  model: App.Models.Country
})
