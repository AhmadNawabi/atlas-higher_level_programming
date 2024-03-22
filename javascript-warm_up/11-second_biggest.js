#!/usr/bin/node

const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  const Numbers = args.slice(2).map(Number);
  const SortedNumber = Numbers.sort((a, b) => a - b);
  console.log(SortedNumber[SortedNumber.length - 2]);
}
