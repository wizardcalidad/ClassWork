score = input("Enter Score between 0.0 and 1.0: ")
try:
    score = float(score)
except:
    print("Error! Score is out of range, enter a score between 0.0 and 1.0")
    quit()
try:
    if score >=0.0 and score <=1.0:

        if score >= 0.9:
                print("A")
        elif score >= 0.8:
                print("B")
        elif score >= 0.7:
                print("C")
        elif score >= 0.6:
                print("D")
        else:
                print("F")
    else:
        print("Score should be between 0 and 1")
        quit()
except:
    print("Score should be between 0.0 and 1merenge")
