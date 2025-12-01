import random

random_number=random.randint(1,10)
print("Random Numnber:",random_number)

contestants=["Vector","Sara","Carlo","Andy"]
print("The winner is:",random.choice(contestants))

cards=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
print("Picked Two Random Cards:",random.sample(cards,2))

playlist=["A","B","C","D","E","F","G"]
(random.shuffle(playlist))
print("Shuffled Playlist :",playlist)

print("Genrating a random decimal from 10.0 to 20.0:",random.uniform(10,20))