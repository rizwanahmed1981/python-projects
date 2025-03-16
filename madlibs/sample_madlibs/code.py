def madlibs():
    body_part = input("Body Part: ")
    verb = input("Verb : ")
    adj1 = input("adjective 1: ")
    adj2 = input("adjective 2: ")
    adj3 = input("adjective 3: ")
    adj4 = input("adjective 4: ")
    adj5 = input("adjective 5: ")
    noun1 = input("Noun 1:")
    noun2 = input("Noun 2:")
    noun_plural_1 = input("Noun (Plural_1): ")
    noun_plural_2 = input("Noun (Plural_2): ")

    madlib = f"I love computer programming because it's {adj1}! The journey to becoming a \
good programmer starts with hope in your mind and a dream in your {body_part}. Through blood, \
sweat, and {noun_plural_1}, hopefully it never ends. Yes, once you learn to {verb}, it becomes \
a part of your life identity and you can become a super {adj2} hacker. Knowledge of programming \
lets you take control of your {noun1}. You can create your own personal {noun_plural_2}, anything \
from developing {adj3} software to analyzing data and making predictions about the {noun2}. You can \
maybe even recreate Jarvis and make him extra {adj4}. I hope you'll start your {adj5} journey by \
coding with Kylie :)"
    
    print(madlib)