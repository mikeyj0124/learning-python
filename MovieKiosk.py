# age group classification
def get_age_group(age):
    if age <= 10:
        return "child"
    elif age > 10 and age <= 55:
        return "adult"
    elif age > 55:
        return "senior"

def is_yes(answer):
    if answer == "yes" or answer == "y":
        return True
    else:
        return False

# asking age
def main():
    age = int(input("How old are you? "))
    age_group = get_age_group(age)
    answer_3d = input("Is this movie in 3D? ").strip().lower()
    is_3d = is_yes(answer_3d)
    print(is_3d)

main()