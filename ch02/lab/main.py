import random
 
#Part A
weeks = 16
print(weeks, type(weeks))

classes = 5
print(classes, type(classes))

tuition = 6000
print(tuition, type(tuition))

classes_per_week = 3
print(classes_per_week, type(classes_per_week))



cost_per_week = ((tuition / classes) / weeks)
print(cost_per_week, type(cost_per_week))



print('Your cost per class is' cost_per_class)


#Part B
 
new = list(range(1,6))
print(random.choice(new))