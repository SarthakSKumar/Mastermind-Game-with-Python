import random
num=[1,2,3,4,5,6,7,8,9]
code=random.sample(num,4)
guess=10
f=0
while(guess!=0):
    if(f==4):
        points=(10*(guess+1))
        if (10-guess==1):
            print("You've successfully cracked the code in 1 guess and have recieved 100 points!")
            break
        else:
            print("You've successfully cracked the code in",10-guess,"guesses and have recieved",points,"points!")
            break
    f=0
    if(f!=4):
        user_guess=int(input("enter code with 4 unique digits ranging from 1 to 9: "))
        
        user_code=[int(digit) for digit in str(user_guess)]
    
        for i in range (0,4):
            if user_code[i] in code:
                if user_code[i]==code[i]:
                    print(user_code[i],"is correctly placed")
                    f+=1        
                else:
                    print(user_code[i],"is present in the code,but incorrectly placed")
            else:
                print(user_code[i],"is not in the required code")
    guess-=1
    print("guesses left:",guess)
while(guess==0): 
    if(f==4):
        points=(10*(guess+1))
        if (10-guess==1):
            print("You've successfully cracked the code in 1)guess and have recieved 100 points!")
            break
        else:
            print("You've successfully cracked the code in",10-guess,"guesses and have recieved",points,"points!")
            break
    else:   
        print("you've failed to guess the code, the required code was",code[0],code[1],code[2],code[3])
        break


            

        
            


