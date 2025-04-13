# fortune.py - Version 1.0

print("🔮 Welcome to Sagiraju Shashank Dutt's Fortune Teller (21JE0797) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ")

if mood.lower() == "happy":
    print("✨ Your fortune: Great things await you, Shashank! Keep smiling. ✨")
elif mood.lower() == "sad":
    print("💧 Your fortune: Better days are coming, Shashank. Hang in there!")
elif mood.lower() == "neutral":
    print("🌀 Your fortune: Change is in the air, Shashank. Stay open-minded!")
else:
    print("🤷 Your fortune: Unknown path, Shashank. Tread carefully!")