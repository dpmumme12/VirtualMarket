const data = JSON.parse(document.getElementById('mydata').textContent);

var times = data.map(function(elem){
    return elem.label;
});
var prices = data.map(function(elem){
    return elem.high;
});

if (data.at(0).open > data.at(-1).high){
    LineColor = 'red'
}
else{
    LineColor = 'limegreen'
}

GraphData = {
    type: 'line',
    data: {
        labels: times,
        datasets: [{
            
            data: prices,
            backgroundColor: 'transparent',
            borderColor:LineColor,
            borderWidth: 1.5
        }]
    },
    options: {
        plugins: {
            legend: {
                display: false 
            },
        },
        elements:{
            point:{
                radius:0
            }
        },
        scales: {
            x: {
                grid: {display:false},
                ticks: {
                    display: true,
                    autoSkip: true,
                    maxTicksLimit: 10
                }
              },
              y: {
              }  
        },
        tooltips: {
            mode: 'index',
            intersect: false,
            enabled: false
         },
         hover: {
            mode: 'index',
            intersect: false
         },
        responsive: true,
        maintainAspectRatio: false,
        animation: false
    }
};

var ctx = document.getElementById('canvas').getContext('2d');
var myChart = new Chart(ctx, GraphData);

var socket = new WebSocket('ws://localhost:8000/ws/stockgraph/');

socket.onmessage = function(elem){
    var num = JSON.parse(elem.data)
    console.log(num.value)
}