#!/usr/bin/node

// Require the callMeMoby function from the other file
const callMeMoby = require('./101-call_me_moby').callMeMoby;

// Use the callMeMoby function
callMeMoby(3, function () {
  console.log('C is fun');
});
