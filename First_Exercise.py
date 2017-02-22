import random
from itertools import permutations
import re

def check_hour_format(*arg):
	hour24format_re = re.compile(r'^(([01]\d|2[0-3])([0-5]\d))$') # [01]\d - '0' or '1' + any digit, |2[0-3] - OR '2' + digit from '0' to '3'. Hours part done, now minutes. [0-5] - number from '0' to '5' + any digit.
	final_digits=[] # lits of all digits which fit to 24hour format
	for digit in arg:
		if hour24format_re.match(digit):
			final_digits.append(digit)
	return final_digits