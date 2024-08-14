document.getElementById("load-audio").addEventListener("click", () => {
  fetch("http://localhost:5000/api/load", {
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => console.log(data));
});

document.getElementById("pause-resume").addEventListener("click", () => {
  fetch("http://localhost:5000/api/pause", {
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => console.log(data));
});

document.getElementById("open-explorer").addEventListener("click", () => {
  fetch("http://localhost:5000/api/play", {
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => console.log(data));
});
