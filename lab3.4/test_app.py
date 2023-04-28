import unittest
from bs4 import BeautifulSoup
from app.repository import Repository
from app import app

NULL_FILE_PATH = 'lab3.4/test_txt_files/null.txt'
DIFFERENT_REG_FILE_PATH = 'lab3.4/test_txt_files/test1.txt'

class TestApp(unittest.TestCase):
    def setUp(self) -> None:
        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()
        self.repo = Repository()
    
    def tearDown(self) -> None:
        self.context.pop()

    def test_couting_in_empty_file(self):
        self.assertIsNone(self.repo.get_frequent_word(NULL_FILE_PATH))    

    def test_couting_with_different_registers(self):
        self.assertEqual(
            self.repo.get_frequent_word(DIFFERENT_REG_FILE_PATH),
            'тест')

    def test_correct_code_responces(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/result')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/null')
        self.assertNotEqual(response.status_code, 200)
        response = self.client.post('/result')
        self.assertNotEqual(response.status_code, 200)                       

    def test_get_result_page_in_first_time(self):
        response = self.client.get('/result')  
        soup = BeautifulSoup(response.get_data(as_text=True), "html.parser")
        data = soup.find('p')      
        self.assertTrue('Данных пока нет' == data.text)                  

if __name__ == '__main__':
    unittest.main()