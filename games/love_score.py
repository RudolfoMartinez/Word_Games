def play():
    print("Love game starts here...")
    # Paste your jogging dream code here


print(r'''



 _                     _       _         _   _               _    _      
| |    _____   _____  (_)___  (_)_ __   | |_| |__   ___     / \  (_)_ __ 
| |   / _ \ \ / / _ \ | / __| | | '_ \  | __| '_ \ / _ \   / _ \ | | '__|
| |__| (_) \ V /  __/ | \__ \ | | | | | | |_| | | |  __/  / ___ \| | |   
|_____\___/ \_/ \___| |_|___/ |_|_| |_|  \__|_| |_|\___| /_/   \_\_|_|   


                           ''')
print("Welcome to your love story.")
print("Will your meet-cute end in a fairytale, or will you be forever alone?")
choice1 = input(
    'You\'re at a local watering hole after work one day when you see them across the bar. Do you send them a drink? \nType "yes" to buy them a drink "no" not to.').lower()

if choice1 == "no":
    choice2 = input('Smart move. It\'s impersonal and creepy to buy a stranger a drink.'
                    'You walk over like an adult. '
                    '\nType "hi" to say hello and introduce yourself. '
                    '\nType "what\'s up" to drop your best line on them.').lower()
    if choice2 == "hi":
        choice3 = input('They smile and extend their hand to you.'
                        '\nType "shake" to shale their hand and smile.'
                        '\nType "kiss" to kiss their hand and bow like a weirdo.'
                        '\nType "lick" if you lick the back of their hand while saying, "so tender".').lower()

        if choice3 == "shake":
            print(
                "They tell you their name and offer you the seat next to them. "
                "\nYou don't know it, but this is the first date with the one person who makes your life complete"
                r'''
           .,,,,,,,,,,.
         ,;;;;;;;;;;;;;;,
       ,;;;;;;;;;;;)));;(((,,;;;,,_
      ,;;;;;;;;;;'      |)))))))))))\\
      ;;;;;;/ )''    - /,)))((((((((((\
      ;;;;' \        ~|\  ))))))))))))))
      /     /         |   ((((((((((((((
    /'      \      _/~'    ')|()))))))))
  /'         `\   />     o_/)))((((((((
 /          /' `~~(____ /  ()))))))))))
|     ---,   \        \     ((((((((((
          `\   \~-_____|      ))))))))
            `\  |      |_.---.  \       -Tua Xiong ''')
            
        if choice3 == "ignore":
            print("What kind of person can ignore an adorable dog? "
                  "\nYou wake up to your dog eating your face because he knows you're a bad human.")
        if choice3 == "kiss":
            print("They chuckle nervously before finding an excuse to leave without giving you their number. Weirdo.")
    else:
        print("They pull their hand away and gasp before punching you in the back of the head and running out of the bar."
              "\nThe bartender chases you out of the bar and never lets you back.")
else:
    print("They drink their free drink without so much as a smile in your direction. "
          "\nYou go home alone. Again. And you die that way because you have absolutely no game.")
