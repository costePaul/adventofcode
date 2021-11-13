with open('./2020/day07/input.txt', "r") as f:
    init_rules = f.read().split(".\n")[:-1]

rules = [rule.split(' bags contain ') for rule in init_rules]
bags = [rule[0] for rule in rules]
bags_fixed = []
for bag in bags:
    if bag not in bags_fixed:
        bags_fixed.append(bag)

rules_fixed = []
list_empty_bags = []
for rule in rules:
    if rule[1] == 'no other bags':
        list_empty_bags.append(rule[0])
    else:
        rule1 = rule[1].split(', ')
        conditions = [rule[0]]
        for condition in rule1:
            if condition[-1]=='s':
                    condition = condition[:-5]
            else:
                condition = condition[:-4]
            conditions.append([condition[0], condition[2:]])
        rules_fixed.append(conditions)

dico_part1 = {}
for bag in bags_fixed:
    dico_part1[bag] = []

for rule in rules_fixed:
    value = rule[0]
    keys = [condition[1] for condition in rule[1:]]
    for key in keys:
        dico_part1[key].append(value)

visited = []
def count_bags_containing(bag):
    liste = dico_part1[bag]
    if liste == []:
        return 0
    else:
        count = 0
        for b in liste:
            if b not in visited:
                visited.append(b)
                count += 1+count_bags_containing(b)
        return count

print(count_bags_containing('shiny gold'))        

#Part2

dico_part2 = {}
for bag in bags_fixed:
    dico_part2[bag] = []

for rule in rules_fixed:
    key = rule[0]
    values = rule[1:]
    dico_part2[key]=values

def count_bags_contained(bag):
    liste = dico_part2[bag]
    if liste == []:
        return 0
    else:
        count = 0
        for couple in liste:
            b = couple[1]
            nb = couple[0]
            count += int(nb)*(1+count_bags_contained(b))
        return count

print(count_bags_contained('shiny gold'))