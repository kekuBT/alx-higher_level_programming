#!/usr/bin/node
const num = process.argv.slice(2);
const nums = parseInt(num[0]);
if (isNaN(nums)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + nums);
}
