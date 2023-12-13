# ============================================== Case Study 01 =========================================================
# =========================================== 'UniBuddy' Chat Bot ======================================================
# *********************************************** E. Thompson **********************************************************

"""
Case Study Story:
Imagine the first day of university for a freshman named Alex.
Alex is excited but also overwhelmed by the vast campus, numerous courses, and the sea of new faces.
To aid new students like Alex, the university's IT department has developed a personalised chatbot.
This chatbot, named "UniBuddy", is designed to make the transition smoother for freshmen.
Upon accessing the chatbot, Alex is prompted to enter their name, favourite colour, and age.
Based on this input, UniBuddy offers a personalised greeting.
For instance, if Alex's favourite colour is blue,
    UniBuddy might suggest joining the university's "Blue Art Club".
If Alex is 18, the chatbot might provide information about freshman-specific events.
The chatbot also offers a feature where Alex can input specific queries, like "Where is the library?"
    or "How do I join the debate club?",
        and UniBuddy responds with relevant information, all while adhering to a friendly tone,
        using string transformation methods to ensure the responses feel personalised and engaging.
"""

# --------------------- Initial messages shown to the user: ------------------------------------------------------------

print("""
Welcome to UniBuddy! Here you can find out more about what's going on 
at our university and have your burning questions answered!

Please enter your details to start!
""")

while True:
    try:
        user_name = input("Please enter your first name : ").capitalize()
        user_age = int(input("Please enter your age : "))
        fav_colour = input("Please enter your favourite colour : ").lower()

        if not user_name.isalpha():
            print("Are you sure that's your first name? Please try again.\n")
        elif not fav_colour.isalpha():
            print("Sorry, I don't recognise that colour! Please try again.\n")
        else:
            break
    except ValueError as err:
        print("You haven't entered a number as your age! Please try again.\n")

print(f"""
Hi, {user_name}!

You have chosen a great university, I can't wait to tell you more!

You said that your favourite colour is '{fav_colour}' and I have some brilliant 
suggestions for you, based on your choice!
""")

# ---------------------- Personalised responses to favourite colour: ---------------------------------------------------

if fav_colour == "red":
    print("If you like red, you'll want to check out these:")
    print("""
    - The Traffic Jam Appreciation Society
    - The Communist Club
    - Our Anger Management Group
    """)

elif fav_colour == "orange":
    print("If you're into orange, you might also be into:")
    print("""
    - The Breakfast Club (free orange juice every Wednesday morning!)
    - The Basketball Team
    - The Citrus Tree Growing Club
    """)

elif fav_colour == "yellow":
    print("If yellow is your thing, you might just love:")
    print("""
    - The Citrus Tree Growing Club
    - The Cheese Appreciation Society
    - The University's Brass Band
    """)

elif fav_colour == "green":
    print("If you like green, you'll want to check out these:")
    print("""
    - The Gardening Club
    - The Cross Country Running Team
    - The Salad Appreciation Society
    """)

elif fav_colour == "blue":
    print("Things to check out if you're not feeling blue, but like blue things:")
    print("""
    - The Swimming Team
    - The Cloud Shape Spotting Club
    - The University Sports Teams, Go Blue Whales!
    """)

elif fav_colour == "pink":
    print("I'm sure you'll be tickled pink with these ideas!:")
    print("""
    - The Barbie Appreciation Society
    - The Pink Panther Club
    - The Debating Club (You'll be pink in the face after all that arguing!)
    """)

elif fav_colour == "purple":
    print("Purple is such a regal choice of colour, you might enjoy these:")
    print("""
    - The Royal Family Appreciation Society
    - The Prom Committee (help plan our balls and choose our King and Queen!)
    - The University's Orchestra
    """)

elif fav_colour == "black":
    print("If you're not too busy having an existential crisis, lovers of black often tolerate:")
    print("""
    - The Drama Club
    - The Goth Society
    - The Dramatic Poetry Group
    """)


elif fav_colour == "white":
    print("White is such a pure choice, you might like these:")
    print("""
    - Our Library's Book Club
    - The Cleaning Club (they love to scrub!)
    - The Guardian Angel Society
    """)

elif fav_colour == "brown":
    print("Brown is a bit of an odd choice for a favourite colour, but I won't judge. You might like:")
    print("""
    - The Chocolate Society (yum!)
    - The Mud Wrestling Team
    - The River Wading Club (includes magnet fishing activities!)
    """)

else:
    print(f"Actually, I'm sorry, I don't know the colour {fav_colour}... Please try again.")

# ---------------------- Personalised responses to age: ----------------------------------------------------------------

if user_age <= 22:

    print("Here are some fresher's events you might want to go to!")
    print("""
    - The Fresher's Fair, where you can find out about and sign up for the clubs and 
      societies I suggested!
    - The Fresher's Ball (tickets are available from the Student Union)
    - New Student's Coffee Mornings, meet other new students and chat over coffee and cake.
    """)

else:

    print("Also, you might like to go to these events!")
    print("""
    - Wine Tasting evening, an event for mature students to meet and mingle.
    - The Grand Concert, a full day of music from our bands and orchestra, completely free.
    - Clubs and Coffee, a quiet event where you can find about and sign up for 
      the clubs and societies I suggested.
    """)

# ---------------------- FAQ (Frequently asked questions) : ------------------------------------------------------------

question = input(f"""
I hope that I have been useful to you so far, {user_name}.

Are there any questions that you would like to ask me?
I can answer questions like 'How do I join a club?' or 'When is... event?'.
If not, please type 'q' to quit: """).lower()

while question != "q":

    if question == "where is the library?":
        print("\nThe library is on Main Street, opposite the Student Union building. Look for the green glass doors.")

    elif question == "where is the student union?":
        print("\nThe Student Union is the ugly concrete monstrosity on Main Street, opposite the Library.")

    elif question == "how do i join a club?" or question == "how do i join a society?":
        print("""
To sign up for clubs and societies, you can go along to the Fresher's Fair or the Clubs and Coffee event.
Alternatively, log into the Student Union website and you can sign up online!""")

    elif question == "how do i join a team?":
        print("""
To sign up for a team, you can go along to the Fresher's Fair or the Clubs and Coffee event.
Alternatively, contact the Sport Centre's Office - their contact details are on the Student Union website.
There are try-outs for the more popular teams, so bring your A-game!""")

    elif question == "how do i join a group?":
        print("""
To join groups, you can go along to the Fresher's Fair or the Clubs and Coffee event.
You can also simply turn up! The Student Union website and the library noticeboard will 
have details of when and where.""")

    elif question == "when is the fresher's ball?":
        print("\nThe ball is on Saturday 31st November, starting at 7pm.")

    elif question == "how much are fresher's ball tickets?" or \
            question == "how much are tickets for the fresher's ball?":
        print("\nTickets for the Fresher's Ball are £50 each, and include transport, food, and a complimentary drink!")

    elif question == "when is the fresher's fair?":
        print("\nThe Fresher's Fair will be held all day Friday and Saturday.")

    elif question == "where is the fresher's fair?":
        print("\nThe Fresher's Fair will be held in the Student Union's Main Hall.")

    elif question == "when is the coffee morning?" or question == "when are the coffee mornings?":
        print("\nCoffee mornings are every weekday morning from 9 to 11 am. Coffee is the best!")

    elif question == "where is the coffee morning?" or question == "where are the coffee mornings?":
        print("\nCoffee mornings are all held in the lovely Library Cafe.")

    elif question == "when is the wine tasting evening?":
        print("\nThe Wine Tasting Evening is on Saturday, it starts at 8pm. There will be cheese too!")

    elif question == "where is the wine tasting evening?":
        print("\nThe Wine Tasting is being held in the bar at the Student Union.")

    elif question == "when is the grand concert?":
        print("\nThe Grand Concert is on the last Sunday of the month.")

    elif question == "where is the grand concert?":
        print("\nThe concert will take place in the Student Union's Hall.")

    elif question == "when is the clubs and coffee event?":
        print("\n'Clubs and Coffee' will take place every Tuesday, 10 - 12pm, for the next 4 weeks.")

    elif question == "where is the clubs and coffee event?":
        print("\nThis event will be held in the Library's Cafe.")

    else:
        print("\nI'm afraid I am unable to answer that question, please try another.")

    question = input("\nFeel free to ask me another question, or type 'q' to quit: ").lower()

print(f"\nThank you for talking to me today {user_name}, I hope you found our chat useful!")
