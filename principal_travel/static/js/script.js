var compare = function(a, b) {
    if (a[1] === b[1]) {
        return 0;
    }
    else {
        return (a[1] > b[1]) ? -1 : 1;
    }
}

var drawBarGraph = function(data){
  var color = d3.scale.category10();
  var svg = d3.select('#chart')
  .append('svg')
  .attr('width', '100%')
  .attr('height', '300')


  var tip = d3.tip()
    .attr("class", "d3-tip")
    .offset([-10, 0])
    .html(function(d) {
    return "<strong>"+d[0]+"</strong> <span style='color:red'>" + d[1] + "</span>";
  })

  var max = d3.max(data, function(d){
    return d[1];
  })

  var linearScale = d3.scale
  .linear()
  .range([0, 100])
  .domain([0,max])

  svg.call(tip);

  var rects = svg.selectAll('rect')
  .data(data)
  .enter()
  .append('rect')

  rects.attr('x', 0)
  .attr('fill', function(d, i){
    return color(i)
  })
  .attr('y', function(d, i){return i*32})
  .attr('height', 20)
  .attr('width', 0)
  .transition()
  .duration(1000)
  .ease('linear')
  .attr('width', function(d){
    return linearScale(d[1]) + "%"
  })

  rects.on('mouseover', tip.show)
  .on('mouseout', tip.hide)



  var labels = svg.selectAll('text')
  .data(data)
  .enter()
  .append('text')
  .text(function(d){
    return d[0]+": "+d[1];
  });

  labels
  .attr('x', 10)
  .attr('y', function(d, i){return (i*32)+17})
  .attr("font-family", "sans-serif")
  .attr("font-size", "11px")
  .attr("fill", "white");
}

var pairSortSlice = function(object){
  var array = _.pairs(object);
  array.sort(compare);
  return array.slice(0,9)
}

var renderTable = function(tripData){
  var template = Handlebars.compile($('#table').html())
  var sortedTrips = _(tripData).chain().sortBy(function(trip){
    return start = new Date(trip.start_date)
  }).value()

  var i = sortedTrips.length
  _.each(sortedTrips, function(trip){
    var now = new Date();
    var start = new Date(trip.start_date)
    if(start>=now){
      $('#upcoming').append(template(trip))
      i--;
    }
  })
  var j = sortedTrips.length - ((sortedTrips.length - i)*2)
  var recentTrips = sortedTrips.slice(j, i)
  recentTrips.reverse();
  _.each(recentTrips, function(trip){

    $('#recent').append(template(trip))
  })
}

var renderMap = function(tripData){
  var map = L.map('map')
  .setView([33, -8], 2);

  L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    maxZoom: 3,
    id: 'noonkay.f59d9773',
    // id: 'noonkay.pfg0o793',
    accessToken: 'pk.eyJ1Ijoibm9vbmtheSIsImEiOiJjaWo4cHhpa2UwMDFidXhseDg3eGMwejBuIn0.tBWxkbD9BloELWmccA1UyQ',
    noWrap: true,
    minZoom: 2,
    maxZoom: 4
  }).addTo(map);

  futureMarkers = L.layerGroup([]).addTo(map);
  monthMarkers = L.layerGroup([]).addTo(map);
  yearMarkers = L.layerGroup([]).addTo(map);
  allPastMarkers = L.layerGroup([]).addTo(map);

  var today = new Date();
  var monthAgo = new Date().setDate(today.getDate()-30)
  var yearAgo = new Date().setDate(today.getDate()-365)
  var template = Handlebars.compile($('#popup').html());
  _.each(tripData, function(trip){
    var start = new Date(trip.start_date)
    _.each(trip.events, function(event){
      var marker = L.marker([event.cities_light_city.latitude, event.cities_light_city.longitude]).bindPopup(template(event));
      if(start >= today){
        futureMarkers.addLayer(marker);
      }else {
        if (start<today && start>= monthAgo) {
          monthMarkers.addLayer(marker);
        }
        if (start<today && start >= yearAgo) {
          yearMarkers.addLayer(marker);
        }
        allPastMarkers.addLayer(marker);
      }
    })
  })

  $( "input" ).on('click', function( event ) {
    var layerClicked = window[event.target.value];
    if (map.hasLayer(layerClicked)) {
      map.removeLayer(layerClicked);
    } else {
      map.addLayer(layerClicked);
    }
  })
}

var renderChart = function(tripData, eventData){
  var principalCount = _.countBy(tripData, function(trip){
    return trip.principal.title;
  })
  var countryCount = _.countBy(eventData, function(event){
    return event.cities_light_country.name;
  })
  var eventTypeCount = _.countBy(eventData, function(event){
    return event.event_type.name;
  })

  drawBarGraph(pairSortSlice(countryCount));
  $("#options").on('change', function(event){
    if (this.value == "country"){
      $('#chart').empty().append('<h3>Top Destinations</h3>')
      drawBarGraph(pairSortSlice(countryCount));
    } else if (this.value == "principal"){
      $('#chart').empty().append('<h3>Top Travelers</h3>')
      drawBarGraph(pairSortSlice(principalCount));
    } else if (this.value == "eventType"){
      $('#chart').empty().append('<h3>Top Event Types</h3>')
      drawBarGraph(pairSortSlice(eventTypeCount));
    }
  })
}

$(document).ready(function(){
  var tripData, eventData;
  $.getJSON('/api/events')
  .done(function(data){
    eventData = data;
    $.getJSON('/api/trips')
    .done(function(data){
      tripData = data;
      renderTable(tripData);
      renderChart(tripData, eventData);
      renderMap(tripData);
    })
  })
})
