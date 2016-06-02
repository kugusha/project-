
function httpGet(theUrl) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function myFunction() {
    var xmlHttp = new XMLHttpRequest();
    var username = document.getElementById("username-input").value;
    var response = httpGet("http://localhost:5000/predict?username=" + username);
    var response = JSON.parse(response);

    console.log("Username: ", username);
    console.log("Request URL: /predict?username=" + username);
    console.log("Response: ", response);
    console.log("====================================================");


    if (response.age == 1) {
    	var age = " < 17";
    } else if (response.age == 2) {
        var age = " 17 - 25";
    } else if (response.age == 3) {
        var age = " 26 - 34";
    } else if (response.age == 4) {
        var age = " > 34";
    }

    if (response.sex == 1) {
        var sex = " male";
    } else if (response.sex == 2) {
        var sex = " female";
    } else if (response.sex == 3) {
        var sex = " female"
    }
   

	document.getElementById("age_pr").innerHTML = "Age: " + age ;
	document.getElementById("sex_pr").innerHTML = "Sex: " + sex  ;
}