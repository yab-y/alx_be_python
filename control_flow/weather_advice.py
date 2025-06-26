weather = input("what's the weather like today? (sunny/rainy/cold): ")
if weather == "sunny":
    clothing_recommmendation = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    clothing_recommmendation = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    clothing_recommmendation = "Make sure to wear a warm coat and a scarf."
else:
    clothing_recommmendation = "Sorry, I don't have recommmendations for this weather."
print(clothing_recommmendation) # updat