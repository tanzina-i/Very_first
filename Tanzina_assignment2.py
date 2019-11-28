s = raw_input("Please enter a string input: ")

new_string = ""
operations = 0

for i in range(len(s)):
    if(ord(s[i]) > ord(s[len(s)-1-i])):
        x = i
        y = len(s) - 1-i

    elif(ord(s[len(s)-1-i]) > ord(s[i])):
        x = len(s) - 1-i
        y = i

    else:
        x = y = i = len(s) - 1-i

    new_string += s[y]
    operations += ord(s[x]) - ord(s[y])

print "The palindrome string created is: ",new_string
print "Number of operations required is: ",operations/2
