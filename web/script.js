function fetchTime() {
    document.getElementById("showTime").innerHTML = new Date();
}

var slider = document.getElementById("weatherIntensity");
var output = document.getElementById("weatherIntensityValue");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value + '%';
}