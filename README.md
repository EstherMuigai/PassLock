# PassLock
This project incorporates lessons learnt in  python basics. Lessons include data types,loops, functions, python as an Object Oriented programming language and Test Driven Development The version is pythonon 3.6.
The project was uploaded on 08/04/2019.


## BDD

| Input Example                                   | Output Example  				                            |
|:----------------------------------------------: | --------------------------------------------------: |		                   
| GIVEN user selects sign up option               |  WHEN they fill in the details THEN details are saved in a list                   |
| 			                                          | 			                                              | 						 		     
| GIVEN user selects an autogenerated password	  |  THEN they are prompted for the desired length,password is then printed|
| 			                                          | 			              						 		                | 
| GIVEN user selects own password                 | THEN they get to type in a custom password          |
| 			                                          | 			                                              | 						 		 
| GIVEN user wants to sign in                     | WHEN they input correct details they can view locker| 
| 			                                          | 			                                              | 						 		 
| GIVEN user wants to add account credentials     | WHEN they fill in details, the account is added     |
| 			                                          | 			                                              | 						 		 
| GIVEN user inputs blank spaces		              | THEN they are prompted			                        | 
| 			                                          | 			                                              | 


## Running unit tests
The project has four unit tests in two files:
1. run python3.6 user_test.py
2. run python3.6 credential_test.py
3. run python3 -m unittest -v user_test for a log of each test
They ran successfully.

## Find license here
https://github.com/EstherMuigai/PassLock/new/master
