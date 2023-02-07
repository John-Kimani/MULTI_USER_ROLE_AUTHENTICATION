const express = require('express');

//configure base directory path using npm module path to get absolute path
const path = require('path');

const app = express();

/// Serve index.html (serve wild card route)
app.get('*', (req, res) => {
    const myPath = path.resolve(__dirname, 'client', 'build', 'index.html')
    console.log('__dirname', __dirname);
    console.log('My path: ', myPath);
    return res.sendFile(myPath);
});

const PORT = process.env.PORT || 5000;


app.listen(PORT, () => console.log(`Server listening to port ${PORT}`));