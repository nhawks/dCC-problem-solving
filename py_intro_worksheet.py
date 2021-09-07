import random

# #* Python Intro Worksheet
#1. Write a function that takes in a list of programming languages and prompts the user for their
# favorite programming language. If the user’s favorite programming language exists in the list,
# return it and print the returned result to the console.

def users_favorite_programming_language(languages_list):
    user_choice = input(
        "Please enter your favorite programming languague: ").lower()
    if user_choice in languages_list:
        return print(user_choice)
    else:
        return print("Not in the list")


programming_languages = ["python", "javascript", "c#", "java", "c++", "c", ]
# users_favorite_programming_language(programming_languages)

# ---------------------------------------------------------------------------------------------
#2. Write a function that takes in a minimum number and maximum number, and return a random
# number between the minimum and maximum range

def generate_random_number(min_num, max_num):
    random_number = random.randint(min_num, max_num)
    return print(random_number)

minimum_number = 1
maximum_number = 100
# generate_random_number(minimum_number, maximum_number)

# -----------------------------------------------------------------------------------------------
#3. Write a function that takes in a word and return the reversal of that word.

def get_reversed_word(word):
    reversed_word = ""
    word = [letter for letter in word]
    word.reverse()
    reversed_word = reversed_word.join(word)
    return print(reversed_word)

word = "python"
# get_reversed_word(word)

# ------------------------------------------------------------------------------------------------
#4. Write a function that prints every number from 100 to 1 (descending).
# c. If the number is divisible by 4 and 7, print “Flamingo -Banana!”
# b. If the number is divisible by 7, print “Flamingo” instead of the number
# a. If the number is divisible by 4, print “Banana” instead of the number

def banana_flamingo(max_number):
    num_array = [number for number in range(1, max_number)]
    num_array.reverse()
    for number in num_array:
        if number % 7 == 0 and number % 4 == 0:
            print("Flamingo-Banana!")
        elif number % 7 == 0:
            print("Flamingo")
        elif number % 4 == 0:
            print("Banana")
        else:
            print(number)

# banana_flamingo(101)

#------------------------------------------------------------------------------------------------
#5. Write a function that takes in a list of numbers. Return a new list that contains only the
# elements that are less than 5. Print to the console the contents of the returned list.
# a. [1, 2, 3, 7, 8, 9, 45, 134, 43, 2, 3, 1, 6, 7, 5, 4]
# i. Bonus for fun: No duplicates in the new list.

def list_of_nums_less_than_five (num_list):
  new_list = []
  for number in num_list:
    if number in new_list:
      continue
    elif number < 5:
      new_list.append(number)
  return print(new_list)

n = [1, 2, 3, 7, 8, 9, 45, 134, 43, 2, 3, 1, 6, 7, 5, 4]
# list_of_nums_less_than_five(n)

# ------------------------------------------------------------------------------------------------
#6. Write a function that prompts the user for their name and age, and then prints out the user’s
# name and the year they will turn 100 years old.

def user_name_and_age():
    user_first_name = input("Please enter your first name: ")
    user_age = int(input("Please enter your age: "))
    current_year = int(input("Please enter the current year: "))
    birth_year = current_year - user_age
    year_user_turns_100 = birth_year + 100
    return print(f"Hello {user_first_name}! You'll turn 100 in year {year_user_turns_100}.")

# user_name_and_age()

# ---------------------------------------------------------------------------------------------------
#7. Write a function that returns a list that contains only the elements that are common between
# the lists (without duplicates). Make sure your program works on two lists of different sizes.
# Examples of two lists:
# i. a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# ii. b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# iii. Bonus for fun: Randomly generate two lists to test this.

def common_elements_between_two_lists(list_one, list_two):
    common_elements_list = []
    for i in list_one:
        for j in list_two:
            if i in common_elements_list or j in common_elements_list:
                continue
            elif j == i:
                common_elements_list.append(j)
    return print(common_elements_list)

list_one = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_two = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# common_elements_between_two_lists(list_one, list_two)
# Bonus
def random_number_list_generator():
    random_list = []
    array_length = random.randint(5, 15)
    for x in range(1, array_length):
        number = random.randint(1, 10)
        random_list.append(number)
    return random_list


random_list_one = random_number_list_generator()
random_list_two = random_number_list_generator()
# common_elements_between_two_lists(random_list_one, random_list_two)

# -----------------------------------------------------------------------------------------------------
#8. Write a function that takes in two words and determines if the two words are an anagram of each other.
# a. An anagram is a word or phrase that is formed by rearranging the letters of another word or phrase.
# b. Assume any word that is passed in is a word that exists in the English language
# c. If the two words are an anagram, return true. Otherwise, return false.

def is_anagram (word_one, word_two):
  word_one = word_one.lower()
  word_two = word_two.lower()
  # word_one = word_one.replace(" ", "")
  # word_two = word_two.replace(" ", "")
  anagram_chars = list(word_one)
  if len(word_one) != len(word_two):
    return False
  for char in word_two:
    if char in anagram_chars:
      continue
    else:
      return False
  return True

word_one = "silent"
word_two = "listen"
# print(is_anagram(word_one, word_two))

# ----------------------------------------------------------------------------------------------------
#9. Write a function that takes in a phrase and reverse each word inside the string, but keeps the
# same order of the phrase.
# a. “Hello world I am a programmer”
# b. “olleh dlrow I ma a remmargorp”

def get_reversed_phrase (phrase):
  phrase = phrase.split()
  reversed_phrase = []
  for word in phrase:
    reversed_phrase.append(word[::-1])
  return " ".join(reversed_phrase)

phrase = "Hello world I am a programmer"
# print(get_reversed_phrase(phrase))

# -----------------------------------------------------------------------------------------------------
#10. Print downward Pyramid Pattern with Star (asterisk).
# a. *****
# ****
#  ***
#  **
#  *
# b. Bonus for fun: Allow user input to decide how many stars on the first row.

def print_pyramid_pattern (pattern):
  for x in pattern:
    print(x)

pyramid_pattern = ["*****", "****", "***", "**", "*"]
# print_pyramid_pattern(pyramid_pattern)

