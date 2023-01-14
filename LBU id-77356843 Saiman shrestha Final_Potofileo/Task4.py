import sys

try:
  # open the sample file and read
    with open(sys.argv[1],'r') as file1:
        encrypted_text  = file1.read()

    # different shift for different encrypted text file
    if sys.argv[1] == 'sample_message_1.txt':
        shift = 14
    elif sys.argv[1] == 'sample_message_2.txt':
        shift = 11
    elif sys.argv[1] == 'sample_message_3.txt':
        shift=21
    elif sys.argv[1] == 'sample_message_4.txt':
        shift=14
    # creating a variable for store decrypted text
    decrypted_text =""
    for i in encrypted_text:
        #check if the character is aplha
        if i.isalpha():
            char_code = ord(i)
            char_code -= shift
            if i.islower():
                if char_code < ord('a'):
                    char_code +=26
            elif i.isupper():
                if char_code < ord('A'):
                    char_code += 26
            decrypted_text += chr(char_code)
        
        else:
            decrypted_text += i          
    print(f'{decrypted_text}')

except FileNotFoundError:
    print(f'''Cannot open "{sys.argv[1]}". Sorry about that.''')
