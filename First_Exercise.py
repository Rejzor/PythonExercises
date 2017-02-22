import random
import re

def check_hour_format(*arg):
	hour24format_re = re.compile(r'^(([01]\d|2[0-3])([0-5]\d))$') # [01]\d - '0' or '1' + any digit, |2[0-3] - OR '2' + digit from '0' to '3'. Hours part done, now minutes. [0-5] - number from '0' to '5' + any digit.
	final_digits=[] # lits of all digits which fit to 24hour format
	for digit in arg:
		if hour24format_re.match(digit):
			final_digits.append(digit)
	return final_digits
def main():
	from itertools import permutations

	random_nums=[str(random.randrange(0,9)) for number in range(4)] # generate for numbers
	permutations=[''.join(perm) for perm in permutations(random_nums)] # all permutations, ''. join(perm) for conver from ('1','1','1','1') format to ('1111').
	final_digits= check_hour_format(*permutations) # check all permutations 
	final_digits.sort() # sort from lowest to highest
	if not final_digits:
		print("From digits {0} cannot create any 24H format digits.".format(permutations))
	else:
		print("Highest hour {0}:{1}, lowest hour {2}:{3}".format(final_digits[-1][0:2],final_digits[-1][2:4],final_digits[0][0:2],final_digits[0][2:4]))
if __name__ == "__main__":
	main()