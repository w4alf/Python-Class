contacts = {
    'number': 4,
    'students':
         [
            {'name': 'Sarah Holderness', 'email': 'sarah@example.com'},
            {'name': 'Harry Potter', 'email': 'Harry@example.com'},
            {'name': 'Hermione Granger', 'email': 'Hermoine@example.com'},
            {'name': 'Ron Weasley', 'email': 'ron@example.com'}
         ] 
}

print('Students Emails:')
for student in contacts['students']:
    print(student['email'])
    