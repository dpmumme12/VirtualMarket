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

var GraphData = GetGraphData(times, prices, LineColor);

var ctx = document.getElementById('canvas').getContext('2d');
var myChart = new Chart(ctx, GraphData);

var socket = new WebSocket('ws://localhost:8000/ws/stockgraph/');

socket.onmessage = function(elem){
    var data = JSON.parse(elem.data);
    var quote = data.response;

    if (quote.iexRealtimePrice >= quote.open) {
        document.getElementById('CurrentPrice').style.color = 'limegreen';
      }
      else {
        document.getElementById('CurrentPrice').style.color = 'red';
      }
 
    document.getElementById('CurrentPrice').innerHTML = quote.iexRealtimePrice.toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD',
      });

}
