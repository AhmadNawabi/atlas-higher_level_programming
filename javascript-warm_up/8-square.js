#!/usr/bin/node

const args = process.argv[2];

if (isNaN(args)) {
  console.log('Missing number');
} else {
  const x = parseInt(args);
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
