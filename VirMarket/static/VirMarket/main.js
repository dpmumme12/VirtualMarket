const data = JSON.parse(document.getElementById('mydata').textContent);
const id = JSON.parse(document.getElementById('key').textContent);
const TotalAccountBalance = document.getElementById('TotalAccountBalance');

var times = [formatAMPM(new Date)];
var CurrentLabelToPop = times[0]

var prices =  [data];


LineColor = 'limegreen'

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

var socket = new WebSocket(`ws://${window.location.host}/ws/UserTotalAccountBalance/${id}/`);

socket.onmessage = function(elem){
    var num = JSON.parse(elem.data)
    TotalAccountBalance.innerHTML = num.price.toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD',
      });
      
      new_prices = myChart.data.datasets[0].data;
      new_labels =myChart.data.labels

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
          new_prices.push(num.price);
          new_labels.push(formatAMPM(new Date));
      }
      else {
          new_prices.push(num.price);
          new_labels.push(formatAMPM(new Date));
      };

      if (num.price >= new_prices[0]){
        myChart.data.datasets[0].borderColor = 'limegreen';
      }
      else {
        myChart.data.datasets[0].borderColor = 'red';
      };

      myChart.data.datasets[0].data = new_prices;
      myChart.data.labels = new_labels;

      myChart.update();

    
}


function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'pm' : 'am';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
  }








