"""
Pseudocode:
1) Open file
2) Go line by line and separate by column
3) Use food_price_dict as food_name: [count_of_over_4, total_count]
4) If item not in food_price_dict then add into dict
5) If price > $4 increment count_of_over_4
6) Also increment total_count
7) Can divide count_of_over_4 after by total_count giving percentage for each item into new dictionary.

Data Structures Needed:
food_price_dict = dict([count_of_over_4, total_count])
food_percentage_over_4 = dict() {food:percentage}

"""


def over_price(filename):
    
    food_price_dict = dict()
    food_percentage_over_4 = dict()

    with open(filename, 'r') as file:
        for line in file:
            columns = line.split()
            food = columns[0]
            price = columns[2].lstrip('$').rstrip() #Strip out the '$' and \n

            if food not in food_price_dict:
                food_price_dict[food] = [0, 1]
                if float(price) > 4:
                    food_price_dict[food][0] += 1
            elif float(price) > 4 and food in food_price_dict:
                food_price_dict[food][0] += 1
                food_price_dict[food][1] += 1
            else:
                food_price_dict[food][1] +=1
        
        for key, value in food_price_dict.items():
            percentage = round(float(value[0]/value[1] * 100), 2)
            food_percentage_over_4[key] = percentage

    print(food_percentage_over_4)
    return food_percentage_over_4


over_price('data.txt')
