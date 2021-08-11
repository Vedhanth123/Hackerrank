
def makingAnagrams(s1, s2):
    # Write your code here

    # 1) first note down all the letters in both the strings
    Each_alphabet_count1 = {}
    Each_alphabet_count2 = {}

    for x in range(26):
        Each_alphabet_count1.update({chr(97 + x):0})
        Each_alphabet_count2.update({chr(97 + x):0})
        
    for x in range(len(s1)):

        Each_alphabet_count1[s1[x]] += 1
        
    
    for x in range(len(s2)):

        Each_alphabet_count2[s2[x]] += 1
        

    difference = 0

    for x in range(len(Each_alphabet_count1)):

    # 2) Check if both the letters are same or not
        if(Each_alphabet_count1[chr(97 + x)] != Each_alphabet_count2[chr(97 + x)]):
           difference += abs(Each_alphabet_count1[chr(97 + x)] - Each_alphabet_count2[chr(97 + x)])


    return difference

    # 3) if the letters are not same then take the absolute value of the 
    # no of repetitions of that letter and remove that many repetitions of the strings
    # 4) note down no of removals
    # 5) return the no of removals

