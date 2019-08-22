name = 'name'
alterEgo='alterEgo'
gender='gender'
powers='powers'

arr = [{
  name: 'Clark Kent',
  alterEgo: 'Superman',
  gender: 'Male',
  powers: ['super human strength', 'flight', 'x-ray vision', 'heat vision']
}, {
  name: 'Barry Allen',
  alterEgo: 'The Flash',
  gender: 'Male',
  powers: ['super speed', 'phasing', 'time travel', 'dimensional travel']
}, {
  name: 'Diana Prince',
  alterEgo: 'Wonder Woman',
  gender: 'Female',
  powers: ['super human strength', 'super human reflexes', 'super human agility', 'flight']
}, {
  name: 'Bruce Banner',
  alterEgo: 'The Hulk',
  gender: 'Male',
  powers: ['super human strength', 'thunder clap', 'super healing factor']
}, {
  name: 'Wade Wilson',
  alterEgo: 'Deadpool',
  gender: 'Male',
  powers: ['super healing factor', 'super human agility']
}, {
  name: 'Jean Grey',
  alterEgo: 'Phoenix',
  gender: 'Female',
  powers: ['telepathy', 'telekinesis', 'rearrange matter at will']
}, {
  name: 'Wanda Maximoff',
  alterEgo: 'Scarlet Witch',
  gender: 'Female',
  powers: ['reality manipulation', 'astral projection', 'psionic']
}]

# Alter Ego
alter_ego = [item['alterEgo'] for item in arr]
print(alter_ego)

from operator import itemgetter
from itertools import groupby 

heroes='heroes' 
# Group by Gender
group_by_gender = [ 
    {
      gender: key,
      heroes : [
        {
            name: member[name],
            alterEgo: member[name],
            powers: member[powers],
        } for member in group 
      ]
    }    
    for key, group in groupby(
        sorted(arr, key=itemgetter('gender')),
        lambda item: item[gender]
    )
]
print(group_by_gender)

# powers
powers = []
for item in arr:
    powers += item['powers']
powers = sorted(list(set(powers)))
print(powers)

body = [[item[name], item[alterEgo], item[gender] ] for item in arr]
headers = ['Name', 'Alter Ego', 'Gender'] 
transpose = [headers, *body] 
print(transpose)
