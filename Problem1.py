import random
import convert
names_list = [
    "John",
    "Mary",
    "Bob",
    "Martha",
    "Linda",
    "James",
    "Elizabeth",
    "Michael",
    "Patricia",
    "William",
    "Jennifer",
    "David",
    "Barbara",
    "Richard",
    "Susan",
    "Joseph",
    "Jessica",
    "Thomas",
    "Sarah",
    "Charles",
    "Karen",
    "Christopher",
    "Nancy",
    "Daniel",
    "Lisa",
    "Matthew",
    "Betty",
    "Anthony",
    "Margaret",
    "Donald",
    "Sandra",
    "Mark",
    "Ashley",
    "Paul",
    "Dorothy",
]
temp_people_data = {}
people_data = []


def generate_birthdays(num_of_people):
    possible_birthdays = 365
    random_birthdays = []
    random_names = []

    for i in range(num_of_people):
        random_bd = random.randrange(1, possible_birthdays + 1)
        random_name = names_list[random.randrange(0, len(names_list))]
        random_names.append(random_name)
        random_birthdays.append(random_bd)
        if random_name not in temp_people_data.keys():
            temp_people_data[random_name] = random_bd
        else:
            temp_people_data[f"{random_name}-{i}"] = random_bd
    return random_birthdays


def has_duplicate(birthdays):
    seen_birthdays = set()

    for birthday in birthdays:
        if birthday in seen_birthdays:
            # find the name of the preson with the same birthday
            return True
        # if birthday in seen_birthdays and birthday < 150:
        #     return True
        seen_birthdays.add(birthday)

    return False


def num_of_duplicates(trials, num_of_people):
    num_of_duplicates = 0

    for _ in range(trials):
        temp_people_data.clear()

        # temp_people_data = {}
        generated_birthdays = generate_birthdays(num_of_people)

        if has_duplicate(generated_birthdays):
            num_of_duplicates += 1
        people_data.append(temp_people_data.copy())
    return num_of_duplicates


def persentage(trials, people_num=23):
    duplicate_rate = (num_of_duplicates(trials, people_num) / trials) * 100
    return duplicate_rate


def average(trials, people_num=23):
    total_rate = 0

    for _ in range(10):
        total_rate += persentage(trials, people_num)

    return total_rate / 10


trials = int(input("Enter the number of trials: "))
people_num = int(input("Enter the number of people: "))


duplicate_probability = persentage(trials, people_num)
print(convert.change_dict(people_data))
print(len(people_data))
print(
    f"The chance of similar birthdays among 23 people is "
    f"{duplicate_probability:.2f}%"
)
