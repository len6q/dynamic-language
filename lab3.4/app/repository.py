import os
from app import app

class Repository():    
    def __init__(self):
        self.files_dict = {}

    def save(self, form):           
        file = form.file.data
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path) 
        self.files_dict[file.filename] = self.get_frequent_word(file_path)        
        
    def get_frequent_word(self, file_path):
        words = self.get_words(file_path)
        words_dict = self.get_words_count(words)        
        if words_dict:
            value = max(words_dict, key=words_dict.get)
        else:
            value = None            

        return value   

    def get_words(self, file_path):
        words = []
        with open(file_path, encoding='utf8') as file:
            for line in file:
                line = line.lower().replace('\n', '')                
                words.append(line)
        return words

    def get_words_count(self, words):
        words_dict = {}
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        return words_dict