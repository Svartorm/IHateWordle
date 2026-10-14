import time

WHITE = 0   # Base untested letter 
GREY = 1    # Not present letter 
YELLOW = 2  # Present letter but not in pos
GREEN = 3   # Present letter in pos

alphabet = [
        ["E", 12.7],
        ["T", 9.1],
        ["A", 8.2],
        ["O", 7.5],
        ["I", 7.0],
        ["N", 6.7],
        ["S", 6.3],
        ["H", 6.1],
        ["R", 6.0],
        ["D", 4.3],
        ["L", 4.0],
        ["C", 2.8],
        ["U", 2.8],
        ["M", 2.4],
        ["W", 2.4],
        ["F", 2.2],
        ["G", 2.0],
        ["Y", 2.0],
        ["P", 1.9],
        ["B", 1.5],
        ["V", 1.0],
        ["K", 0.77],
        ["J", 0.16],
        ["X", 0.15],
        ["Q", 0.12],
        ["Z", 0.08],
        ]

keyboard = []
for letter in alphabet:
    keyboard.append([letter, WHITE, []])


# def compute_word_score(word):
#     score = 0
#     for letter in word:
#         letter = letter.upper()
#         for a in alphabet:
#             if a[0] == letter:
#                 score += a[1]
#     return score

def compute_word_score(word, keyboard):
    seen_letters = []
    score = 0
    for i, letter in enumerate(word):
        letter = letter.upper()
        for key in keyboard:
            # If key is not possible at all 
            if key[1] == GREY:
                continue
            # if key is not possible at this pos 
            if key[1] == YELLOW and i in key[2]:
                continue 

            # Else add it to the score
            if key[0][0] == letter:
                if key[0][0] in seen_letters:
                    score += key[0][1] / 2 
                else:
                    score += key[0][1]
                    seen_letters.append(key[0][0])
    return score

def find_best_word(keyboard):
    # Find the best word for the current keyboard 
    result = ""
    max_score = 0
    
    with open("../data/5-letters.txt", "r") as file:
        for line in file:
            word = line.upper()
            score = compute_word_score(word, keyboard)
            if score > max_score:
                max_score = score
                result = word

    # Return the word 
    return result

def keyboard_find(char, keyboard):
    for i in range(len(keyboard)):
        if keyboard[i][0][0] == char:
            return i
    return -1

def update_kb(word, solution, keyboard):
    for i in range(len(word)):
        # Letter is valid
        if word[i] == solution[i]:
            print(f"Letter {word[i]} is found valid ({solution[i]})")
            kbi = keyboard_find(word[i], keyboard)
            keyboard[kbi][1] = GREEN 
            keyboard[kbi][2] = [ i ]
            continue 

        # Letter is in the word 
        if word[i] in solution:
            print(f"Letter {word[i]} is found semi-valid ({solution[i]})")
            kbi = keyboard_find(word[i], keyboard)
            keyboard[kbi][1] = YELLOW
            keyboard[kbi][2].append(i)
            continue

        # Letter is not in the word 
        print(f"Letter {word[i]} is found not-valid ({solution[i]})")
        kbi = keyboard_find(word[i], keyboard)
        keyboard[kbi][1] = GREY
    return








solution = input("Enter the word to find: ").upper()

while True:
    word = find_best_word(keyboard).strip()
    score = compute_word_score(word, keyboard)
    print(f"IWH plays {word} ({score})")
    update_kb(word, solution, keyboard)

    if word == solution:
        print("Solution found!")
        break
    time.sleep(1)



# best_first_word = find_best_word(keyboard)
# print(f"The best starting word is {best_first_word}")
# while True:
#     word = input(">> ")
#     score = compute_word_score(word, keyboard)
#     print(f"Got a score of {score} points")
