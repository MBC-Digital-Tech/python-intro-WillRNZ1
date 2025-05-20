# starter program week 3 - perhaps this could be a task

def cooking():
    print("Meal planner")
    print()

    # change these to your favourite meals
    print("1. Chicken curry ")
    print("2. Veggie lasagne")
    print("3. Burger and salad")
    print("4. Smelly Soup")
    print()
    print("Which of these meals is your favourite? (1, 2, 3 or 4) ")
    answer = int(input())
    if answer == 1:
        print("Chicken curry coming up")
    elif answer == 2:
        print("Veggie lasagne coming up")
    elif answer == 4:
        print("Smelly soup coming up")
    else:
        print("Burger and salad coming up!")
    print("Enjoy!")
    
cooking()