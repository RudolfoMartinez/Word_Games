def play():
    print("Love score game starts here...")
    # Paste your love score code here
def calculate_love_score(name1, name2):
    # Combine and lowercase both names
    combined_names = (name1 + name2).lower()

    # Count letters in "TRUE"
    true_score = 0
    for letter in "true":
        true_score += combined_names.count(letter)

    # Count letters in "LOVE"
    love_score = 0
    for letter in "love":
        love_score += combined_names.count(letter)

    # Combine the scores to get the final score (as a 2-digit number)
    final_score = int(str(true_score) + str(love_score))

    print(f"Your love score is {final_score}")