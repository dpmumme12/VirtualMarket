import {GetGraphData, formatAMPM} from './functions.js';

const data = JSON.parse(document.getElementById('mydata').textContent);
const id = JSON.parse(document.getElementById('key').textContent);
const TotalAccountBalance = document.getElementById('TotalAccountBalance');

var times = [formatAMPM(new Date)];
var prices =  [data];
var LineColor = 'limegreen'
var CurrentLabelToPop = times[0]


var GraphData = GetGraphData(times, prices, LineColor);

var ctx = document.getElementById('canvas').getContext('2d');
var myChart = new Chart(ctx, GraphData);


fetch('/api/Stocks')
.then(response => response.json())
.then(data => {
    var stocks = data
    for (let stock of stocks){
        document.getElementById('StocksTableBody').innerHTML += `
        <tr style="position: relative;">
            <td>${stock.Symbol}</td>
            <td>${stock.Shares}</td>
            <td id='${stock.Symbol.toUpperCase()}-price'></td>
            <td><a href="Stock/${stock.Symbol}" class="stretched-link"></a></td>
        </tr>`
    };
});



var socket = new WebSocket(`ws://${window.location.host}/ws/UserTotalAccountBalance/${id}/`);

socket.onmessage = function(elem){
    var resp = JSON.parse(elem.data);
    var stocks = resp.stocks;
    
    TotalAccountBalance.innerHTML = resp.TotalAccountBalance.toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD',
      });
      
      var new_prices = myChart.data.datasets[0].data;
      var new_labels = myChart.data.labels;

      if (new_prices.length >= 70){
          for(i=0; i < new_labels.length; i++){
              if(new_labels[i] === CurrentLabelToPop){
                  if(new_labels[i+1] === CurrentLabelToPop){
                    CurrentLabelToPop = new_labels[i+1];
                    new_prices.splice(i+1,1);
                    new_labels.splice(i+1,1);
                    break;
                  }
              }
              else{
                NewLabelToPop = new_labels[i+1]
                if(NewLabelToPop !== CurrentLabelToPop){
                    CurrentLabelToPop = NewLabelToPop
                }
              };
          }
          new_prices.push(resp.TotalAccountBalance);
          new_labels.push(formatAMPM(new Date));
      }
      else {
          new_prices.push(resp.TotalAccountBalance);
          new_labels.push(formatAMPM(new Date));
      };

      if (resp.TotalAccountBalance >= new_prices[0]){
        myChart.data.datasets[0].borderColor = 'limegreen';
      }
      else {
        myChart.data.datasets[0].borderColor = 'red';
      };

      myChart.data.datasets[0].data = new_prices;
      myChart.data.labels = new_labels;

      myChart.update();
     
      
      for(let stock in stocks) {
          if (stocks[stock].quote.latestPrice >= stocks[stock].quote.open) {
            document.getElementById(`${stock}-price`).style.color = 'limegreen';
          }
          else {
            document.getElementById(`${stock}-price`).style.color = 'red';
          }
          document.getElementById(`${stock}-price`).innerHTML = stocks[stock].quote.latestPrice.toLocaleString('en-US', {
            style: 'currency',
            currency: 'USD',
          });;
      }  
}


var typingTimer;
var doneTypingInterval = 300;

function SearchKeyUp() {
    clearTimeout(typingTimer);
    var typingTimer = setTimeout(SearchQuery, doneTypingInterval);
}

function SearchKeyDown() {
    clearTimeout(typingTimer);
}

function SearchOnBlur(){
    document.getElementById('MyDropdown').innerHTML = '';
    document.getElementById('SearchBar').value = '';
}


async function SearchQuery() {
    document.getElementById('MyDropdown').innerHTML = '';

    var query = document.getElementById('SearchBar').value.toUpperCase();

    if (query === ''){
        return
    }

    await fetch(`https://finnhub.io/api/v1/search?q=${query}&token=c5bmkjqad3ifmvj0nc10`)
    .then(response => response.json())
    .then(data => {
        Stocks = data.result
        Stocks = Stocks.filter(function(elem) {
            return !elem.symbol.includes('.') & !elem.symbol.includes(':');
        });

        for(i=0; i< 10; i++){
        document.getElementById('MyDropdown').innerHTML += `<a href="${'/Stock/' + Stocks[i].symbol}" class="Dropdown-Item">${Stocks[i].symbol}<p class="SearchDescription">${Stocks[i].description}</p></a>`;
        }
    });
}










