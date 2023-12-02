#!/usr/bin/python3

import sys 

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: part1.py <input_file>")
		sys.exit(1)
	
	game = {
		"red": 12,
		"green": 13,
		"blue": 14,
	}
	total = 0
	with open(sys.argv[1]) as f:
		lines = f.readlines()
		for line in lines:
			id = line.split(":")[0].split(" ")[1]
			color_sets = line.strip().split(":")[1].split(";")
			no_of_sets = len(color_sets)
			valid = 0
			
			for set in color_sets:
				colors = set.split(",")
				check_set = 0
				valid_check = len(colors)
				for color in colors:
					color_num = int(color.strip().split(" ")[0])
					color_name = color.strip().split(" ")[1]
					if color_num <= game[color_name]:
						check_set += 1
				if check_set == valid_check:
					valid += 1
			if valid == no_of_sets:
				total += int(id)
	print(total)
				
				

	