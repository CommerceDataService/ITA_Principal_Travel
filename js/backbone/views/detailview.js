App.Views.DetailView = Backbone.View.extend({
  el: '#content',
  initialize: function(){
    console.log('detail view initialized');
    $('#content').empty();
  }
  // render: function(){
  //   var data = {
  //     regions:[
  //       Asia: [{
  //         country: 'Japan',
  //         trips: [{
  //           principal: 'Secretary Pritzker',
  //           length: '4',
  //           cities: ['Tokyo']
  //         },
  //         {
  //           principal: 'Undersecretary ',
  //           length: '5',
  //           cities: ['Tokyo']
  //         }]
  //       },
  //       {
  //         country: 'Kuwait',
  //         trips: [{
  //             principal: 'Secretary Pritzker',
  //             length: '4',
  //             cities: ['Kuwait City']
  //           },
  //           {
  //             principal: 'Undersecretary Something',
  //             length: '5',
  //             cities: ['Kuwait City']
  //           }]
  //       }]
  //     ]
  //
  //   }
  // }
})
