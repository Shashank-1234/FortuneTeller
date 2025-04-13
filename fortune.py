# fortune.py - Version 1.1
# A fortune teller that randomly generates fortunes based on user input and added stressed.

import random
import time

def pause(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

print("🔮 Welcome to Sagiraju Shashank Dutt's Fortune Teller (21JE0797)🔮")
name = 'Shashank'
mood = input(f"Ah, {name}... How are you feeling today? (happy/sad/neutral/stressed): ").lower()

print("\n Gazing into the crystal ball...\n")
time.sleep(2)


fortunes = {
    "happy": [
        "The stars align in your favor, {name}. Prosperity dances in your shadow today! 🌟",
        "Joy is a flame — let yours light up someone else’s world today, {name}. 🔥",
        "Your energy is contagious, {name}. A surprise blessing is on its way! 🎁"
    ],
    "sad": [
        "Even the moon hides sometimes, {name}. Your light will return. 🌘",
        "Tears water the seeds of future strength. Something beautiful is growing within you, {name}. 🌱",
        "The winds of change are shifting. Hold tight, {name} — serenity awaits. 🍃"
    ],
    "neutral": [
        "A calm sea hides hidden treasures. Dare to explore, {name}. 🧭",
        "Your path is unwritten, {name}. Each step you take is a word in your story. 📝",
        "Today is a blank canvas — will you paint, write, or dance upon it, {name}? 🎨"
    ],
    "stressed": [
        "Breathe deep, {name}. Peace is near.",
        "Take a break, {name}. You've earned it!"
    ],
    "unknown": [
        "Emotions are a spectrum, {name}. Not everything needs to fit in a box. 🎭",
        "Mystery surrounds your aura. Perhaps destiny is playing coy with you today, {name}. 🕯",
        "Complex hearts forge rare paths. Trust your inner compass, {name}. 🧭"
    ]
}

if mood in fortunes:
    fortune = random.choice(fortunes[mood])
else:
    fortune = random.choice(fortunes["unknown"])

pause(f"🔮 Your Fortune,:")
pause(fortune.format(name=name))