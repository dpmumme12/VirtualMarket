///////////////////////////////////////////////////////
/// Script for the User profile page "Profile.html" ///
///////////////////////////////////////////////////////

//gets the user's info from specifies internal API endpoint
fetch('/api/UserInfo')
.then(response => response.json())
.then(data => {
    var UserInfo = data;

    document.getElementById('Username').value = UserInfo.username;
    document.getElementById('FirstName').value = UserInfo.first_name;
    document.getElementById('LastName').value = UserInfo.last_name;
    document.getElementById('Email').value = UserInfo.email;
});

//updates user profile
function UpdateProfile(){
    const csrfToken = getCookie('csrftoken');

    fetch('/api/UserInfo', {
        method: 'PUT', 
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
          },
          mode: 'same-origin',
        body: JSON.stringify({
        "username": document.getElementById('Username').value,
        "first_name": document.getElementById('FirstName').value,
        "last_name": document.getElementById('LastName').value,
        "email": document.getElementById('Email').value,
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
    
        if (response_status === 200) {
            document.getElementById('alert-wrapper').className = 'alert alert-success alert-dismissible';
            document.getElementById('alert-text').innerHTML = `<i class="bi bi-check-circle-fill" style="padding-right: 10px;"></i> Profile updated successfully`;
            document.getElementById('alert-wrapper').style.display = 'block';
            
            
        }
        else {
            document.getElementById('alert-wrapper').className = 'alert alert-danger alert-dismissible';
            document.getElementById('alert-text').innerHTML = '<i class="bi bi-exclamation-triangle-fill" style="padding-right: 10px;"></i> Oops something has gone wrong.';
            document.getElementById('alert-wrapper').style.display = 'block';
        }

    })
}