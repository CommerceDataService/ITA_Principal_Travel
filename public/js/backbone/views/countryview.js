App.Views.CountryView = Backbone.View.extend({
  el: '#content',

  initialize: function(){
    $('#content').empty();
    this.vizTemplate = Handlebars.compile($('#viz-template').html());

    this.renderAll();
    this.renderViz();
    this.listenTo(this.collection, 'sync', this.renderViz)
  },

  renderAll: function(){
    this.$el.append(this.vizTemplate({title: "Countries Ranked by the Number of Visits"}));
    this.$el.append(this.vizTemplate({title: "Days Spent In Each Country"}));
  },

  renderViz: function(){
    var allTrips = this.collection;

    var allCountries = _.uniq(allTrips.pluck('country'))
    var data = []
    _.each(allCountries, function(thisCountry){
      var temp = allTrips.where({'country': thisCountry})
      data.push(temp)
    })
    // data.sort(function(a, b){
    //   return b.length - a.length;
    // })
    var color = d3.scale.category20b();
    var charts =d3.selectAll('.chart')
    var svg = d3.select(charts[0][0])
    .append('svg')
    .attr('width', '100%')
    .attr('height', '350')

    var rects = svg.selectAll('rect')
    .data(data)
    .enter().append('rect')
    var max = d3.max(data, function(d){
      return d.length;
    })

    var linearScale = d3.scale
    .linear()
    .range([0, 100])
    .domain([0,max])

    rects.attr('x', 0)
    .attr('y', function(d, i){return i*22})
    .attr('height', 20)
    .attr('width', function(d){
      return linearScale(d.length) + "%"
    })
    .attr('fill', function(d, i){
      return color(i)
    })

    var labels = svg.selectAll('text')
    .data(allCountries)
    .enter()
    .append('text')
    .text(function(d){
      return d;
    });
    labels
    .attr('x', 5)
    .attr('y', function(d, i){return (i*22)+13})
    .attr("font-family", "sans-serif")
    .attr("font-size", "11px")
    .attr("fill", "white");;
    ///begin second visualization
    var tripLengthData = [];
    _.each(data, function(trips){
      var sum = 0;
      var country;
      _.each(trips, function(trip){
        var start = new Date(trip.attributes.start_date)
        var end = new Date(trip.attributes.end_date)
        var millisecondsPerDay = 24 * 60 * 60 * 1000;
        sum += Math.abs(end-start)/millisecondsPerDay
        country = trip.attributes.country
      })
      tripLengthData.push({'country': country, 'time': sum })
    })


    var width = 400,
    height = 300,
    radius = Math.min(width, height) / 2;

    svg = d3.select(charts[0][1])
      .append('svg')
      .attr("width", width)
      .attr("height", height)
      .append("g")
      .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

    var arc = d3.svg.arc()
    .outerRadius(radius - 10)
    // .innerRadius(0);
    var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) {
      return d.time;
     })

    var path = svg.selectAll('path')
      .data(pie(tripLengthData))
      .enter()
      .append('path')
      .attr('d', arc)
      .attr('fill', function(d,i){
        return color(i)
      })
  },


})
