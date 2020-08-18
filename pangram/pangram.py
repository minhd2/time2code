

def is_pangram(input_string):
	s = s.lower()
	s = s.replace(" ", "")
	s = set()
	if len(s) >= 26:
		return "pangram"
	return "not pangram"