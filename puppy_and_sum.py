def Puppy_Sum(D, N):
    
    ps = 0
    
    for x in range(D):
        
        ps = 0
        for y in range(1, N+1):
            ps += y
        
        N = ps
    
    return ps
    
testcases = int(input())

for x in range(testcases):
    
    parameters = input()
    
    parameters = parameters.split()
    
    print(Puppy_Sum(int(parameters[0]), int(parameters[1])))
    