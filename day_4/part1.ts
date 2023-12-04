import * as fs from 'fs';

const words = fs.readFileSync('input', 'utf8').split('\n');

let total = 0;

for(let i = 0; i < words.length - 1; i++)
{
	const numbers = words[i].split(":")[1];
	const [ wn , gn ] = numbers.split("|");
	const winNums = wn.trim().split(" ");
	const gameNums = gn.trim().split(" ");
	const nums = winNums.filter(x => x != "" && gameNums.includes(x)).length
	if (nums > 0)
		total += Math.pow(2, nums - 1 )
}
console.log(total);
