import * as fs from 'fs';

const words = fs.readFileSync('input', 'utf8').split('\n');

const h = {}
let total = 0;

for (let i = 0;  i < words.length - 1; i++)
{
	h[i] = 1;
}



for(let i = 0; i < words.length - 1; i++)
{
	const numbers = words[i].split(":")[1];
	const [ wn , gn ] = numbers.split("|");
	const winNums = wn.trim().split(" ");
	const gameNums = gn.trim().split(" ");

	let cp =  winNums.filter(x => x != "" && gameNums.includes(x)).length
	let tmp = cp
	for (let l = 0; l < h[i]; l++)
	{
		cp = tmp;
		let k = i + 1;
		while(cp != 0)
		{
			if (k >= words.length - 1)
			{
				break;
			}
			h[k] = h[k] + 1;
			k++;
			cp--;
		}
		
	}
	
}

for (let i in h)
{
	total += h[i];
}
console.log(total);
