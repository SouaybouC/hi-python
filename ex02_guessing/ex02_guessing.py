import random

def guess():
    
    print("left?: ")
    left = input()
    print("right: ")
    right = input()
    
    if(int(left)>int(right)):
        return "left must < right"
        
    rand = random.randrange(int(left),int(right))
    print("your guess ?: ")
    x = input()
    print(rand)
    while(int(x)!=rand):
        
        lastx = x
        if(int(x)<rand):
            print("too small try again:")
            x= input()
            if(int(lastx)<int(x)<rand ) :
                print(" small but closer to result")
        if (int(x)>rand):
            print("too great try again:")
            x = input()
            if(int(x)<rand<int(lastx)):
                print("new range is " + x + " < result < " +lastx)
    return ("yes !"+str(rand))    
    
print(guess())