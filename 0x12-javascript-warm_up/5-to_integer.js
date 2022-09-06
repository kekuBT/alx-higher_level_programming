#!/usr/bin/node
const nums = parseInt(process.argv);
if (isNaN(nums)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + nums);
}
