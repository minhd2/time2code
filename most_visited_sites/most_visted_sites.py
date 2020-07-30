"""
Thoughts: Thinking of which way would be best to pull the list out of the sorted dictionary.
Essentially I can just do print(sorted_counter_dictionary[0:5] but this will give the amount of times visited.
The question itself is only asking for a 2d array,set of highest website visited.. Such as
[('imdb.com', 7), ('walmart.com', 6), ('etsy.com', 5), ('fandom.com', 5), ('pinterest.com', 4)]

Going to leave it as this for now. Will have to revisit.


I can go through the list 


"""

def most_visited_sites(filename):
	tmp_counter_dictionary = {}

	with open(filename, 'r') as file:
		for line in file:
			sites = line.split()
			for site in sites[2::]:
				tmp_counter_dictionary[site] = tmp_counter_dictionary.get(site, 1) + 1

	
	sorted_counter_dictionary = sorted(tmp_counter_dictionary.items(), key=lambda x: x[1], reverse=True)
	top_5_websites = sorted_counter_dictionary[0:5]
	return top_5_websites
	

most_visited_sites("data.txt")