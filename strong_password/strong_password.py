#Copy and pasted right out from hackerrank after submitting code and success.
#Runtime is currently O(lengthOfPassword*4(length of dictionary)) so essentially#This is O(n) depending on length of password manily.


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    needed_checks = 0

    difficulty_dict = {'numbers_check': False, 'lower_check': False, 'upper_check': False, 'special_check': False}

    for letter in password:
        if letter in numbers:
            difficulty_dict['numbers_check'] = True
        elif letter in lower_case:
            difficulty_dict['lower_check'] = True
        elif letter in upper_case:
            difficulty_dict['upper_check'] = True
        elif letter in special_characters:
            difficulty_dict['special_check'] = True
        else:
            continue
    
    for checks in difficulty_dict.values():
        if checks == False:
            needed_checks += 1
    
    if n >= 6 and needed_checks == 0:
        return 0
    elif n >= 6 and needed_checks > 0:
        return needed_checks
    elif n < 6:
        totalchecks = n + needed_checks
        if totalchecks >= 6:
            return needed_checks
        difference = 6 - totalchecks
        totalneeded = difference + needed_checks
        return totalneeded


