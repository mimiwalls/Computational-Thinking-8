cat_points = 0 
dog_points = 0 

answer = input("what would you rather do A) explore as much or the ocean as you want, or B explore space as much as you want")
if answer == "A":
    cat_points += 1 
elif answer == "B":
    dog_points += 1 
answer = input (" are you A) a person that needs to be around people all the time, or B a person that would rather be all by your self?")
if answer == "A":
        dog_points += 1 
elif answer == "B": 
     cat_points += 1 
answer = input("what would you rather do A) go travel for the rest of your life, or B or stay at home for the rest of your life?")
if answer == "a" or answer == "A": 
        dog_points += 1 
elif answer == "B" and cat_points > 3: 
     print ("you really like cats!!!") 
     cat_points += 1  
answer = input(" are you A) a very trusting person, or B some one that can't trust people very well.")
if answer == "a" or answer == "A": 
    dog_points += 1 
elif answer == "B": 
     cat_points += 1 
answer = input ("are you A) not very moody or B moody?")
if answer == "A": 
     dog_points += 1 
elif answer == "B":
     cat_points += 1 
if cat_points > dog_points:
     print ("you are cat person!!!")
elif dog_points > cat_points:
    print ("you are a dog person!")
    print ("thanks for playing")