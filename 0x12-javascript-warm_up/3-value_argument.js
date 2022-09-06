#!/usr/bin/node
const count = process.argv;

if (count === null) {
    console.log('No argument');
} else {
    console.log(count[0]);
}

