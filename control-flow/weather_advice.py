import random

# List of recommendations for each type of weather
sunny_recommendations = [
    "Wear a t-shirt and sunglasses.",
    "Don't forget to apply sunscreen.",
    "Wear a hat or cap to protect yourself from the sun.",
    "Put on light and comfortable clothing.",
    "Carry a water bottle to stay hydrated."
]

rainy_recommendations = [
    "Don't forget your umbrella and a raincoat.",
    "Wear rain boots to keep your feet dry.",
    "Bring a waterproof jacket.",
    "Consider wearing dark-colored clothes to avoid stains.",
    "Carry a plastic bag to protect your belongings."
]

cold_recommendations = [
    "Make sure to wear a warm coat and a scarf.",
    "Wear gloves and a hat to stay warm.",
    "Dress in layers.",
    "Consider wearing thermal socks.",
    "Drink something hot to stay warm inside."
]

# Function to give a random recommendation based on the weather
def recommend_weather(weather):
    if weather == "sunny":
        print(random.choice(sunny_recommendations))
    elif weather == "rainy":
        print(random.choice(rainy_recommendations))
    elif weather == "cold":
        print(random.choice(cold_recommendations))
    else:
        print("Sorry, I don't have recommendations for this weather.")

# Prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Give a recommendation based on user input
recommend_weather(weather)
