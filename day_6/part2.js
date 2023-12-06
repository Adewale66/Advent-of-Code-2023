import { readFileSync } from 'fs';
const data = readFileSync('input', 'utf8');

const lines = data.toString().split('\n');

const t  = Number.parseInt(lines[0].split(':')[1].split(' ').filter((x) => x !== '').reduce((acc, x) => acc + x));
const d  = Number.parseInt(lines[1].split(':')[1].split(' ').filter((x) => x !== '').reduce((acc, x) => acc + x));

let first = (-t + Math.sqrt((t * t) - 4 * -1 * -d)) / -2;
let second = (-t - Math.sqrt((t * t) - 4 * -1 * -d)) / -2;

console.log(Math.abs(Math.ceil(second) - Math.floor(first)) - 1);

