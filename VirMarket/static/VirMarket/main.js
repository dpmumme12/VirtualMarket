// const data = JSON.parse(document.getElementById('mydata').textContent);

// var times = [formatAMPM(new Date)];

// var prices =  [data];


// LineColor = 'limegreen'

// GraphData = {
//     type: 'line',
//     data: {
//         labels: times,
//         datasets: [{
            
//             data: prices,
//             backgroundColor: 'transparent',
//             borderColor:LineColor,
//             borderWidth: 1.5
//         }]
//     },
//     options: {
//         plugins: {
//             legend: {
//                 display: false 
//             },
//         },
//         elements:{
//             point:{
//                 radius:0
//             }
//         },
//         scales: {
//             x: {
//                 grid: {display:false},
//                 ticks: {
//                     display: true,
//                     autoSkip: true,
//                     maxTicksLimit: 10
//                 }
//               },
//               y: {
//               }  
//         },
//         tooltips: {
//             mode: 'index',
//             intersect: false,
//             enabled: false
//          },
//          hover: {
//             mode: 'index',
//             intersect: false
//          },
//         responsive: true,
//         maintainAspectRatio: false,
//         animation: false
//     }
// };

// var ctx = document.getElementById('canvas').getContext('2d');
// var myChart = new Chart(ctx, GraphData);

// var socket = new WebSocket('ws://localhost:8000/ws/UserTotalAccountBalance/8/');

// socket.onmessage = function(elem){
//     var num = JSON.parse(elem.data)
//     console.log(num.price)
// }



// function formatAMPM(date) {
//     var hours = date.getHours();
//     var minutes = date.getMinutes();
//     var ampm = hours >= 12 ? 'pm' : 'am';
//     hours = hours % 12;
//     hours = hours ? hours : 12; // the hour '0' should be '12'
//     minutes = minutes < 10 ? '0'+minutes : minutes;
//     var strTime = hours + ':' + minutes + ' ' + ampm;
//     return strTime;
//   }








