from random import sample
import sys

try:
    #store commandline argunment into file1
    file1 = sys.argv[1]
    email_list =[]
    id_list =[]
    with open(file1,'r') as names:
        for line in names:
            #extracting id and name fro file1
            id,name = line.strip().split(' ',1)
            #splitting the name into forname and surname.
            surname,forename = name.split(',',1)
            a=forename.lower()
            #printing the fore index of forename.
            first_letter = '.'.join([i[0] for i in a.split()])
            #removing the non-alphanbet chracter from surname.
            newr = ''.join(ch for ch in surname if ch.isalpha())
            s = newr.lower()
            #printing 4 digits random numbers.
            random_digits = ''.join(str(x) for x in sample(range(4005,7000),1))
            emails = f"{first_letter}.{s}{random_digits}@poppleton.ac.uk"
            id_list.append(id)
            email_list.append(emails)
            #opening and storing the emails into another text file.
    with open('students_email.txt','a') as email:
        n = list(zip(id_list, email_list))
        for i ,j in n:
            email.write(f'{i} {j}\n')
# if error condition matches print below statements
except FileNotFoundError:
    print(f'''Error: Cannot open {sys.argv[1]}. Sorry about that.''')
except IndexError:
    print("Error: Missing command-line argument.")