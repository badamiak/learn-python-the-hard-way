def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("""You have %d cheeses!
You have %d boxes of crackers!
Man that's enought for a party!
Get a blanket.""" %(cheese_count, boxes_of_crackers))

print("We can just give he function numbers directly:")
cheese_and_crackers(20,30)

print("or, we can use variables from our script:")
cheese_count = 10
crackers_count = 50

cheese_and_crackers(cheese_count, crackers_count)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(cheese_count+100, crackers_count+1000)