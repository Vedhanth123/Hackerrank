

def kaprekarNumbers(p, q):

    no_of_karprekar_numbers = 0

    for i in range(p, q+1):
        
        # ) find the number of digits of a number
        number = int(i)
        
        no_of_digits_of_original_number = len(str(number))
        
        # ) Take a number and square the number
        
        square_of_number = number ** 2
        
        # ) find the number of digits of squared number
        square_of_number = str(square_of_number)
        
        size_of_squared_number = len(square_of_number)
        
        # ) split the number so that the right part of the splitted number 
        
        # must have same number of digits as the digits of the original number

        if(size_of_squared_number == 1):
            left = 0
            right = square_of_number

        else:
            left = square_of_number[:size_of_squared_number-no_of_digits_of_original_number]
            
            right = square_of_number[size_of_squared_number-no_of_digits_of_original_number:]
        

        # ) Then add the two numbers  

        summed = int(left) + int(right)
        
        # ) if the added number is equal to the original number then the number 
        # is said to be karprekar number
        
        if(summed == number):
            print(summed)
            no_of_karprekar_numbers += 1
        

    if(no_of_karprekar_numbers == 0):
        print("INVALID RANGE")
        
        
kaprekarNumbers(1,100)
