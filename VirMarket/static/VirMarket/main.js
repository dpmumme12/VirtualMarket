
var ctx = document.getElementById('canvas').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: 'High',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: 'transparent',
            borderColor:'blue',
            borderWidth: 1
        },
        {
            label: 'Low',
            data: [9, 15, 1, 3, 0, 1],
            backgroundColor: 'transparent',
            borderColor:'Green',
            borderWidth: 1
        }]
    },
    options: {
        elements:{
            line:{
                tension:0
            }
        },
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


document.write(window.data);
