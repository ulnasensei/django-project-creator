#!/usr/bin/env node
const {exec} = require('child_process')
const createdjango = exec('bash createdjango', 
(error, stdout, stderr) => {
    console.log(stdout);
    console.log(stderr);
    if(error){
        console.log(`exec error: ${error}`)
    }
})