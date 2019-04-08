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
            User.user_list = []
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
    
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_verify_user(self):
        '''
        test_verify_user confirms whether the user is on the list with a username and password
        '''
    
        self.new_user.save_user()
        verified_user = User.verify_user("@bey","#####")

        self.assertTrue(verified_user)

    def test_create_credential(self):
        '''
        test_create_credential allows user to update a new credential
        '''
        facebook_credential = User.create_credential("facebook","Beyonce""Knowles","@beybey","beybey@hack","password")
        self.assertTrue(facebook_credential)

    def test_save_credential(self):
        '''
        test_save_credentials test case to test if the credential object is saved into
         the credential list
        '''
        facebook_credential = User.create_credential("facebook","Beyonce""Knowles","@beybey","beybey@hack","password")
        user_credential_list = []
        User.save_credential(facebook_credential,user_credential_list)
        self.assertEqual(len(user_credential_list),1)
    
    def test_display_credential(self):
        '''
        test_display_credential test case to test if all credentials will be returned
        '''
        facebook_credential = User.create_credential("facebook","Beyonce""Knowles","@beybey","beybey@hack","password")
        user_credential_list = []
        User.save_credential(facebook_credential,user_credential_list)
        self.assertEqual(User.display_credentials(),user_credential_list)


 
if __name__ == '__main__':
    unittest.main()

    
