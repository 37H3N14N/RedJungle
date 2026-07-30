const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 5090;

const HIERARCHY_SERVER = 'http://192.168.1.103:9011'


// Define a route for the root URL
app.get('/', (req, res) => {

  axios.get(HIERARCHY_SERVER, {params:{'session_id':'greatings earthlings'}})

  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });


});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});




