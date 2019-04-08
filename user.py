from random import *
import string
from credential import Credential
class User:
    """
    Class that generates new instances of users.

    """

    def __init__(self,first_name,last_name,username,email,password):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

    credential_list = []

    @classmethod
    def create_credential(cls,detail1,detail2,detail3,detail4,detail5,detail6):
        '''
        be able to create a new credential/account with all details
        '''
        new_credential = Credential(detail1,detail2,detail3,detail4,detail5,detail6)

        return new_credential

    @classmethod
    def save_credential(cls,new_credential,credential_list):
        '''
        be able to save a new credential/account with all details to a list
        '''
        credential_list.append(new_credential)

        return credential_list

    @classmethod
    def display_credential(cls,credential_list):
        '''
        be able to display all credentials
        '''
        return credential_list

    @classmethod
    def del_credential(cls,credential_list):
        '''
        be able to delete a credential
        '''
        
        Contact.contact_list.remove(self)



