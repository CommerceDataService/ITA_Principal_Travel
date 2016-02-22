App.Views.CountryView = Backbone.View.extend({
  el: '#content',

  initialize: function(){
    console.log('country view is initialized');
    this.box1Template = Handlebars.compile($('#template1').html());
    this.box2Template = Handlebars.compile($('#template2').html());
    this.box3Template = Handlebars.compile($('#template3').html());
    this.renderAll();
    this.renderViz();
  },

  renderAll: function(){
    this.$el.append(this.box1Template({title: "Countries Visited", description:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."}));
    this.$el.append(this.box2Template({title: "Time Spent In Countries", description:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."}));
    this.$el.append(this.box3Template({title: "Country Related Visualization", description:"Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."}));
  },

  renderViz: function(){
    var data = [{country: "Sweden", number: 4}, {country: "Norway", number: 8}, {country: "Denmark", number: 15}];
      var rects = d3
      .select('#box1')
      .selectAll('rect')
      .data(data)
      .enter().append('rect')
      // var max = d3.max(data.number)
      var linearScale = d3.scale.linear().range([0, 300]).domain([0,15])
      rects.attr('x', 0).attr('y', function(d, i){return i*22}).attr('height', 20).attr('width', function(d){
        return linearScale(d.number)
      })
      rects.attr('fill', function(d, i){
        return "rgba(0, 0, 0," + d.number*0.04+")"
      })
      var labels = d3
      .select('#box1')
      .selectAll('text')
      .data(data)
      .enter()
      .append('text')
      .text(function(d){
        return d.country
      });
      labels
      .attr('x', 0)
      .attr('y', function(d, i){return (i*22)+15})
      .attr("font-family", "sans-serif")
      .attr("font-size", "12px")
      .attr("fill", "white");;
  }
})
