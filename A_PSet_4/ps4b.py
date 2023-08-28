import random

class Message(object):
    def __init__(self, input_text):
        '''
        Initializes a Message object

        input_text (string): the message's text

        a Message object has one attribute:
            the message text
        '''
        self.message_text = input_text # starts message_text attribute w/ input_text argument

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''Message('{self.get_text()}')'''

    def get_text(self):
        '''
        Used to access the message text outside of the class

        Returns: (string) the message text
        '''
        return self.message_text # returns message_text attribute

    def shift_char(self, char, shift):
        '''
        Used to shift a character as described in the pset handout

        char (string): the single character to shift.
                    ASCII value in the range: 32<=ord(char)<=126
        shift (int): the amount to shift char ASCII value up by

        Returns: (string) the shifted character with ASCII value in the range [32, 126]
        '''
        shifted_char = chr((ord(char) - 32 + shift) % 95 + 32) # shifts char by a given #
        return shifted_char # returns the shifted character ('shifted_char')

    def apply_pad(self, pad):
        '''
        Used to calculate the ciphertext produced by applying a one time pad to the message text.
        For each character in the text at index i shift that character by
            the amount specified by pad[i]

        pad (list of ints): a list of integers used to encrypt the message text
                        len(pad) == len(the message text)

        Returns: (string) The ciphertext produced using the one time pad
        '''
        ciphertext = '' # starts an '' to save the 'ciphertext'
        for i in range(len(self.message_text)): # iterate chars in 'message_text'
            shifted_char = self.shift_char(self.message_text[i], pad[i]) # shift each chars by # in 'pad'
            ciphertext += shifted_char # add the shifted character to the ciphertext string
        return ciphertext # returns ciphertext strg

class PlaintextMessage(Message):
    def __init__(self, input_text, pad=None):
        '''
        Initializes a PlaintextMessage object.

        input_text (string): the message's text
        pad (list of ints OR None): the pad to encrypt the input_text or None if left empty
            if pad!=None then len(pad) == len(self.input_text)
            save as a COPY

        A PlaintextMessage object inherits from Message. It has three attributes:
            the message text
            the pad (list of integers, determined by pad
                or generated randomly using self.generate_pad() if pad==None)
            the ciphertext (string, input_text encrypted using the pad)
        '''
        super().__init__(input_text) # parent class = Message
        if pad is None:
            self.pad = self.generate_pad() # generates a new 'pad' by'self.generate_pad()' if pad = None
        else:
            self.pad = pad.copy() # save the pad as a copy if pad is not None
        self.ciphertext = self.apply_pad(self.pad) # encrypts 'input_text' using the pad in 'self.apply_pad()'


    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''PlaintextMessage('{self.get_text()}', {self.get_pad()})'''

    def generate_pad(self):
        '''
        Generates a one time pad which can be used to encrypt the message text.

        The pad should be generated by making a new list and for each character
            in the message chosing a random number in the range [0, 110) and
            adding that number to the list.

        Returns: (list of integers) the new one time pad
                    len(pad) == len(message text)
        '''
        return [random.randint(0, 109) for _ in range(len(self.message_text))]  #generates a new 'pad' w/ random #s in [0, 110) for each char in the 'message_text'

    def get_pad(self):
        '''
        Used to safely access your one time pad outside of the class

        Returns: (list of integers) a COPY of your pad
        '''
        return self.pad.copy() # returns a copy of pad


    def get_ciphertext(self):
        '''
        Used to access the ciphertext produced by applying pad to the message text

        Returns: (string) the ciphertext
        '''
        return self.ciphertext # returns ciphertext
    
    def change_pad(self, new_pad):
        '''
        Changes the pad used to encrypt the message text and updates any other
        attributes that are determined by the pad.

        new_pad (list of ints): the new one time pad that should be associated with this message.
            len(new_pad) == len(the message text)
            save as a COPY

        Returns: nothing
        '''
        self.pad = new_pad.copy() # save a copy of the new pad
        self.ciphertext = self.apply_pad(self.pad) # encrypts the 'message_text' using new pad

class EncryptedMessage(Message):
    def __init__(self, input_text):
        '''
        Initializes an EncryptedMessage object

        input_text (string): the ciphertext of the message

        an EncryptedMessage object inherits from Message. It has one attribute:
            the message text (ciphertext)
        '''
        super().__init__(input_text) # parent class =  Message

    def __repr__(self):
        '''
        Returns a human readable representation of the object
        DO NOT CHANGE

        Returns: (string) A representation of the object
        '''
        return f'''EncryptedMessage('{self.get_text()}')'''

    def decrypt_message(self, pad):
        '''
        Decrypts the message text that was encrypted with pad as described in the writeup

        pad (list of ints): the new one time pad used to encrypt the message.
            len(pad) == len(the message text)

        Returns: (PlaintextMessage) the decrypted message (containing the pad)
        '''
        plaintext = '' # empty string to save the decrypted message
        for i in range(len(self.message_text)): # iterates chars of message_text
            shifted_char = self.shift_char(self.message_text[i], -pad[i]) # shifts chars by # in pad
            plaintext += shifted_char # appends decrypted char to 'plaintext' 
        return PlaintextMessage(plaintext, pad) # returns a new PlaintextMessage class
