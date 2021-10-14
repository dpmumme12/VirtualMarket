window.addEventListener('DOMContentLoaded', (event) => {
    setTimeout(DomLoaded, 1000);
  });

const data = JSON.parse(document.getElementById('mydata').textContent);
const UserId = JSON.parse(document.getElementById('Id').textContent);
const symbol = JSON.parse(document.getElementById('symbol').textContent);
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

var socket = new WebSocket(`ws://${window.location.host}/ws/stock/${symbol}/`);

var quote;

socket.onmessage = function(elem){
    var data = JSON.parse(elem.data);
    quote = data.response;

    if (quote.latestPrice >= quote.open) {
        document.getElementById('CurrentPrice').style.color = 'limegreen';
      }
      else {
        document.getElementById('CurrentPrice').style.color = 'red';
      }
 
    document.getElementById('CurrentPrice').innerHTML = quote.latestPrice.toLocaleString('en-US', {
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
    var price = Math.round((quote.latestPrice + Number.EPSILON) * 100) / 100


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
        "Price": price,
        "TransactionType": TransactionType,
        "User_id": UserId
        })
    })
    .then(response => {
        return response.json().then((data) => {
           return {
             data: data,
             status_code: response.status,
           };
        });
     })
    .then(resp => {
        var response_status = resp.status_code;
        
        console.log(resp.data)
    
        if (response_status === 201) {
            if (TransactionType === 'BUY'){
                document.getElementById('alert-wrapper').className = 'alert alert-success alert-dismissible';
                document.getElementById('alert-text').innerHTML = `<i class="bi bi-check-circle-fill" style="padding-right: 10px;"></i> ${shares} shares of ${quote.symbol} purchased successfully.`;
                document.getElementById('alert-wrapper').style.display = 'block';
            }
            else if (TransactionType === 'SELL') {
                document.getElementById('alert-wrapper').className = 'alert alert-success alert-dismissible';
                document.getElementById('alert-text').innerHTML = `<i class="bi bi-check-circle-fill" style="padding-right: 10px;"></i> ${shares} shares of ${quote.symbol} sold successfully.`;
                document.getElementById('alert-wrapper').style.display = 'block';
            }
        }
        else if (response_status === 402) {
            document.getElementById('alert-wrapper').className = 'alert alert-danger alert-dismissible';
            document.getElementById('alert-text').innerHTML = `<i class="bi bi-exclamation-triangle-fill" style="padding-right: 10px;"></i> ${resp.data.error_message}`;
            document.getElementById('alert-wrapper').style.display = 'block';
        }
        else {
            document.getElementById('alert-wrapper').className = 'alert alert-danger alert-dismissible';
            document.getElementById('alert-text').innerHTML = '<i class="bi bi-exclamation-triangle-fill" style="padding-right: 10px;"></i> Oops something has gone wrong.';
            document.getElementById('alert-wrapper').style.display = 'block';
        }

    })
    SumbitButton.disabled = false;
}