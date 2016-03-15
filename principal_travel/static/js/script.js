$(document).ready(function(){
  $.getJSON('/api/events')
  .done(function(data){
    var countryCount = _.countBy(data, function(country){
      return country.cities_light_country.name
    })
    countryCount = _.pairs(countryCount)

    var color = d3.scale.category20b();
    var svg = d3.select('#dashboard')
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
    console.log(max)

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
      return d[0];
    });
    labels
    .attr('x', 5)
    .attr('y', function(d, i){return (i*22)+13})
    .attr("font-family", "sans-serif")
    .attr("font-size", "11px")
    .attr("fill", "white");;

  })

})
