const express = require('express');

//configure base directory path using npm module path to get absolute path
const path = require('path');


require('dotenv').config();


const registerRoute = require('./routes/auth/register');

const app = express();


app.use(express.json());

app.use(registerRoute);

//server static files in client/build
app.use(express.static('client/build'));
/// Serve index.html (serve wild card route)
app.get('*', (req, res) => {
    return res.sendFile(path.resolve(__dirname, 'client', 'build', 'index.html'));
});

const PORT = process.env.PORT || 5000;


app.listen(PORT, () => console.log(`Server listening to port ${PORT}`));