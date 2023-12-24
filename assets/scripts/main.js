if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/service-worker.js')
      .then(registration => {
      console.log('Service Worker registered:', registration);
      })
      .catch(error => {
      console.log('Service Worker registration failed:', error);
      });
}

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