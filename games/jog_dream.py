def play():
    print("Jogging dream game starts here...")
    # Paste your jogging dream code here
print(r'''
 
                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     /,  `\_/
                 |     \'
 pb  /\_        /`      /\
   /' /_``--.__/\  `,. /  \
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \
                            `\ \
                              \_\__
                               \___)
    
                           ''')
print("Welcome to your morning jog.")
print("Your mission is to run five miles.")
choice1 = input(
    'You\'re tying your shoes before your morning jog. Do you double knot them? \nType "yes" to double tie them or "no" not to.').lower()

if choice1 == "no":
    choice2 = input('You leave your apartment and head towards the park.'
                    'There is a attractive person jogging the other way. '
                    '\nType "ignore" to keep jogging. '
                    '\nType "look" to turn around and watch them jog past you.').lower()
    if choice2 == "ignore":
        choice3 = input('You keep jogging through the park when you see an adorable dog all by itself.'
                        '\nType "pet" to stop and pet the adorable dog.'
                        '\nType "ignore" if you hate dogs and are a miserable human being.'
                        '\nType "perv" if you try to find the attractive person you saw jogging past you earlier.').lower()

        if choice3 == "pet":
            print("After playing with the adorable dog you wake up smiling and happy and find your dog is licking your face in bed next to you. "
                  "\nYou go on to have the best day because you have a dog and don't have to jog. You win at life."
                  r'''
                ."";._   _.---._   _.-"".
               /_.'_  '-'      /`-` \_   \
             .'   / `\         \   /` \   '.
           .'    /    ;    _ _  '-;    \   ;'.
        _.'     ;    /\   / \ \    \    ;  '._;._
     .-'.--.    |   /  |  \0|0/     \   |        '-.
    / /`    \   |  /  .'             \  | .---.     \
   | |       |  / /--'   .-"""-.      \ \/     \     |
   \ \      /  / /      (  , ,  )     /\ \      |    /
    \ '----' .' |        '-(_)-'     |  | '.   /    /
     `'----'`   |                    '. |   `'----'`
            jgs \                      `/
                 '.         ,         .'
                   `-.____.' '.____.-'
                          \   /
                           '-'
    
                           ''')
        if choice3 == "ignore":
            print("What kind of person can ignore an adorable dog? "
                  "\nYou wake up to your dog eating your face because he knows you're a bad human.")
        if choice3 == "perv":
            print("You can't play my game anymore. Just go away. You lose.")
    else: print("You run into a tree and wake up in a bad mood."
                "\nIt sets a bad tone for the rest of your day because you feel bad for being a creeper.")
else: print("You fall over, face first onto the floor and wake startled realizing it was a horrible dream. "
            "\nIt sets bad tone for the rest of your day because, eww, who the hell likes jogging?")


