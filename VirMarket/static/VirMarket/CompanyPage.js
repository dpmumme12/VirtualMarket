const data = JSON.parse(document.getElementById('mydata').textContent);
const UserId = JSON.parse(document.getElementById('Id').textContent);
document.getElementById('BuyButton').checked = true;
var TransactionType = document.getElementById('BuyButton').value;



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

var quote

socket.onmessage = function(elem){
    var data = JSON.parse(elem.data);
    quote = data.response;

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

function RadioGroupToggle(){
    var BuyButton = document.getElementById('BuyButton');
    var SellButton = document.getElementById('SellButton');

    if (BuyButton.checked === true) {
        document.getElementById('SumbitButton').className = 'btn btn-success';
        document.getElementById('SumbitButton').innerHTML = 'BUY';
        TransactionType = BuyButton.value;
    }
    else if (SellButton.checked === true) {
        document.getElementById('SumbitButton').className = 'btn btn-danger';
        document.getElementById('SumbitButton').innerHTML = 'SELL';
        TransactionType = SellButton.value;
    }
}

function AddShare(){
     var num = document.getElementById('SharesInput').value;
     var shares = parseInt(num) + 1;
     document.getElementById('SharesInput').value = shares.toString();
}

function RemoveShare(){
    var num = document.getElementById('SharesInput').value;
    if (parseInt(num) === 0){
        return;
    }
    var shares = parseInt(num) - 1;
    document.getElementById('SharesInput').value = shares.toString();
}

function Transaction(){
    var SumbitButton = document.getElementById("SumbitButton");
    SumbitButton.disabled = true;

    var shares = document.getElementById('SharesInput').value;
    const csrfToken = getCookie('csrftoken');

    fetch('/api/Transactions', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
          },
          mode: 'same-origin',
        body: JSON.stringify({
        "Symbol": quote.symbol,
        "Name": quote.companyName,
        "Shares": parseInt(shares),
        "Price": quote.iexRealtimePrice,
        "TransactionType": TransactionType,
        "User_id": UserId
        })
    })
    .then(resp => {
        console.log(resp.json());
    })
    SumbitButton.disabled = false;

}
