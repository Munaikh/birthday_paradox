import random
import convert
import matplotlib.pyplot as plt
import pandas as pd

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
    return random_birthdays, temp_people_data


# Check if any birthdays in a list are duplicates
def has_duplicate(birthdays):
    seen_birthdays = set()
    duplicates = 0

    for birthday in birthdays:
        if birthday in seen_birthdays:
            duplicates += 1
        seen_birthdays.add(birthday)

    return duplicates


# Calculate the number of trials with duplicate birthdays
def num_of_duplicates(trials, num_of_people):
    # num_of_one_duplicate = 0
    # num_of_more_than_two_duplicates = 0
    num_of_duplicate = {
        "one_duplicate": 0,
        "more_than_two_duplicates": 0,
    }

    for _ in range(trials):
        # temp_people_data.clear()
        # temp_people_data will be used in here
        generated_birthdays, temp_people_data = generate_birthdays(num_of_people)

        duplicates = has_duplicate(generated_birthdays)
        if duplicates >= 1:
            num_of_duplicate['one_duplicate'] += 1
        if duplicates > 2:
            num_of_duplicate['more_than_two_duplicates'] += 1

        people_data.append(temp_people_data.copy())

    return num_of_duplicate


# Calculate the percentage of trials with duplicates
def persentage(trials, people_num=23):
    persentage = (num_of_duplicates(trials, people_num)['one_duplicate'] / trials) * 100
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
duplicates_num = num_of_duplicates(trials, people_num)
print(f"The number of trials with at least one duplicate birthday: {duplicates_num['one_duplicate']}")
print(f"The number of trials with more than two people sharing a birthday: {duplicates_num['more_than_two_duplicates']}")
# print(convert.change_dict(people_data))


# Initialize lists for the x-axis and y-axis
x_axis = []
y_axis = []

# Iterate over a range of numbers representing the number of people
for num_of_people in range(1, 101):
    # Simulate a number of trials and calculate the proportion of trials with duplicate birthdays
    proportion_duplicates = num_of_duplicates(trials, num_of_people)['one_duplicate'] / trials
    # Append the number of people to the x-axis list and the proportion of trials with duplicate birthdays to the y-axis list
    x_axis.append(num_of_people)
    y_axis.append(proportion_duplicates)

# Create a plot with the x-axis and y-axis lists
plt.plot(x_axis, y_axis)

plt.axvspan(1, 23, color='yellow', alpha=0.5)
plt.text(2, 0.3, 'In this part the graph rises slowly. \nthe chances of having duplicate birthdays are relatively low.', style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})

plt.axvspan(23, 100, color='green', alpha=0.5)
plt.text(25, 0.6, 'In this part, the graph rises rapidly. \nthe chances of having duplicate birthdays increase high. \nThis rapid rise continues- \nuntil it reaches near 1 (or 100% in terms of probability), \nwhere it starts to level off.', style='italic', bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 10})

# Label the x-axis, y-axis, and the title of the plot
plt.xlabel('Number of People')
plt.ylabel('Proportion of Trials with Duplicate Birthdays')
plt.title('Proportion of Trials with Duplicate Birthdays vs Number of People')

# Display the plot
plt.show()
