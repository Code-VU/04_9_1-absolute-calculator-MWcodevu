def calculateAbsolute():
    
    # This first line is provided for you
    in_num  = int(input("Enter a number: "))
    if in_num >= 21:
        in_dif = (in_num -21)*2
    else:
        in_dif = 21 - in_num
    print(f"Result: {in_dif}")    














    # end assignment

## If you want to test locally run > python payCalculator.py

if __name__ == "__main__":
    calculateAbsolute()
