def location(city):
    south = ["dunedin", "christchurch", "invercargill"]
    north = ["wellington", "auckland"]

    if(city.lower() in south):
        print("The location of", city, "is South Island")
    elif(city.lower() in north):
        print("The location of", city, "is North Island")
    else:
        print("The location of", city, "is unknown")

def discount(age):
    if(age < 15):
        return "Kids4Free"
    elif(age > 64):
        return "GoldenAge"
    else:
        return "No discount for you"

def rating(rate):
    if(rate < 5):
        return "shockingly bad"
    elif(rate < 7):
        return "strictly for a rainly afternoon"
    elif(rate < 8):
        return "pretty good"
    else:
        return "a must see"

def ordinal(cardinal):
    if(cardinal % 10 == 1 and cardinal != 11):
        return str(cardinal) + "st"
    elif(cardinal % 10 == 2 and cardinal != 12):
        return str(cardinal) + "nd"
    elif(cardinal % 10 == 3 and cardinal != 13):
        return str(cardinal) + "rd"
    else:
        return str(cardinal) + "th"

city = input("Enter the city you wish to locate: ")
location(city)
age = int(input("Enter your age: "))
print("You are entitled to a", discount(age), "discount package.")
rate = int(input("Enter the movie rating: "))
print("A rating of", rate, "indicates that this movie is", rating(rate))
cardinal = int(input("Enter Integer "))
print(ordinal(cardinal))
