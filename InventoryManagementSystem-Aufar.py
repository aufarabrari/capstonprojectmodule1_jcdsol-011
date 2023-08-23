# Nama: Muhammad Aufar Abrari
# ID: JCDSOL-011-019
# Capstone Project Modul 1 - Gudang (Data Stok)

# Global Variable (Dictionary dalam List)
RM = [
    {'ID': '100100','Nama': 'Calcium Carbonate','Stok': 10000},
    {'ID': '100101','Nama': 'Vitamin A','Stok': 1000 },
    {'ID': '100102','Nama': 'Vitamin B Kompleks','Stok': 2000},
    {'ID': '100103','Nama': 'Vitamin C','Stok': 2000},
    {'ID': '100104','Nama': 'Iron Sulphate','Stok': 5000},
    {'ID': '100105','Nama': 'Zinc Sulphate','Stok': 5000},
    {'ID': '100106','Nama': 'Sodium Chloride','Stok': 0}
    ]
FG = [
    {'ID': '200100', 'Nama': 'Mineral Mix A','Stok': 80000},
    {'ID': '200101', 'Nama': 'Minevit A','Stok': 9000},
    {'ID': '200102', 'Nama': 'Minevit B','Stok': 10000},
    {'ID': '200103', 'Nama': 'Mineral Mix Aqua','Stok': 15000},
    {'ID': '200104', 'Nama': 'Minevit 100','Stok': 20000}
    ]

# Inventory Display Function -> Read
def rm_inventory():
    print(''' 
          >>> RAW MATERIAL INVENTORY <<<
          ''')
    print('{:<8} | {:<25} | {:<15}'.format('ID', "Nama", "Stok (Kg)"))
    print('-' * 49)
    
    for item in RM:
        print('{:<8} | {:<25} | {:<15}'.format(item['ID'], item['Nama'], item['Stok']))
    
    print('\nThis is the latest update')
              
def fg_inventory():
    print(''' 
          >>> FINISHED GOODS INVENTORY <<<
          ''')
    print('{:<8} | {:<25} | {:<15}'.format('ID', "Nama", "Stok (Kg)"))
    print('-' * 49)
    for item in FG:
        print('{:<8} | {:<25} | {:<15}'.format(item['ID'],item['Nama'], item['Stok']))
    
    print('\nThis is the latest update')

# Logistic Dept. Functions
def log_inventorycheck(): # Read
    menu = '''
    Choose Inventory to Check:
    1. Raw Material
    2. Finished Goods
    3. Back to Landing Page'''
    print(menu)
    while True:
        Entry = input('\nEnter Input: ')
        if Entry == '1':
            rm_inventory()
            print(menu)
        elif Entry == '2':
            fg_inventory()
            print(menu)
        elif Entry == '3':
            logisticpage()
            break
        else:
            print('Invalid entry. Please choose a valid option.')

def log_addinventory(): # Create
    menu='''
    Choose Inventory to Create New:
    1. Raw Material
    2. Finished Goods
    3. Back to Landing Page'''
    print(menu)
    while True:
        Entry = input('\nEnter Input: ')
        
        if Entry == '1':
            id = input('\nEnter new Raw Material ID: ')
            name = input('Enter Raw Material name: ').lower()
            found = False
            for item in range(len(RM)):
                if RM[item]['Nama'].lower() == name or RM[item]['ID'] == id:
                    found = True
                    rm_inventory()
                    break        
            if not found: 
                stock = int(input('Enter quantity amount (Kg): '))
                while True:
                    confirm = input(f'\nProceed to enter {name.title()} ({id}) for {stock} Kg to system? (Y/N)?: ')
                    if confirm.upper() == 'Y':
                        new_item = {'ID': id, 'Nama' : name.title(), 'Stok': stock}
                        RM.append(new_item)
                        print('\nData succesfully applied!\n')
                        rm_inventory()
                        log_addinventory()
                        break
                    elif confirm.upper() == 'N':
                        print('\nAdd new Raw Material data cancelled\n')
                        log_addinventory()
                        break
                    else:
                        print('Invalid entry. Please choose valid option (Y/N)')
            if found:
                print('Item(s) already exist')
                while True:
                    conf=input('Proceed to Stock Update menu? (Y/N): ')
                    if conf.upper() == 'Y':
                        log_stockupdate()
                        break
                    elif conf.upper() == 'N':
                        print('\nAdd New Raw Material Data cancelled')
                        log_addinventory()
                        break  
                    else:
                        print('Invalid entry. Please choose valid option (Y/N)')
            break
        
        elif Entry == '2':
            id = input('\nEnter new Finished Good ID: ')
            name = input('Enter finished good name: ').lower()
            found = False
            for item in range(len(FG)):
                if FG[item]['Nama'].lower() == name or FG[item]['ID'] == id:
                    found = True
                    fg_inventory()
                    break             
            if not found:  
                stock = int(input('Enter quantity amount (Kg): '))
                while True:
                    confirm = input(f'\nProceed to enter {name.title()} ({id}) for {stock} Kg to system? (Y/N)?: ')
                    if confirm.upper() == 'Y':
                        new_item = {'ID': id, 'Nama' : name.title(), 'Stok': stock}
                        FG.append(new_item)
                        print('Data succesfully applied!')
                        fg_inventory()
                        log_addinventory()
                        break
                        
                    elif confirm.upper() == 'N':
                        print('Add new Raw Material cancelled')
                        log_addinventory()
                        break
                    else:
                        print('Invalid entry. Please enter valid option (Y/N)')
            if found:
                print('Item(s) already exist')
                while True:
                    conf=input('Proceed to Stock Update page? (Y/N): ')
                    if conf.upper() == 'Y':
                        log_stockupdate()
                        break
                    elif conf.upper() == 'N':
                        print('\nRedirecting to Add New Inventory page')
                        log_addinventory()
                        break
                    else:
                        print('Invalid input! Please enter a valid option (Y/N)') 
            break
        
        elif Entry == '3':
            logisticpage()
            break
        
        else:
            print('\nInvalid input! Please enter a valid option [1-3]')

def log_stockupdate(): # Able to increase stock quantity (Update)
    menu = '''
    Choose Inventory to Update Stock:
    1. Raw Material
    2. Finished Goods
    3. Back to Landing Page'''
    print(menu)
    while True:
        Entry = input('\nEnter Input: ')

        if Entry == '1':
            rm_inventory()
            item_id = input('\nEnter Raw Material ID: ')
            found = False
            for item in range(len(RM)):
                if RM[item]['ID'] == item_id:
                    print(f'\nPlease enter amount to add for {RM[item]["Nama"]}')
                    stock_increase = int(input('Enter quantity to add (Kg): '))
                    RM[item]['Stok'] += stock_increase
                    print(f'\nAdd {RM[item]["Nama".title()]} ({item_id}) stock by {stock_increase} Kg?')
                    found = True
                    break
            if not found:
                print(f'\nID {item_id} not registered')               
                while True:
                    conf = input('Proceed to Add Inventory page? (Y/N):')
                    if conf.upper() == 'Y':
                        log_addinventory()
                        break
                    elif conf.upper() == 'N':
                        print('\nRedirecting to Stock Update menu page')
                        log_stockupdate()
                        break
                    else:
                        print('Invalid entry. Please enter valid option (Y/N)')   
            if found:
                while True:
                    confirm = input('\nProceed to update? (Y/N): ')
                    if confirm.upper() == 'Y':
                        print('\nRaw Material stock succesfully updated')
                        rm_inventory()
                        log_stockupdate()
                        break
                    elif confirm.upper() == 'N':
                        RM[item]['Stok'] -= stock_increase
                        print('\nStock update cancelled, redirecting to Stock Update menu page')
                        rm_inventory()
                        log_stockupdate()
                        break
                    else:
                        print('\nInvalid input! Please enter a valid option (Y/N)')
            break

        elif Entry == '2':
            fg_inventory()
            item_id = input('\nEnter Finished Good ID: ')
            found = False
            for item in range(len(FG)):
                if FG[item]['ID'] == item_id:
                    print(f'\nPlease enter amount to add for {FG[item]["Nama"]}')
                    stock_increase = int(input('Enter quantity to add: '))
                    FG[item]['Stok'] += stock_increase
                    print(f'\nAdd {FG[item]["Nama".title()]} ({item_id}) stock by {stock_increase} Kg?')
                    found = True
                    break
            if not found:
                print(f'\nID {item_id} not registered')
                while True:
                    conf = input('Proceed to Add Inventory Data? (Y/N):')
                    if conf.upper() == 'Y':
                        log_addinventory()
                        break
                    elif conf.upper() == 'N':
                        print('\nRedirecting to Stock Update menu page')
                        log_stockupdate()
                        break
                    else:
                        print('Invalid entry. Please choose valid option (Y/N)')
            if found:
                while True:
                    confirm = input('Proceed to update? (Y/N) ')
                    if confirm.upper() == 'Y':
                        print('Finished Good stock succesfully updated')
                        fg_inventory()
                        log_stockupdate()
                        break
                    elif confirm.upper() == 'N':
                        FG[item]['Stok'] -= stock_increase
                        print('Stock update cancelled, redirecting to Stock Update menu page')
                        fg_inventory()
                        log_stockupdate()
                        break
                    else:
                        print('\nInvalid input! Please enter a valid option (Y/N)')
            break
                  
        elif Entry == '3':
            logisticpage()
            break
        else:
            print('\nInvalid input! Please choose a valid option [1-3]')

def log_deletedata(): # Delete inventory from list 
    menu = '''
    Choose Inventory to Delete:
    1. Raw Material
    2. Finished Goods
    3. Back to Landing Page'''
    print(menu)
    while True:
        Entry = input('\nEnter Input: ')

        if Entry == '1':
            rm_inventory()
            item_id = input('\nSelect Raw Material ID to be erase: ')
            found = False
            for item in range(len(RM)):
                if RM[item]['ID'] == item_id:
                    found = True
                    while True:
                        confirm = input(f'\nAre you sure want to delete {RM[item]["Nama"]} ({item_id}) from inventory? (Y/N): ')
                        if confirm.upper() == 'Y':
                            RM.pop(item)
                            print('\nRaw Material data erased')
                            rm_inventory()
                            log_deletedata()
                            break                         
                        elif confirm.upper() == 'N':
                            print('\nData erase aborted')
                            rm_inventory()
                            log_deletedata()
                            break                           
                        else:
                            print('\nInvalid entry. Please enter valid option! (Y/N)')         
            if not found:
                print(f'\nRaw Material with ID of {item_id} not found in inventory!')
                log_deletedata()
                break
            break
            
        elif Entry == '2':
            fg_inventory()
            item_id = input('\nSelect Finished Good ID to be erase: ')
            found = False
            for item in range(len(FG)):
                 if FG[item]['ID'] == item_id:
                    found = True
                    while True:
                        confirm = input(f'\nAre you sure to delete {FG[item]["Nama"]} ({item_id}) from inventory? (Y/N): ')
                        if confirm.upper() == 'Y':
                            FG.pop(item)
                            print('\nFinished Good data erased')
                            fg_inventory()
                            log_deletedata()
                            break
                        elif confirm.upper() == 'N':
                            print('\nData erase aborted')
                            fg_inventory()
                            log_deletedata()
                            break
                        else:
                            print('\nInvalid entry. Please enter valid option! (Y/N)')
            if not found:
                print(f'\n{RM[item]["Nama"]} ({item_id}) not found in inventory')
                log_deletedata()
                break
            break
        
        elif Entry == '3':
            logisticpage()
            break

        else:
            print('\nInvalid input! Please choose a valid option [1-3]')

# PPIC Dept. Functions
def ppic_production(): # Decrease stock quantity (Update)
    intro = '''
====== Production Process ======''' 
    print(intro)
    production_data = []
    unlisted_items = []
    while True:   
        item_name = input('''
Enter the name of the raw material needed for production 
(or type "done" to finish): ''').title()
        if item_name.lower() == 'done':
            break
        found = False
        for item in range(len(RM)):
            if RM[item]['Nama'] == item_name:
                quantity = int(input(f'Enter QTY of {item_name} neeeded: '))
                if RM[item]['Stok'] >= quantity:
                    while True:
                        confirmation = input(f'\nProceed to add {item_name} ({RM[item]["ID"]}) for {quantity} Kg to Production List? (Y/N): ')
                        if confirmation.upper() == 'Y':
                            production_data.append({'Nama': item_name,'QTY': quantity})
                            RM[item]['Stok'] -= quantity
                            print(f'\n{quantity} Kg of {item_name} deducted from RM inventory.')
                            rm_inventory()
                            break
                        elif confirmation.upper() == 'N':
                            print('\nProduction Cancelled')
                            break
                        else:
                            print('\nInvalid input. Please choose a valid option! (Y/N)')
                else:          
                    print(f'\nInsufficient stock of {item_name}. Available stock: {RM[item]["Stok"]} Kg')
                found = True
                break
        if not found:
            print('\nItem unavailable, please try again')
            unlisted_items.append(item_name)
        
    print('\nProduction completed.\n')
    print('Summary:')
    for item in range(len(production_data)):
        print(f'{production_data[item]["QTY"]} Kg of {production_data[item]["Nama"]} used in production.')
    
    if unlisted_items:
        print('\nItem(s) Unavailable:')
        for unavail in unlisted_items:
            print(unavail)
            break
    ppicpage()

# Procurement Dept. Functions
def proc_autocheck(): # Read data (Raw Material) and automaticly display warning message regarding stock qty
    low_stock = []
    for item in range(len(RM)):
        if RM[item]['Stok'] <= 500:
            low_stock.append({'Nama': RM[item]['Nama'], 'ID': RM[item]['ID']})
    
    if low_stock:
        print("\nWarning! Following item(s) is running out of stock. Please re-stock immediately!: ")
        for item in range(len(low_stock)):
            print(f'{low_stock[item]["Nama"]} ({low_stock[item]["ID"]})')
    else:
        print("\nAll Raw Material stock is in acceptable level")

# Sales Dept. Functions
def sales_dataentry(): # Update data on Finished Goods (Substract)
    
    intro = '''
====== Sales Data Entry ======'''
    print(intro)
    sales_data = []
    item_unavail = []
    while True:   
        item_name = input('''
Enter Finished Good name
(or type "done" to finish): ''').title()
        if item_name.lower() == 'done':
            break
        found = False
        for item in range(len(FG)):
            if FG[item]['Nama'] == item_name:
                quantity = int(input(f'Enter QTY of {item_name} to be sold: '))
                if FG[item]['Stok'] >= quantity:
                    while True:
                        confirmation = input(f'\nProceed to sell {item_name} for {quantity} Kg? (Y/N): ')
                        if confirmation.upper() == 'Y':
                            sales_data.append({'Nama': item_name,'QTY':quantity})
                            FG[item]['Stok'] -= quantity
                            print(f'\n{quantity} Kg of {item_name} deducted from FG inventory.')
                            fg_inventory()
                            break
                        elif confirmation.upper() == 'N':
                            print('\nSales Cancelled')
                            break
                        else:
                            print('\nInvalid input. Please choose a valid option! (Y/N)')

                else:          
                    print(f'\nInsufficient stock of {item_name}. Available stock: {FG[item]["Stok"]} Kg')
                found = True
                break
        if not found:
            print('\nItem unavailable, please try again')
            item_unavail.append(item_name)
    print('\nSale completed.\n')
    print('Summary:')
    for item in range(len(sales_data)):
        print(f'{sales_data[item]["QTY"]} Kg of {sales_data[item]["Nama"]} sold.')
    
    if item_unavail:
        print('\nItem(s) Unavailable:')
        for unavail in item_unavail:
            print(unavail)
            break
    salespage()
    
# Main Menu
def MainMenu():
    menu = '''
====== Welcome to Inventory Management System ======
====== PT. AUFAR SEJAHTERA BERSAMA PURWADHIKA ======
       1. Logistic
       2. PPIC
       3. Procurement
       4. Sales
       5. Exit'''
    print(menu)
    while True:
        Entry = input('\nChoose your department: ')
        if Entry == '1':
            log_landingpage()
        elif Entry == '2':
            ppic_landingpage()
        elif Entry == '3':
            proc_landingpage()
        elif Entry == '4':
            sales_landingpage()
        elif Entry == '5':
            print('\nExiting program, have a nice day!')
            exit()
        else:
            print('Invalid entry, please choose a valid option [1-5]')
            print(menu)

# Logistic Landing Page
def log_landingpage():
    print("\nYou're about to enter Logistic Department page")
    keycode = '44421'
    attempts = 0
    while attempts < 5:
        entered_keycode = (input('Enter credential number: '))
        if keycode == entered_keycode:
            logisticpage()
            while True:
                entry = (input('\nChoose Preferred Action: '))
                if entry == '1':
                    log_inventorycheck()
                elif entry == '2':
                    log_addinventory()
                elif entry == '3':
                    log_stockupdate()
                elif entry == '4':
                    log_deletedata()
                elif entry == '5':
                    MainMenu()
                else:
                    print('Invalid entry, please choose a valid option [1-5]')
                    logisticpage()
        else:
            attempts += 1
            print(f'Invalid keycode! Remaining attempts: {5 - attempts}')
    else:
        print(f'Maximum login attempts reached. Exiting program.')
        exit()

# PPIC Landing Page
def ppic_landingpage():
    print("\nYou're about to enter PPIC Department page")
    keycode = '44321'
    attempts = 0
    while attempts < 5:   
        entered_keycode = (input('Enter credential number: ')) 
        if keycode == entered_keycode:
            ppicpage()
            while True:
                entry = (input('\nChoose Preferred Action: '))
                if entry == '1':
                    rm_inventory()
                    ppicpage()
                elif entry == '2':
                    ppic_production()
                elif entry == '3':
                    MainMenu()
                else:
                    print('Invalid entry, please choose a valid option [1-3]')
                    ppicpage()
        else:
            attempts += 1
            print(f'Invalid keycode! Remaining attempts: {5 - attempts}')
    else:
        print(f'Maximum login attempts reached. Exiting program.')
        exit()

# Procurement Landing Page
def proc_landingpage():
    print("\nYou're about to enter Procurement Department page")
    keycode = '44221'
    attempts = 0
    while attempts < 5:   
        entered_keycode = (input('Enter credential number: ')) 
        if keycode == entered_keycode:
            procpage()
            proc_autocheck()
            while True:
                entry = (input('\nChoose Preffered Action: '))
                if entry == '1':
                    rm_inventory()
                    procpage()
                elif entry == '2':
                    MainMenu()
                else:
                    print('Invalid entry, please choose a valid option [1-2]')
                    procpage()
        else:
            attempts += 1
            print(f'Invalid keycode! Remaining attempts: {5 - attempts}')
    else:
        print(f'Maximum login attempts reached. Exiting program.')
        exit()

# Sales Landing Page
def sales_landingpage():
    print("\nYou're about to enter Sales Department page")
    keycode = '44121'
    attempts = 0
    while attempts < 5:    
        entered_keycode = (input('Enter credential number: '))
        if keycode == entered_keycode:
            salespage()
            while True:
                entry = (input('\nChoose Preffered Action: '))
                if entry == '1':
                    fg_inventory()
                    salespage()
                elif entry == '2':
                    sales_dataentry()
                elif entry == '3':
                    MainMenu()
                else:
                    print('\nInvalid entry, please choose a valid option [1-3]')
                    salespage()
        else:
            attempts += 1
            print(f'Invalid keycode! Remaining attempts: {5 - attempts}')
    else:
        print(f'Maximum login attempts reached. Exiting program.')
        exit()

def logisticpage():
    print('''
========= Logistic Departement ===========
====== Choose Your Preffered Action ======
       1. Inventory Check
       2. Add Inventory
       3. Stock Update
       4. Delete Inventory
       5. Back to Main Menu''')

def ppicpage():
    print( '''
    =========== PPIC Departement =============
    ====== Choose Your Preffered Action ======
           1. Inventory Check
           2. Add Production Input
           3. Back to Main Menu''')

def procpage():
    print('''
    ========= Procurement Departement ========
    ====== Choose Your Preffered Action ======
           1. Inventory Check (Table)
           2. Back to Main Menu''')

def salespage():
    print('''
    =========== Sales Departement ============
    ====== Choose Your Preffered Action ======
           1. Inventory Check (Table)
           2. Input Sales Data
           3. Back to Main Menu''')
MainMenu()