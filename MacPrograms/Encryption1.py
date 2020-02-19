import random
print('What is your message?')
message = input()
message2 = ''
for i in range(len(message)):
    message2 = message2+chr(int((ord(message[i]))+2))
print('Here is your encypted message:\n'+str(message2)+'\nHere is your decryption code:\n'+str(2))
