#for loop exercise

#you're having a party and want to invite your friends
#you want the print out invitations for each friend using for loops
#the names are in two lists, 'names' and 'names1'
#you also need to add two extra names to the list using an 'input' box, when you run the code
#printout one invitation to each friend per line
#names should be properly capitalized

#printout: Name! You are invited to the party on saturday.

names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
names2 = [input('First name'), input('Second Name')]

names_total = names + names1 + names2

for nome in names_total:
    print(f'{nome.capitalize()}! You are invited to the party on saturday.')

print('End of guests.')



 