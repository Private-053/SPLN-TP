var express = require('express');
var router = express.Router();
const axios = require('axios');

/* GET home page. */
router.get('/', function(req, res, next) {
  axios.get('http://localhost:5000/')
    .then(response => {
      dados = response.data;
      res.render('index', {programacao: dados });
    })
    .catch(function (error) {
      console.log(error);
    })
});

module.exports = router;
