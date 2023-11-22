// Import packages
const express = require("express");
const home = require("./routes/home");
const config = require("./config");

// Middlewares
const app = express();
app.use(express.json());

// Routes
app.use("/", home);

// Connection
app.listen(config.port, (err) => {
  if (err) {
    console.error(`Error starting the server: ${err.message}`);
  } else {
    console.log(`Server is running on http://localhost:${config.port}`);
  }
});