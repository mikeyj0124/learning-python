# age group classification
def get_age_group(age):
    if age <= 10:
        return "child"
    elif age > 10 and age <= 55:
        return "adult"
    elif age > 55:
        return "senior"


#is movie in 3D
def is_yes(answer):
    if answer == "yes" or answer == "y":
        return True
    else:
        return False

# matinee time
def is_matinee(hour):
    if 8 <= hour < 11:
        return True
    else:
        return False

# ticket price calculation
def get_ticket_price(age_group, is_3d, is_matinee_time):
    if age_group == "child":
        price = 5.00
    elif age_group == "adult":
        if is_3d and is_matinee_time:
            price = 17.00
        elif is_matinee_time and not is_3d:
            price = 10.00
        elif is_3d and not is_matinee_time:
            price = 19.00
        else:
            price = 14.00
    elif age_group == "senior":
        price = 10.00
    return price


# customer information
def main():
    age = int(input("How old are you? "))
    age_group = get_age_group(age)
    answer_3d = input("Is this movie in 3D? ").strip().lower()
    is_3d = is_yes(answer_3d)
    has_student_id = input("Do you have a student ID? ").strip().lower()
    has_student_id = is_yes(has_student_id)
    hour = int(input("what hour is your movie? (8-23) "))
    is_matinee_time = is_matinee(hour)
    price = get_ticket_price(age_group, is_3d, is_matinee_time)
    print(price)


main()