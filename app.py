from check_string import spotting_word

key_name = ["arthur"]
key_item = ["grail"]
key_colour = ["yellow"]

first_answer_input = input("What is your Name: ").lower()
if spotting_word(first_answer_input, key_name) == False:
    second_answer_input = input("what is your quest: ").lower()
    if spotting_word(second_answer_input, key_item) == True:
        third_answer_input = input("What is my favourite colour: ").lower()
        if spotting_word(third_answer_input, key_colour) == True:
            print("You may pass")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril")
    else:
        print("Only those who seek the Holy Grail may pass")
else:
    print("My Leige! You may Pass.")
