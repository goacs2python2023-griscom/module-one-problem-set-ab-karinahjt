def win_prob(rolls, faces):
    print("Rolls: ", rolls)
    print("Die faces: ", faces)
    rolls_list = rolls.split()
    faces_list = faces.split()
    # expected roll
    r1, r2 = rolls_list[0], rolls_list[1]
    r1_count = faces_list.count(r1)
    r2_count = faces_list.count(r2)
    probability = (r1_count/6) * (r2_count/6)
    return probability

"""
print("Probability: ", win_prob("A C", "A B C D E F"))
print("Probability: ", win_prob("A C", "A B C C E F"))
print("Probability: ", win_prob("A C", "A B C C C F"))
print("Probability: ", win_prob("1 5", "1 2 4 4 6 5"))
print("Probability: ", win_prob("3 3", "1 2 3 3 3 6"))
print("Probability: ", win_prob("1 1", "1 1 1 1 1 1"))
print("Probability: ", win_prob("2 2", "1 2 3 4 5 6"))
print("Probability: ", win_prob("1 3", "3 3 3 3 3 3"))
"""

print('Enter your expected rolls:')
rolls = input()
print('Enter your dice faces:')
faces = input()
print("Probability: ", win_prob(rolls, faces))