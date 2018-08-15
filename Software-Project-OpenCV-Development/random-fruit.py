import random

#apple = False;
#orange = 'orange';
#banana = 'yellow';
#strawberry = 'red';
#pineapple = 'gold';

fruit = {'apple': False, 'orange': 'orange', 'banana': 'yellow', 'strawberry': 'red', 'pineapple': 'gold'}

rand_fruit = random.choice(list(fruit))

print rand_fruit.keys()

if(rand_fruit == False):
    rand_fruit = True
    print rand_fruit
