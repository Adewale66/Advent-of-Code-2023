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
	with open(sys.argv[1], "r") as f:
		lines = f.readlines()
		for line in lines:
			color_sets = line.strip().split(":")[1].split(";")
			game_min = {
				"red": 0,
				"green": 0,
				"blue": 0,
			}
			power = 1
			for set in color_sets:
				colors = set.split(",")
				for color in colors:
					color_num = int(color.strip().split(" ")[0])
					color_name = color.strip().split(" ")[1]
					if color_num > game_min[color_name]:
						game_min[color_name] = color_num
			for color in game_min:
				power *= game_min[color]
			total += power
					
	print(total)
				
				

	