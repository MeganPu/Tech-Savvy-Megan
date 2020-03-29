#Exercise 5
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
team = 'New England Patriots'
print(any_lowercase1(team))

#This function only check the first character of the string and 
#will return True only if the first character in the string is
#lower case.

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

team = 'NQWWGDU'
print(any_lowercase2(team))

#This function check whether there is a lowercase in 'c', which is True, 
# instead of checking each character in the string s.

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

team = 'Thui'
print(any_lowercase3(team))

#This is a right function to check.

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

team = 'rtyuio'
print(any_lowercase4(team))

#This is a right function to check. The difference between this one and 
#the previous one is that it set flag as False at first and then make 
#flag = False or c.islower. When there is a lowercase in the string, the 
#result is Flase or True, which is still True.

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

team = 'ertyui'
print(any_lowercase5(team))

#This function is similar to the first one and only check the first character 
# of the string and will return True only if the first character 
# in the string is lower case.

ord('A')


#Exercise 6
encrypted_msg = "'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

encrypted_msg ='map'
orginal_msg = ""

for letter in encrypted_msg:
    if letter.isalpha():
        decrpted_letter = chr(ord(letter)+2)
    else:
        decrpted_letter = letter
    orginal_msg +=decrpted_letter


print(orginal_msg)
