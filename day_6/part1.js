import { readFileSync } from 'fs';


const data = readFileSync('input', 'utf8');

const lines = data.toString().split('\n');

const time  = lines[0].split(':')[1].split(' ').filter((x) => x !== '').map((x) => parseInt(x, 10));
const distance  = lines[1].split(':')[1].split(' ').filter((x) => x !== '').map((x) => parseInt(x, 10));
let total = 1;


for (let i = 0; i < time.length; i++) {
  const t = time[i];
  const d = distance[i];

  let first = (-t + Math.sqrt((t * t) - 4 * -1 * -d)) / -2;
  let second = (-t - Math.sqrt((t * t) - 4 * -1 * -d)) / -2;

  total *= Math.abs(Math.ceil(second) - Math.floor(first)) - 1;
  
}
console.log(total);

