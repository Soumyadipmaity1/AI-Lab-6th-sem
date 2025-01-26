#Store the name of 7 of your friend, print the name who has the highest num of a letter

friends = ["Rahul", "Soumyaditya", "Indulekha", "Sudeep", "Gaurav", ]

max_count = 0
name = ""

for name1 in friends:
    count = 0  
    for char in name1:  
        if char == 'A' or char == 'a':  
            count += 1
    if count > max_count:  
        max_count = count
        name = name1


print(f"The friend with the highest number of 'A's is: {name}")
