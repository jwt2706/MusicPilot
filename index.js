const { app, BrowserWindow } = require("electron");
const path = require("path");
const { exec } = require("child_process");

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
      nodeIntegration: true,
      contextIsolation: false,
    },
  });

  mainWindow.loadFile("index.html");
}

app.on("ready", () => {
  // Install Flask dependencies
  exec("pip install -r requirements.txt", (err, stdout, stderr) => {
    if (err) {
      console.error(`Error installing dependencies: ${stderr}`);
      return;
    }
    console.log(`Dependencies installed: ${stdout}`);

    // Start Flask server
    exec("flask run", (err, stdout, stderr) => {
      if (err) {
        console.error(`Error starting Flask: ${stderr}`);
        return;
      }
      console.log(`Flask started: ${stdout}`);
    });

    createWindow();
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});

app.on("activate", () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
