people = {1: {'name': 'kohli', 'age': '35', 'profession': 'cricketer',"lastname":"virat"},
          2: {'name': 'rohit', 'age': '37', 'profession': 'cricketer',"lastname":"sharma"}}

new_person  =  {'name': 'dhoni', 'age': '39', 'profession': 'cricketer', "lastname":"ms"}
people[len(people)+1] = new_person
print(people)