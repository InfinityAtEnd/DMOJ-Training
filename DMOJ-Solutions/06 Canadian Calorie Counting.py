# See the problem request at the link down below
# https://dmoj.ca/problem/ccc06j1

# my solution:
Burger = int(input())
Side = int(input())
Drink = int(input())
Dessert = int(input())
callories = 0

if Burger == 1:
	callories += 461
elif Burger == 2:
	callories += 431
elif Burger == 3:
	callories += 420

if Drink == 1:
	callories += 130
elif Drink == 2:
	callories += 160
elif Drink == 3:
	callories += 118

if Side == 1:
	callories += 100
elif Side == 2:
	callories += 57
elif Side == 3:
	callories += 70

if Dessert == 1:
	callories += 167
elif Dessert == 2:
	callories += 266
elif Dessert == 3:
	callories += 75

print(f'Your total Calorie count is {callories}.')
