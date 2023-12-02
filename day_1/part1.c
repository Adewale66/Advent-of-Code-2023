#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char **argv)
{
	if (argc != 2)
	{
		printf("Usage: %s <string>\n", argv[0]);
		return 1;
	}

	char *line = NULL;
	size_t len = 0;
	ssize_t read;
	FILE *input = fopen(argv[1], "r");
	if (input == NULL)
	{
		printf("Error opening file %s\n", argv[1]);
		return 1;
	}
	size_t sum = 0;
	while ((read = getline(&line, &len, input)) != -1)
	{
		size_t first = 0;
		size_t last = 0;
		size_t length = strlen(line) - 1;

		for (size_t i = 0; i < length; i++)
		{
			if (line[i] > 47 && line[i] < 58)
			{
				if (first == 0)
					first = line[i] - '0';
			}
			if (line[length - i - 1] > 47 && line[length - i - 1] < 58)
			{
				if (last == 0)
					last = line[length - i - 1] - '0';
			}
			if (first != 0 && last != 0)
				break;
		}
		sum += ((first * 10) + last);
	}
	fclose(input);
	if (line)
		free(line);
	printf("Sum: %ld\n", sum);
	return 0;
}
