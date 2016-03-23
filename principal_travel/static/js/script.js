$(document).ready(function(){
  $.getJSON('/api/events')
  .done(function(data){
    var countryCount = _.countBy(data, function(country){
      return country.cities_light_country.name
    })
    countryCount = _.pairs(countryCount)

    var color = d3.scale.category20b();
    var svg = d3.select('#country')
    .append('svg')
    .attr('width', '100%')
    .attr('height', '350')

    var rects = svg.selectAll('rect')
    .data(countryCount)
    .enter()
    .append('rect')

    var max = d3.max(countryCount, function(d){
      return d[1];
    })

    var linearScale = d3.scale
    .linear()
    .range([0, 100])
    .domain([0,max])

    rects.attr('x', 0)
    .attr('y', function(d, i){return i*22})
    .attr('height', 20)
    .attr('width', function(d){
      return linearScale(d[1]) + "%"
    })
    .attr('fill', function(d, i){
      return color(i)
    })

    var labels = svg.selectAll('text')
    .data(countryCount)
    .enter()
    .append('text')
    .text(function(d){
      return d[0]+": "+d[1];
    });
    labels
    .attr('x', 5)
    .attr('y', function(d, i){return (i*22)+13})
    .attr("font-family", "sans-serif")
    .attr("font-size", "11px")
    .attr("fill", "white");;

  })

  $.getJSON('/api/trips').done(function(data){

    var sortedTrips = _(data).chain().sortBy(function(trip){
      return start = new Date(trip.start_date)
    }).value()

    _.each(sortedTrips, function(trip){
      var now = new Date();
      var start = new Date(trip.start_date)
      if(start>now){
        var template = Handlebars.compile($('#table').html())
        $('#time-table').append(template(trip))
      }
    })
  })

    var map = L.map('map')
    .setView([33, 50], 2);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
      attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
      maxZoom: 3,
      id: 'noonkay.pfg0o793',
      accessToken: 'pk.eyJ1Ijoibm9vbmtheSIsImEiOiJjaWo4cHhpa2UwMDFidXhseDg3eGMwejBuIn0.tBWxkbD9BloELWmccA1UyQ'
    }).addTo(map);

    futureMarkers = L.layerGroup([]).addTo(map);
    monthMarkers = L.layerGroup([]).addTo(map);
    yearMarkers = L.layerGroup([]).addTo(map);
    oldMarkers = L.layerGroup([]).addTo(map);

    $.getJSON('/api/trips').done(function(data){
      var today = new Date();
      var monthAgo = new Date().setDate(today.getDate()-30)
      var yearAgo = new Date().setDate(today.getDate()-365)
      var template = Handlebars.compile($('#popup').html());
      _.each(data, function(trip){
        var start = new Date(trip.start_date)
        _.each(trip.events, function(event){
          var marker = L.marker([event.cities_light_city.latitude, event.cities_light_city.longitude]).bindPopup(template(event));
          if(start >= today){
            futureMarkers.addLayer(marker);
          } else if (start<today && start>= monthAgo) {
            monthMarkers.addLayer(marker);
          } else if (start<monthAgo && start >= yearAgo) {
            yearMarkers.addLayer(marker);
          } else{
            oldMarkers.addLayer(marker);
          }
        })
      })

      $( "input" ).click(function( event ) {
          var layerClicked = window[event.target.value];
              console.log(window)
              console.log(layerClicked)
              if (map.hasLayer(layerClicked)) {
                  map.removeLayer(layerClicked);
              }
              else{
                  map.addLayer(layerClicked);
              } ;
      });
    })
})
