import math
 
def theater_square():
    num1, num2, num3 = input().split()
    height = int(num1)
    width = int(num2)
    length = int(num3)
    
    answer = (math.ceil(height/length)) * (math.ceil(width/length))
    
    print(answer)
    
theater_square()
