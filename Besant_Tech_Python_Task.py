
# Define a function to categorize the person
def categorize_person(name, age):
    # Use string slicing to get the first and last letters of the name
    first_letter = name[0]
    last_letter = name[-1]
    
    # Determine if the age is young, middle-aged, or old
    if age < 30:
        category = "Young"
    elif 30 <= age <= 60:
        category = "Middle-Aged"
    else:
        category = "Old"

    # Use string slicing and check if the number of letters in name is even or odd
    name_length = len(name)
    if name_length % 2 == 0:
        name_length_category = "Even number of letters"
    else:
        name_length_category = "Odd number of letters"

    # Return the result as a dictionary
    return {
        "first_letter": first_letter,
        "last_letter": last_letter,
        "category": category,
        "name_length_category": name_length_category,
        "name_length": name_length
    }

# Function to interact with villagers
def magic_calculator():
    
    villagers = []
    
    # Let's add 5 villagers for the demonstration
    villagers.append({"name": "Divya", "age": 25})
    villagers.append({"name": "Madhur", "age": 24})
    villagers.append({"name": "Parul", "age": 44})
    villagers.append({"name": "Sameer", "age": 56})
    villagers.append({"name": "Sneha", "age": 70})

    # Loop over each villager and categorize them
    for villager in villagers:
        name = villager["name"]
        age = villager["age"]

        # Call the categorize_person function for each villager
        result = categorize_person(name, age)
        
        # Print the results for the villager
        print(f"  Villager: {name}, Age: {age}")
        print(f"  First Letter: {result['first_letter']}")
        print(f"  Last Letter: {result['last_letter']}")
        print(f"  Category: {result['category']}")
        print(f"  Name Length: {result['name_length']} ({result['name_length_category']})")
        print("-" * 40)

# Run the magic calculator
magic_calculator()
