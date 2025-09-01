item1 = 50   
item2 = 30   
item3 = 20   
print("first item:",item1)
print("second item:",item2)
print("third item:",item3)

budget = 120

total_cost = item1 + item2 + item3


print("Total cost of items:", total_cost)
print("Budget:", budget)


if total_cost <= budget:
    print("You are within budget.")
    print("Money left:", budget - total_cost)
else:
    print("You exceeded the budget!")
    print("You need", total_cost - budget, "more.")