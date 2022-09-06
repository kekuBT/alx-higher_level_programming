#!/usr/bin/node
const count = process.argv.slice(2);

if (!count[0]) {
  console.log('No argument');
} else {
  console.log(count[0]);
}
