# read input values
X = int(input())
dog_costs = []
for i in range(3):
    dog_costs.append(list(map(int, input().split())))

# initialize variables
smiling_dogs = 0

# iterate over each dog and calculate the cost of each service
for i in range(3):
    vet_cost = dog_costs[i][0]
    bath_cost = dog_costs[i][1]
    eat_cost = dog_costs[i][2]

    # check if Diksha has enough money to pay for each service
    if X >= vet_cost:
        X -= vet_cost
        smiling_dogs += 1
    elif X >= bath_cost:
        X -= bath_cost
        smiling_dogs += 1
    elif X >= eat_cost:
        X -= eat_cost
        smiling_dogs += 1
    else:
        break

# print the number of dogs Diksha can make smile
print(smiling_dogs)
