import * as fs from 'fs';

const words = fs.readFileSync('input', 'utf8').split('\n');

let total = 0;

for(let i = 0; i < words.length - 1; i++)
{
	let points = 0;
	const numbers = words[i].split(":")[1];
	const [ wn , gn ] = numbers.split("|");
	const winNums = wn.trim().split(" ");
	const gameNums = gn.trim().split(" ");

	for (let j = 0; j < winNums.length; j++)
	{
		if (winNums[j] == "")
		{
			continue;
		}
		
		if (gameNums.includes(winNums[j]))
		{
			if (points == 0)
				points++;
			else
				points *= 2;
		}
	
	}
	total += points;

}
console.log(total);
