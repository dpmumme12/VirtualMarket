
const data = JSON.parse(document.getElementById('mydata').textContent);
console.log(data)

var times = data.map(function(elem){
    return elem.label;
});

var prices = data.map(function(elem){
    return elem.high;
});

var AvgPrice  = data.at(-1).average;

var min = AvgPrice - AvgPrice/15;
var max = AvgPrice + AvgPrice/15;


GraphData = {
    type: 'line',
    data: {
        labels: times,
        datasets: [{
            label: 'High',
            data: prices,
            backgroundColor: 'transparent',
            borderColor:'blue',
            borderWidth: 1
        }]
    },
    options: {
        elements:{
            point:{
                radius:0
            }
        },
        scales: {
            y: {
                min: min,
                max: max
            }
        },
        tooltips: {
            mode: 'index',
            intersect: true
         },
         hover: {
            mode: 'index',
            intersect: false
         }
         
    }
};



var ctx = document.getElementById('canvas').getContext('2d');
var myChart = new Chart(ctx, GraphData);

var socket = new WebSocket('ws://localhost:8000/ws/graph/');

socket.onmessage = function(elem){
    var data = JSON.parse(elem.data);

    GraphData.data.datasets[0].data.shift();
    GraphData.data.datasets[0].data.push(data.value);

    myChart.update();
}