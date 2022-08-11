from pathlib import Path
import os.path
import csv


class BlockSpamBots:

    def char_check(name, email, s):
        ### Initiate lists with checker values for the loops to controll ###
        name = name
        email = email
        alpa = "abcdefghijklmnopqrstuvwxyåäö1234567890 @!&()?+"
        alpa_upper = alpa[0:-18].upper()
       
        checker =  list(alpa) + list(alpa_upper)
        
        bad_word = ["sex", "nude", "href", "xxx", "porn"]
        #print(alpa_upper)
        ### Loop and message list for chars to check chars return True for chars we don't understand or forbidden chars
        bad_message = list(s)
        found_chars = []
        for ele in bad_message:
            if ele not in checker:
                found_chars.append(ele)
        

        ### Loop and message list for words and return the bad word to display for the user
        bad_message = list(s.split(" "))
        found_words = []
        for words in bad_word:
            if words in bad_message:
                found_words.append(words)
        # if all is good return True for no error found in the checkers or return word found in words
        if found_chars or found_words:
            BlockSpamBots.write_spamfile(name, email, s)
            return found_chars + found_words
        else:
            return True

    def write_spamfile(name, email, message):
        rows = [name, email, message]
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



print(BlockSpamBots.char_check("Micke", "micke@micke.se", "Hello Whats up in the morning sex %%%===")) #tester case