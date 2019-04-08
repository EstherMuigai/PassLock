import unittest
from random import *
import string
from user import User
from credential import Credential

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Beyonce","Knowles","@bey","bknowles@carter.com","#####")

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            credential_list = []
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Beyonce")
        self.assertEqual(self.new_user.last_name,"Knowles")
        self.assertEqual(self.new_user.username,"@bey")
        self.assertEqual(self.new_user.email,"bknowles@carter.com")
        self.assertEqual(self.new_user.password,"#####")

    def test_create_credential(self):
        '''
        test_create_credential allows user to update a new credential
        '''
        facebook_credential = User.create_credential("facebook","Beyonce","Knowles","@beybey","beybey@hack","password")
        self.assertTrue(facebook_credential)

    def test_save_credential(self):
        '''
        test_save_credentials test case to test if the credential object is saved into
         the credential list
        '''
        facebook_credential = User.create_credential("facebook","Beyonce","Knowles","@beybey","beybey@hack","password")
        user_credential_list = []
        User.save_credential(facebook_credential,user_credential_list)
        self.assertEqual(len(user_credential_list),1)
    
    def test_display_credential(self):
        '''
        test_display_credential test case to test if all credentials will be returned
        '''
        facebook_credential = User.create_credential("facebook","Beyonce","Knowles","@beybey","beybey@hack","password")
        user_credential_list = []
        User.save_credential(facebook_credential,user_credential_list)
        self.assertEqual(User.display_credential(user_credential_list),user_credential_list)

    
if __name__ == '__main__':
    unittest.main()

    
