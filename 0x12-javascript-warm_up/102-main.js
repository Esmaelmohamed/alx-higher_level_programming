#!/usr/bin/node

// Require the addMeMaybe function from the other file
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;

// Use the addMeMaybe function
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
