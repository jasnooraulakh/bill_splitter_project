import random

# write your code here

def lucky_one(name_list):
    random_name = random.choice(name_list)
    return random_name

print("Enter the no. of friends: ")
no_of_guests = int(input())

if no_of_guests <= 0:
    print("No one is joining for the party")

else:
    names = []

    print("Enter the name of every friend (including you), each on a new line:")

    for i in range(no_of_guests):
        friend_name = input()
        names.append(friend_name)

    print("Enter the total bill value:")
    bill_total = float(input())

    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    lucky_response = input()
    lucky_guest = None

    if lucky_response == 'Yes':
        lucky_guest = lucky_one(names)
        print(f"{lucky_guest} is the lucky one!")
        no_of_guests -= 1
    else:
        print("No one is going to be lucky")

    split_total = round((bill_total / no_of_guests), 2)

    friend_dict = {name: 0 if name == lucky_guest else split_total for name in names}

    print(friend_dict)


