'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # Base case - 'th' requires at least two characters for it to exist
    if len(word) < 2:
        return 0
        
    # check to see if 'th' are the first two characters
    if word[:2] == "th":
        # if it does, call count again passing the word 
        # without the first two chars 
        # (since 'h' will not be a 't' if we just remove first char)
        count = count_th(word[2:])
        # return 1
        return count + 1
    # if 'th' are not the first two characters
    else:
        # call count again passing in word without the first char
        count = count_th(word[1:])
        # return 0    
        return 0 + count

print(count_th("thsothbidth"))
