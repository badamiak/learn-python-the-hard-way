states = {
    "Oregon" : "OR",
    "Florida": "FL",
    "California": "CA",
    "New York" : "NY",
    "Michigan"  : "MI"
}

cities = {
    "CA" : "San Francisco",
    "MI" : "Detroit",
    "FL" : "Jacksonville"
}

cities["NY"] = "New York"
cities["OR"] = "Portland"

print("-"*10)
print(f"NY State has: {cities['NY']}")
print(f"OR State has: {cities['OR']}")

print("-"*10)
print(f"Michigan's abbreviation is: {states['Michigan']}")
print(f"Florida's abbreviation is: {states['Florida']}")

print("-"*10)
print(f"Michigan has: {cities[states['Michigan']]}")
print(f"Florida has: {cities[states['Florida']]}")

print("-"*10)
for state, abbrev in states.items():
    print(f"{state} is abbreviated {abbrev}")

print("-"*10)
for abbrev, city in cities.items():
    print(f"{city} is in {abbrev}")

print("-"*10)
for state, abbrev in states.items():
    print(f"{state} is abbrevieated {abbrev} and has the city of {cities[abbrev]}")

print("-"*10)
state = states.get("Texas")

if not state:
    print("Sorry, no Texas")

city = cities.get('TX', "Doesn't exist")
print(f"The city for the state 'TX' is: {city}")