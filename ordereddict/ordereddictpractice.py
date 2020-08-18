# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

entry_ordered = OrderedDict()
for order in range(int(input())):
    line = input()
    words = line.split()
    item_product = ' '.join(words[:-1])
    amount = int(words[-1])
    entry_ordered[item_product] = entry_ordered.get(item_product, 0) + amount

for key, value in entry_ordered.items():
    print(key, value)


    
