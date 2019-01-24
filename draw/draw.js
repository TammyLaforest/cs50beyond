


        const svg = d3.select('#svg');
        let drawing = false;
        // document.getElementById('my-svg-rect').setAttribute('fill', 'black')
        // let colorchoice = blue;

        function draw_point() {
            if (!drawing)
                return;

            const coords = d3.mouse(this);
            // circle.data([32, 57, 112]);

            svg.append('circle')
               .attr('cx', coords[0])
               .attr('cy', coords[1])
               
               // Size of dot
               .attr('r', 10)
               
               // Color of dot
               .style('fill', 'blue')
               // .style('stroke', 'blue')
               // .style('fill-opacity', '.5')
                // .style("fill", () => { this.setAttribute('fill', 'black'));

        };

      function myFunction() {
        var x = document.getElementById("mySelect").selectedIndex;
        let color = (document.getElementsByTagName("option")[x].value);
        svg.style.fill = color;
      }

        svg.on('mousedown', () => {
            drawing = true;
        });

        svg.on('mouseup', () => {
            drawing = false;
        });

        svg.on('mousemove', draw_point);

       //  svg.select('#slide3 #singleButton')
       // .text('POWER button!')
       // .classed('btn-primary', true)
       // .style('font-weight', 'bold')
       // .on('click', function() {
       //  d3.select(this)
       //   .text('Dumb button')
       //   .classed('blueish', false)
       //   .style('font-weight:normal');
       // });





