
from time import ctime

# this class used for identifying items in the restauraunt
class new_Item:
    def __init__(self,Description,Btn_Description,Price,Qty):
        self.Description=Description
        self.Btn_Description=Btn_Description
        self.Price=Price
        self.Qty=Qty
    def price(self,previousPrice):
        return (previousPrice+(self.Price*self.Qty))
# this class holds employee name ,ID, password and registeration time
# encyrtyp fnction creates Cipher class which defined sepatedly below

class Registeration:
    def __init__(self,Name,ID,Password,Registeration_Time):
        self.Name=Name
        self.ID=ID
        self.Password=Password
        self.Registeration_Time=Registeration_Time
        self.Login_Time=""
        self.Clock="Clocked Off"
        self.Button_x=0
    def encrypt(self):
        ID_encryption=Cipher(Encrypt_phrase=self.ID,Decrypt_phrase=None)
        Password_encryption=Cipher(Encrypt_phrase=self.Password,Decrypt_phrase=None)
        self.ID=ID_encryption.encrypt()
        self.Password=Password_encryption.encrypt()
    def check(self,ID,Password):
         if ID==self.ID and Password==self.Password:
            return "ID and Password Matched"
         elif ID==self.ID:
            return "ID Matched"
         elif ID!=self.ID and Password!=self.Password:
            return "No Match"
    def Clock_On(self):
        self.Clock="Clocked On"
        self.Login_Time=ctime()
    def Clock_Off(self):
        self.Clock="Clocked Off"
        self.Login_Time=ctime()
    def set_Button_index(self,index):
        self.Button_x=index
    def get_Button_index(self):
        return self.Button_x
# this class encrypts and decrypt given Encrypt_phrase and Decrypt_phrase
# it is the same function that is used in assigment 1
class Cipher:
    def __init__(self,Encrypt_phrase=None,Decrypt_phrase=None):
        self.Encrypt_phrase=Encrypt_phrase
        self.Decrypt_phrase=Decrypt_phrase
        self.Encrypted_phrase=""
        self.Decrypted_phrase=""
        self.characters="0123456789"                   # saves English lowercase Alphabet in a string
        self.location_in_characters=0
        self.reversed_phrase=""
        self.Distance=4
    def reverse(self,phrase):
        for x in range(len(phrase)):
            self.reversed_phrase+=str(phrase[len(phrase)-x-1])         # Starting from last character of phrase_user_input save it to reversed_phrase and decrease the index
    def encrypt(self):
        self.reverse(self.Encrypt_phrase)
        for x in range (len(self.reversed_phrase)):
            for y in range(len(self.characters)):                                              # This loops runs until next letter from reversed_phrase found in Alphabet
                if self.reversed_phrase[x] == self.characters[y]:                                   # if the letter in location Alphabet[y]
                    self.location_in_characters = y+self.Distance                                   # Add distance to set new location in alphabet
                    self.location_in_characters %= len(self.characters)                               # current distance + user distance might be bigger than len(Alphabet) so Calculate mod 26
                    self.Encrypted_phrase += str(self.characters[self.location_in_characters])             # Save new letter after pushing distance.
                    break                                                               # break the loop letter has been found
        return self.Encrypted_phrase
    def decrypt(self):
        self.reverse(self.Decrypt_phrase)
        for x in range (len(self.reversed_phrase)):
            for y in range(len(self.characters)):                                              # This loops runs until next letter from reversed_phrase found in Alphabet
                if self.reversed_phrase[x]==self.characters[y]:                                     # if the letter in location Alphabet[y]
                    self.location_in_characters = y-self.Distance+len(self.characters)                     # Extract distance from current location to set new location in alphabet (to avoid negative add len(Alphabet))
                    self.location_in_characters %= len(self.characters)                               # current distance - user distance + len(Alphabet) might be bigger than len(Alphabet) so Calculate mod 26
                    self.Decrypted_phrase += str(self.characters[self.location_in_characters])             # Save new letter after pushing distance.
                    break                                                               # break the loop letter has been found
        return self.Decrypted_phrase
