# record all cards
card_list = []


def show_menu():
    """display the menu"""

    print("*" * 50)
    print("welcome")
    print()
    print("1.add a new card")
    print("2.display all cards")
    print("3.search a card")
    print()
    print("0.exit system")
    print("*" * 50)


def add_new_card():
    """add a new card"""
    print("add a new card")

    # 1. remind user to enter card info
    name_str = input("please enter the name:")
    phone_str = input("please enter the tel No.:")
    qq_str = input("please enter the qq:")
    email_str = input("please enter the email:")

    # 2. create a card dict
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str
                 }
    # 3. add card dict to card_list
    card_list.append(card_dict)
    # 4. remind add successful
    print("add %s card successful!" % name_str)


def show_all_cards():
    """display all cards"""
    for name in ["name", "tel", "qq", "email"]:
        print(name, end="\t\t")
    print()
    print("=" * 50)

    # check  whether card exists
    if len(card_list) == 0:
        print("no record!")
        return

    # print("show all cards")
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))


def search_card():
    """search card"""
    print("search a card")
    # 1.remind user to input username
    name_str = input("please enter the username you want to search:")
    # 2.search list if not found remind user
    for card_dict in card_list:
        if card_dict["name"] == name_str:
            for name in ["name", "tel", "qq", "email"]:
                print(name, end="\t\t")
            print()
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            deal_card(card_dict)
            break
    else:
        print("the user %s is not found" % name_str)


def deal_card(find_dict):

    action_str = input("please input your operation: [1]modify [2]delete [0]return")

    if (action_str == "1"):
        pass
    elif (action_str == "2"):
        card_list.remove(find_dict)
        print("%s is deleted!" % find_dict["name"])
