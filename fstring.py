person = "John"
coins = 3

# print("\n " + person + " has " + str(coins) + " coins ")

# message = "\n %s has %s coins" %(person, coins)
# print(message)

# message = "\n {} has {} coins" .format(person, coins)
# print(message)

# message = "\n {1} has {0} coins" .format(coins, person)
# print(message)

# message = "\n {person} has {coins} coins" .format(person = person, coins = coins)
# print(message)

player = {"person": "Dave", "coins" : 3}
# message = "\n {person} has {coins} coins" .format(**player)
# print(message)


#f-string
message = f"\n{person} has {coins} coins"
print(message)
message = f"\n{person} has {coins+1} coins"
print(message)

message = f"\n{person.lower()} has {coins+1} coins"
print(message)

message = f"\n{player['person']}  has {2 * 5} coins left."
print(message)

num = 10 
print(f"\n2.25 times of {num} is {2.25*num:.2f}")

for i in range(1,11):
    print(f"\n2.25 times of {i} is {2.25*i:.2%}")

 