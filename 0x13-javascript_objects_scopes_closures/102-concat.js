#!/usr/bin/node
// concats 2 files
const zote = require('fs');
const fileA = zote.readFileSync(process.argv[2], 'utf8');
const fileB = zote.readFileSync(process.argv[3], 'utf8');
zote.writeFileSync(process.argv[4], fileA + fileB);
