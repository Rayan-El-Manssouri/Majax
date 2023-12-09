const express = require("express");
const fs = require("fs");
const path = require("path");
const config = require("./config");

const app = express();
app.use(express.json());

// Endpoint pour récupérer tous les utilisateurs
app.get("/users", (req, res) => {
  try {
    const usersData = fs.readFileSync(path.join(__dirname, "users.json"));
    const users = JSON.parse(usersData);
    res.status(200).json(users);
  } catch (error) {
    console.error(`Error reading users file: ${error.message}`);
    res.status(500).send("Internal Server Error");
  }
});

// Endpoint pour récupérer un utilisateur par son ID
app.get("/users/:id", (req, res) => {
  const userId = req.params.id;

  try {
    const usersData = fs.readFileSync(path.join(__dirname, "users.json"));
    const users = JSON.parse(usersData);
    const user = users.find((u) => u.id === userId);

    if (user) {
      res.status(200).json(user);
    } else {
      res.status(404).send("User not found");
    }
  } catch (error) {
    console.error(`Error reading users file: ${error.message}`);
    res.status(500).send("Internal Server Error");
  }
});

// Connection
app.listen(config.port, (err) => {
  if (err) {
    console.error(`Error starting the server: ${err.message}`);
  } else {
    console.log(`Server is running on http://localhost:${config.port}`);
  }
});