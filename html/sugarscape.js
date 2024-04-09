const width = 500;  // Customize as needed
const height = 500;
const cellSize = 30; // Adjust for desired cell dimensions

const svg = d3.select("body") // Assumes you're appending to the body
  .append("svg")
  .attr("width", width)
  .attr("height", height);

d3.json("data/onesurface.json")
  .then (data => {
    // Create grid cells
    svg.selectAll("rect")
       .data(data) 
       .enter()
       .append("rect")
       .attr("x", d => d.x * cellSize)
       .attr("y", d => d.y * cellSize)
       .attr("width", cellSize)
       .attr("height", cellSize)
       .attr("stroke", "black")
       .attr("stroke-width", 1); 
  })
