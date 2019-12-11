#! /usr/bin/python3

import card_tools
while True:
    # show the menu
    card_tools.show_menu()
    action_str = input("please enter your operation:")

    # 1,2,3 is the operation for card
    if action_str in ["1", "2", "3"]:

        # create a new card
        if action_str == "1":
            card_tools.add_new_card()
        # show all
        if action_str == "2":
            card_tools.show_all_cards()
        # query card
        if action_str == "3":
            card_tools.search_card()
        print("your operation is %s" % action_str)
        pass

    # 0 exit system
    elif action_str == "0":
        print("see you!")
        break

    # others will remind user error
    else:
        print("your operation is not allowed please enter again!")
