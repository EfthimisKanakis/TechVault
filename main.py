import os

def get_choice(min_value , max_value):
    valid = False 
    while valid == False:
        try: 
            choice = int(input('Choose an option: '))

            if choice >= min_value and choice <= max_value :
                valid = True
            else :
                print('invalid choice')
                print()
        except ValueError:
            print('Please enter a number!')

    return choice


def show_menu():
    print()

    print('0. to Exit')
    print('1. to Create new Note')
    print('2. to View Notes')
    print('3. to Edit a Note')


print('==========================================')
print('           Welcome to TechVault')
print('==========================================')

print()

name = input('Give your name: ')
valid1 = False
while valid1 == False:
    try:
        age = int(input('Give your age: '))
        valid1 = True
    except ValueError:
        print('Type a number!')



print()

print('Welcome ' + name + '!')
print('You are ' + str(age) + ' years old and ready to use TechVault!')

print()

show_menu()

choice = get_choice(0 , 3)


while choice != 0 :

    if choice == 1:
        title = input('Enter a title for the new note: ')
        filename = title.replace(' ', '_') + '.txt'
        if os.path.exists('notes/' + filename):
            print('This filename already exists!')
            print('=============================')
            print('Try a valid filename')
        else:
            content = input('Write what you want your note to contain: ')
            with open('notes/' + filename , 'w' , encoding='utf-8') as file:
                file.write(content)
            print('Your note: ' + title + ' ,was saved sucessfully in the note folder!')
            print()
       
    elif choice == 2 : 
        title = input('which file do you want to View?: ')
        print()
        filename = title.replace(' ', '_') + '.txt'

        try: 
            with open('notes/' + filename, 'r', encoding='utf-8') as f:
                content = f.read()
                print('================================')
                print(content)
                print('================================')
                print()
        except FileNotFoundError:
            print('This File does not exist') 
            print()
    

    elif choice == 3:
        title = input('which file do you want to Edit?: ')         
        print()
        filename = title.replace(' ', '_') + '.txt'
        if os.path.exists('notes/'+ filename):
            content = input('What do you want to add to your Note:')
            with open('notes/' + filename , 'a', encoding='utf-8') as file:
                file.write('\n' + content) 
            print('You have just updated your note!')
            print()
        else: 
            print('This file does not exists!')
            print('Type a valid filename!')
            print()

    else :
        print('invalid choice!')
        print()

    show_menu()
    choice = get_choice(0 , 3) 

print()
print('Thank you for choosing TechVault!')

