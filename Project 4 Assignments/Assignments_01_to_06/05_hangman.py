import random
import string

# Word list for Hangman
word_list = [
    # Easy words
    "apple", "banana", "grape", "orange", "peach",
    "cat", "dog", "fish", "bird", "mouse",
    
    # Medium words
    "guitar", "planet", "rocket", "island", "jungle",
    "pencil", "puzzle", "tunnel", "dragon", "flower",
    
    # Hard words
    "python", "hangman", "dolphin", "zeppelin", "cyclone",
    "syndrome", "horizon", "mystery", "chimney", "crescent",
    
    # Thematic words
    "astronaut", "volcano", "avocado", "glacier", "diamond",
    "elephant", "umbrella", "penguin", "chameleon", "sapphire"
]

def main():
    word = random.choice(word_list).upper()
    word_letters = set(word)
    aplphabets = set(string.ascii_uppercase)
    used_letters = set()
    
    while len(word_letters) > 0:
        print("You have used these letters", "".join(used_letters))
        
        letter_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ''.join(letter_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in aplphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
        elif user_letter in used_letters:
           print("You have already used that letter!")
        
        else :
            print("Invalid character!")
            
    print("Congratulations! You guessed the word", word)
            
    
if __name__ == "__main__":
    main()
    

    