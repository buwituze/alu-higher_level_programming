#!/usr/bin/node
const fs = require('fs');

// Get the file path from command line arguments
const filePath = process.argv[2];

// Check if the file path is provided
if (!filePath) {
  console.error('File path is missing.');
  process.exit(1);
}

// Read the content of the file
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err); // Print the error object if an error occurred
  } else {
    console.log(data); // Print the content of the file
  }
});
