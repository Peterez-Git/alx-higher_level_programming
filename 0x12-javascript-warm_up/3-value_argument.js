#!/usr/bin/node

const arg2 = process.argv;

if (arg2[2] === undefined) {
  console.log('No argument');
} else {
  console.log(arg2[2]);
}
