import random # Importing the random module to randomly select a story
from colorama import Fore, Style # Importing the colorama module to add color to the output

# List of stories
stories = [
        """
        It was a {adjective} morning when {person} decided to explore the {place}. The air smelled like {food}, and the trees whispered secrets as the wind passed through them. As {person} walked along the narrow path, they suddenly heard a strange sound. Turning around, they saw a {adjective2} {animal} staring at them.

        "What are you doing here?" {person} asked. To their surprise, the {animal} replied, "I am the guardian of this place. If you wish to pass, you must prove that you can {verb} better than me!"

        Shocked but excited, {person} accepted the challenge. They took a deep breath and started to {verb} with all their might. The {animal} watched in awe and finally nodded. "Impressive," it said. "But one last challenge remains. You must {verb2} before the sun sets!"

        Without hesitation, {person} rushed to complete the final challenge. Just as the sun was about to disappear, they succeeded! The {animal} cheered and handed them a golden {food} as a reward. "You have earned my respect," it said.

        As {person} left the {place}, they knew they would never forget this {adjective} adventure.
        """,
                """
        In a quiet {place}, a {adjective} {animal} was discovered by {person}. It was unlike any other because it could {verb}! "How is this possible?" {person} wondered.

        As they got closer, the {animal} spoke: "I have been waiting for someone to {verb2} with me." Curious and excited, {person} joined in. But suddenly, a giant {food} appeared out of nowhere! The {adjective2} {animal} ran away, leaving {person} laughing at the bizarre adventure.

        That night, as {person} sat under the stars, they couldn't stop thinking about their encounter. What other secrets did the {place} hold? Would they ever meet the {animal} again? With a heart full of excitement, they decided to return the next day and see what new surprises awaited them.
        """,
                """
        Deep in the heart of {place}, {person} stumbled upon an ancient door covered in {adjective} carvings. Curiosity got the best of them, and with a gentle push, the door creaked open to reveal a hidden chamber filled with glowing {food}.

        Suddenly, a {adjective2} {animal} appeared from the shadows. "You must prove your worth by solving my riddle," it said. "What can {verb}, {verb2}, and still remain unseen?"

        {person} thought for a moment and then confidently gave an answer. The {animal} nodded, impressed. "You have done well. Now, take this {food} as a gift and go forth with wisdom."

        As {person} stepped outside, the {place} seemed brighter than before. They had uncovered one of the greatest mysteries of all time, and they knew that their adventure was only just beginning.
        """
]

# User input for the words to be used in the story
words = {
    "adjective": input("Enter an adjective: "),
    "person": input("Enter a person's name: "),
    "place": input("Enter a place: "),
    "food": input("Enter a type of food: "),
    "adjective2": input("Enter another adjective: "),
    "animal": input("Enter an animal: "),
    "verb": input("Enter a verb: "),
    "verb2": input("Enter another verb: ")
}

# Function to generate the story
def generate_story(words):
    story = random.choice(stories) # Randomly select a story from the list
    return(story.format(**words)) # Fill in the blanks in the story with the user's input

if all(words.values()): # Check if all the words have been entered
    # Output the story
    print("\n" + Fore.LIGHTCYAN_EX + "🎭 Here's your Mad Libs story:" + Style.RESET_ALL)   
    print(Fore.YELLOW+generate_story(words)+Style.RESET_ALL)
else:
    print(Fore.RED + "Please enter all the words to generate the story." + Style.RESET_ALL) # Error message if words are missing  
    

