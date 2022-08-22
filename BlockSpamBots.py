from pathlib import Path
import os.path
import csv


from matplotlib.pyplot import text


class BlockSpamBots:

    def __init__ (self, name, email, text):
        self.name = name.lower()
        self.email = email.lower()
        self.text = text.lower()
        
    # this is only usefull if we are doing something with it else we coud just call self.name (run_check.name)
    def get_name(self):
        return self.name.title()
    
    # this is only usefull if we are doing something with it else we coud just call self.email (run_check.email)
    def get_email(self):
        return self.email

    def get_text(self):
        ### Initiate lists with checker values for the loops to controll ###
        ascii_chars = "abcdefghijklmnopqrstuvwxyåäö1234567890 @!&()?+"        
        bad_word = ["sex", "nude", "href", "xxx", "porn"]
        
        ### Loop and message list for chars to check chars return True for chars we don't understand or forbidden chars
        bad_message = list(self.text)
        found_chars = []
        for ele in bad_message:
            if ele not in ascii_chars:
                found_chars.append(ele)        

        ### Loop and message list for words and return the bad word to display for the user
        bad_message = list(self.text.split(" "))
        found_words = []
        for words in bad_word:
            if words in bad_message:
                found_words.append(words)
        # if all is good return True for no error found in the checkers or return word found in words
        if found_chars or found_words:
            BlockSpamBots.write_spamfile(self)
            return found_chars + found_words
        else:
            return True
    # This will save spam and a posible way to make it more efective 
    def write_spamfile(self):
        rows = [self.name, self.email, self.text]
        spam_file = Path("/home/mikael/Development/Python/BlockSpamBots/spamfile/spamtext.csv")
        if os.stat(spam_file).st_size == 0  and spam_file.is_file():
            
            with open(spam_file, 'w') as csvfile:
                fields = ['Name', 'E-mail', 'message']
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(fields) 
                csvwriter.writerow(rows)
                csvfile.close()
                 
        else:
            with open(spam_file, 'a') as csvfile: 
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(rows)
                csvfile.close()



run_check = BlockSpamBots("Micke bot svensson", "micke@micke.se", "Hello Whats up in the morning se =% % % %") #tester case
print(f"{run_check.get_name()} {run_check.get_text()}")