import modules

modules.init_data()
modules.set_company_name()

run = True

while run:
    print('GAME: make your choice \nGAME: 1 - mining\nGAME: 2 - see inventory\nGAME: 3 - upgrade mine\nGAME: 4 - visit shop\nGAME: 5 - to see info\nGAME: 6 - EXIT')
    print('GAME: 7 - crafting\nGAME: 8 - get wood\nGAME:9 - furnace\nGAME:10 - building')
    action = input()
    
    if action == '1':
        modules.mining()
        
    elif action == '2':
        inventory = modules.get_inventory()
        print(inventory)
        
    elif action == '3':
        modules.upgrade_mining()
    
    elif action == '4':
        choice= input('Do you want to sell or to buy\n(1 or 2) ')
        if choice == '1':
            item = input('what item?: ')
            amount = input('how many?: ')
            modules.sell_to_shop(item, amount)
        elif choice == '2':
            item = input('what item?: ')
            amount = input('how many?: ')
            modules.buy_in_shop(item, amount)
            
    elif action == '5':
        print(modules.get_info())
    
    elif action == '6':
        run = False
        
    elif action == '7':
        item = input('which item? ')
        amount = input('how many? ')
        modules.craft(item, amount)
    
    elif action == '8':
        modules.deforestation()
    
    elif action == '9':
        material = input('material? :')
        material_amount = int(input('how many? :'))
        fuel = input('fuel? :')
        fuel_amount = int(input('how many? :'))
        modules.furnace(material= material, material_amount= material_amount, fuel= fuel, fuel_amount= fuel_amount)
    elif action == '10':
        building = input('what do you want to build')
        modules.build(building)
        