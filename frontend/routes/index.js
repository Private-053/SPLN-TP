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

/* GET rating. */
router.get('/rating/:titulo', function(req, res, next) {
  axios.get('http://localhost:5000/rating/' + req.params.titulo)
    .then(response => {
      dados = response.data;
      res.render('rating', {rating: dados });
      
    })
    .catch(function (error) {
      console.log(error);
    })
});

router.get('/canal/:canal', function(req, res, next) {
  axios.get('http://localhost:5000/canal/' + req.params.canal)
    .then(response => {
      dados = response.data;
      res.render('canal', {canal: dados, nome: req.params.canal }); 
    })
    .catch(function (error) {
      console.log(error);
      res.render('error',{error: error})
    })
});

module.exports = router;
