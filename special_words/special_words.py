"""
Pseudocode:
1) Open file go through each line word by word
2) rstrip the new line at the end
3) Check first two characters to see if match 'he'
4) Check second index onwards to see if 'er' is in there.
5) Append to a list and return sorted list.

Data Structures:
1) A list containin the words that match the criteria
"""


def special_words(filename):

    matched_criteria = list()

    with open(filename, 'r') as file:

        for word in file:
            if word.startswith('he') and 'er' in word[1:]:
                matched_criteria.append(word.rstrip())
        
        sorted_words = sorted(matched_criteria)

        for word in sorted_words:
            print(word)

        return sorted_words


special_words('data.txt')
