import random
import array
while True:
    print("")
    print("")
    print("                                               ------PASSWORD GENERATOR------    ")
    print("          ")
    print("")
    print("GENERATE A PASSWORD-> (1)")
    print("EXIT -> (2)")
    choice=int(input("choice: "))
    if choice==1:
        pass_length=int(input("ENTER THE LENGTH OF THE PASSWORD:"))
        if pass_length>=12:
            D = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

            uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

            symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', 
		'*', '(', ')',]

            everything = D+ lowercase + uppercase + symbols
            rand_digit = random.choice(D)
            rand_upper = random.choice(uppercase)
            rand_lower = random.choice(lowercase)
            rand_symbol = random.choice(symbols)
            temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
            for x in range(pass_length - 4):
                    temp_pass = temp_pass + random.choice(everything)
                    temp_pass_list = array.array('u', temp_pass)
                    random.shuffle(temp_pass_list)
            password = ""
            for x in temp_pass_list:
                    		password = password + x
            print("")
            print("")
            print("YOUR NEWLY GENERATED PASSWORD :",password)
        else:
            D = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

            uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

            symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', 
		'*', '(', ')',]

            everything = D+ lowercase + uppercase + symbols
            rand_digit = random.choice(D)
            rand_upper = random.choice(uppercase)
            rand_lower = random.choice(lowercase)
            rand_symbol = random.choice(symbols)
            temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
            for x in range(pass_length - 4):
                    temp_pass = temp_pass + random.choice(everything)
                    temp_pass_list = array.array('u', temp_pass)
                    random.shuffle(temp_pass_list)
            password = ""
            for x in temp_pass_list:
                    		password = password + x
            print("")
            print("YOUR NEWLY GENERATED PASSWORD :",password)
            print("WEAK PASSWORD !")
    elif choice==2:
        break
