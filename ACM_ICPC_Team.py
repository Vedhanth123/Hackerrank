
def acmTeam(topic):
    # Write your code here

    subjects = []
    
    highest = 0
    no_of_highest = 0

    # 1) bunch two strings at a time 
    for x in range(len(topic)):

        for y in range(x+1, len(topic)):
            
            count = 0

            # 2) compare each element of the strings with 'or' if it has one
            if(int(topic[x]) | int(topic[y])):

                # 3) note down the 1's and store the result
                    count += 1
            
            if(count > highest):
                highest = count
                
            
            subjects.append(count)
            
    # 4) find the largest number and count the largest numbers in the array and return it
    for x in range(len(subjects)):
    
        if(highest == subjects[x]):
            no_of_highest += 1
            
            
    return [highest, no_of_highest]
 
print(acmTeam(['10101', '11110', '00010']))


