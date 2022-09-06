#!/usr/bin/node
const a = parseInt(process.argv);
if (isNaN(a)) {
  console.log('Missing number of occurrences');
} else {
  console.log('C is fun\n'.repeat(a));
}
