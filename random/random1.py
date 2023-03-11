import random

my_list = [1,2,3,4,5,6,7,8,9,10]
print("random from my_list (1-10)>> ", random.choice(my_list))
print("random choice from range(100) >> ", random.choice(range(100)))
print("random from randrange (10,50,3) >> ", random.randrange(10,50,3))
print("random float value between 0 <= 1 >> ", random.random())
print("randomizes the items of a list >> ", random.shuffle(my_list))
print("shuffeled list >> ", my_list)

print("random uniform >> ", random.uniform(30, 40)) # The uniform() method returns a random floating number between the two specified numbers (both included).

print(random.choices(my_list, k=2)) # [9, 4]
