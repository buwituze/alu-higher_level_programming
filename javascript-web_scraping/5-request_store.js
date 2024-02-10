#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const sourceURL = process.argv[2];
const destinationFilePath = process.argv[3];

// Making a request to the source URL and piping the response to a writable stream
request(sourceURL).pipe(fs.createWriteStream(destinationFilePath));
