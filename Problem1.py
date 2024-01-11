import random
import convert


# Temporary storage for birthday data for each trial
temp_people_data = {}

# List of dictionaries containing the birthday data
people_data = []


# Generate random birthdays for a specified number of people
def generate_birthdays(num_of_people):
    possible_birthdays = 365
    random_birthdays = []
    random_names = []
    # List of random names for the random people
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

    
    # Loops through the specified number of times
    for i in range(num_of_people):
        # Generating a random birthday for a randomly chosen name and storing them in a temporary dictionary.
        random_bd = random.randrange(1, possible_birthdays + 1)
        random_name = names_list[random.randrange(0, len(names_list))]
        random_names.append(random_name)
        random_birthdays.append(random_bd)
        # If a name already exists, it adds a suffix to avoid duplicate names.
        if random_name not in temp_people_data.keys():
            temp_people_data[random_name] = random_bd
        else:
            temp_people_data[f"{random_name}-{i}"] = random_bd
    return random_birthdays


# Check if any birthdays in a list are duplicates
def has_duplicate(birthdays):
    # Creating an empty set
    seen_birthdays = set()

    # Iterate through the list of generated birthdays.
    for birthday in birthdays:
        # If a birthday already exists in the set, it means it's a duplicate.
        if birthday in seen_birthdays:
            # find the name of the preson with the same birthday
            return True
        # Add each birthday to the set.
        seen_birthdays.add(birthday)

    return False


# Calculate the number of trials with duplicate birthdays
def num_of_duplicates(trials, num_of_people):
    num_of_duplicates = 0

    # Loops through the specified number of trials
    for _ in range(trials):
        # Clearing the temporary data at the start of every trial
        temp_people_data.clear()
        # Generating new birthdays on each run.
        generated_birthdays = generate_birthdays(num_of_people)

        # Checks for duplicates and increases the counter if found.
        if has_duplicate(generated_birthdays):
            num_of_duplicates += 1
        # Copying the temporary data to the permanent people data
        people_data.append(temp_people_data.copy())
    return num_of_duplicates


# Calculate the percentage of trials with duplicates
def persentage(trials, people_num=23):
    persentage = (num_of_duplicates(trials, people_num) / trials) * 100
    return persentage


# Calculate the average percentage of duplicates over multiple runs
def average(trials, people_num=23):
    total_rate = 0

    for _ in range(10):
        total_rate += persentage(trials, people_num)

    return total_rate / 10


# Ask for number of simulation runs
trials = int(input("Enter the number of trials: "))
# Ask for number of people per run
people_num = int(input("Enter the number of people: "))


# Calculate percentage of duplicate birthdays
duplicate_probability = persentage(trials, people_num)


# Show the total number of trials simulated
print(len(people_data))

# Show the results
print(
    f"The chance of similar birthdays among 23 people is "
    f"{duplicate_probability:.2f}%"
)
# print(convert.change_dict(people_data))

