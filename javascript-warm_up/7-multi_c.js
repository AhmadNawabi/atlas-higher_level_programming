#!/usr/bin/node
const args = process.argv[2];

if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(args);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
