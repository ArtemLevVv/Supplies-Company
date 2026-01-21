import modules

modules.init_data()
modules.set_company_name()

def show_hud():
    info = modules.get_info()
    company = info['company']
    workers = info['workers']
    town = info['town']

    print("\n" + "="*40)
    print(f"💰 Budget: ${company['budget']} | 👷 Workers: {company['people']} | 🏭 Free: {workers['free_workers']}")
    boosts = town['boost']
    print(f"📈 Town boosts: Infrastructure {boosts['infrastructure']}, Social {boosts['social']}, Administrative {boosts['administrative']}, Industrial {boosts['industrial']}")
    print("="*40 + "\n")

def show_inventory(target='player'):
    inventory = modules.get_inventory(target=target)
    if not inventory:
        print(f"{target.capitalize()}'s inventory is empty")
        return
    print(f"{target.capitalize()}'s inventory:")
    for item, amt in inventory.items():
        print(f"  {item}: {amt}")
    print("-"*20)

def show_quests():
    quests = modules.get_info()['town']['quest_id']
    print("Available quests:")
    for qt, level in quests.items():
        print(f"  {qt.capitalize()}: Quest {level}")

def main_menu():
    while True:
        show_hud()
        print("=== MENU ===")
        print("1 - Mining 🪓")
        print("2 - Inventory 🎒")
        print("3 - Upgrade mine ⛏️")
        print("4 - Shop 🛒")
        print("5 - Company info 🏢")
        print("6 - Exit ❌")
        print("7 - Crafting 🛠️")
        print("8 - Get wood 🌲")
        print("9 - Furnace 🔥")
        print("10 - Buildings 🏠")
        print("11 - Sell everything!!! ")
        print("Q - Quests 📜")
        print("H - Help ❔")

        action = input("Choose action: ").strip().lower()

        if action == '1':
            try:
                times = int(input("How many times to mine? "))
            except:
                times = 1
            modules.mining(amount_of_work=times)

        elif action == '2':
            show_inventory()

        elif action == '3':
            modules.upgrade_mining()

        elif action == '4':
            choice = input("Sell or Buy? (1-sell / 2-buy): ").strip()
            item = input("Item: ")
            try:
                amount = int(input("Amount: "))
            except:
                print("Invalid amount")
                continue
            if choice == '1':
                modules.sell_to_shop(item, amount)
            elif choice == '2':
                modules.buy_in_shop(item, amount)

        elif action == '5':
            info = modules.get_info()
            print(info)

        elif action == '6':
            print("Exiting game...")
            break

        elif action == '7':
            item = input("Item to craft: ")
            try:
                times = int(input("Amount: "))
            except:
                times = 1
            modules.craft(item, times)

        elif action == '8':
            try:
                times = int(input("How many times to chop wood? "))
            except:
                times = 1
            modules.deforestation(amount_of_work=times)

        elif action == '9':
            material = input("Material: ")
            try:
                material_amount = int(input("How many? "))
                fuel = input("Fuel: ")
                fuel_amount = int(input("Fuel amount: "))
            except:
                print("Invalid number")
                continue
            modules.furnace(material, material_amount, fuel, fuel_amount)

        elif action == '10':
            building = input("Which building to build? ")
            modules.build(building)

        elif action == '11':
            input('sure!?')
            modules.sell_everything()
        
        elif action == '12':
            s_action = input('to you or your workers (1, 2)')
            if s_action == '1':
                tool = input('witch tool')
                modules.set_tool(tool)
            if s_action =='2':
                tool = input('witch tool')
                modules.set_tool_to_worker(tool)
        
        elif action == 'q':
            show_quests()
            type_of_quest = input("Quest type to complete: ").strip().lower()
            modules.quest(type_of_quest)

        elif action == 'h':
            print("Help menu:")
            print("1-10: actions as described")
            print("Q: view/complete quests")
            print("H: show this help")
            print("Type numbers or letters as indicated")

        else:
            print("Invalid input, try again!")

if __name__ == "__main__":
    main_menu()
