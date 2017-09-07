function update_buttons(belt, vertical, horizontal)
{
	if (belt != null) {
		document.getElementById("belt").className = 
			(belt == "belt") ? "button_active" : "button_inactive";
		document.getElementById("nobelt").className = 
			(belt == "nobelt") ? "button_active" : "button_inactive";
	}
	
	if (vertical != null) {
		document.getElementById("up").className = 
			(vertical == "up") ? "button_active" : "button_inactive";
		document.getElementById("down").className = 
			(vertical == "down") ? "button_active" : "button_inactive";
		document.getElementById("nov").className = 
			(vertical == "nov") ? "button_active" : "button_inactive";
	}

	if (horizontal != null) {
		document.getElementById("cw").className = 
			(horizontal == "cw") ? "button_active" : "button_inactive";
		document.getElementById("ccw").className = 
			(horizontal == "ccw") ? "button_active" : "button_inactive";
		document.getElementById("noh").className = 
			(horizontal == "noh") ? "button_active" : "button_inactive";
	}
}

function error()
{
	CLIENT=window.location.hash.substr(1);
	e = document.getElementById("error");
	switch (CLIENT) {
		case "1":
			e.innerHTML = 'Error communicating with the server. Try the <a href="http://192.168.0.230/excavator.html#2">HA version</a>!';
			break;
		case "2":
			e.innerHTML = 'Failover in progress, please wait...';
			break;
	}
	e.className = "error_visible";
}

function noerror()
{
	document.getElementById("error").className = "error_hidden";
}

function set_state(button)
{
	CLIENT=window.location.hash.substr(1);
	
	var xhttp;
	document.getElementById(button).className = "button_inprogress";
	
	belt = null;
	vertical = null;
	horizontal = null;
	switch(button) {
		case "up":
		case "down":
		case "nov":
			vertical = button;
			group = "vertical";
			break;

		case "cw":
		case "ccw":
		case "noh":
			horizontal = button;
			group = "horizontal";
			break;

		case "belt":
		case "nobelt":
			belt = button;
			group = "belt";
			break;
	}
	xhttp=new XMLHttpRequest();
	xhttp.timeout = 1000;
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4) {
			if (this.status == 200) {
				update_buttons(belt, vertical, horizontal);
			}
			else {
				error();
			}
		}
	};
	xhttp.open("GET", '/cgi-bin/set_state.cgi?' + group + '=' + button + "&client=" + CLIENT);
	xhttp.send();
}

function update_state()
{
	CLIENT=window.location.hash.substr(1);

	var xhttp;
	xhttp=new XMLHttpRequest();
	xhttp.timeout = 1000;
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4) {
			if (this.status == 200) {
				res = xhttp.responseText.trim().split(" ");
	    			if (res[0] == "OK") {
					update_buttons(res[1], res[2], res[3]);
					noerror();
				}
			}
			else error();
 		}
	};
	xhttp.open("GET", '/cgi-bin/get_state.cgi?web' + CLIENT);
	xhttp.send();
}

setInterval(update_state, 1000);
