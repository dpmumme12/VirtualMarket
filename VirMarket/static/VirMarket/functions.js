var typingTimer;
var blurtimeout;
var doneTypingInterval = 400;

function SearchKeyUp() {
    clearTimeout(typingTimer);
    typingTimer = setTimeout(SearchQuery, doneTypingInterval);
}

function SearchKeyDown() {
    clearTimeout(typingTimer);
}

function SearchOnBlur(){
    setTimeout(clearSearchBar, 100);
}

function clearSearchBar(){
    document.getElementById('SearchBar').value = '';
    document.getElementById('MyDropdown').innerHTML = '';
}


function SearchQuery() {
    document.getElementById('MyDropdown').innerHTML = '';

    var query = document.getElementById('SearchBar').value.toUpperCase();

    if (query === ''){
        return
    }

    fetch(`https://finnhub.io/api/v1/search?q=${query}&token=c5bmkjqad3ifmvj0nc10`)
    .then(response => response.json())
    .then(data => {
        Stocks = data.result
        Stocks = Stocks.filter(function(elem) {
            return !elem.symbol.includes('.') & !elem.symbol.includes(':');
        });
       
        for(i=0; i< 10; i++){
            if (Stocks[i] == null){
                //pass
            }
            else{
                document.getElementById('MyDropdown').innerHTML += `<a tabIndex="-1" href="${'/Stock/' + Stocks[i].symbol}" class="Dropdown-Item">${Stocks[i].symbol}<p class="SearchDescription">${Stocks[i].description}</p></a>`;
            }
        }
    });
}

function GetGraphData(times, prices, LineColor) {
    var GraphData = {
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

    return GraphData;
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

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function closeAlert(){
    document.getElementById('alert-wrapper').style.display = 'none';
}
