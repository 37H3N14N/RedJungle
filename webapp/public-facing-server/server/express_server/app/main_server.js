const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 5090;

const data_transport = {
  "workflow_name":"create_user",
  "authorization":{'jwt':'SDLA45AD1FADF5A4FA5DFADAF'},
  "payload":{"username":"James Bond"}
}

// Define a route for the root URL
app.get('/', (req, res) => {
    const {data_fastapi} = axios.post('http://localhost:7001/client',data_transport)
    res.send(data_fastapi);
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});




