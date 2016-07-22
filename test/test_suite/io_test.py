##########################################################################################################
#                    DECLARATIONS
##########################################################################################################

##########################################################################################################
#                    IMPORTS and CnC VARIABLES
import unittest;
##########################################################################################################

##########################################################################################################
#                    MAIN
class io_test_(unittest.TestCase): 
    def __init__(self, test_subject):
        """
        Initialize common internal variables
        """
        self.test_subject = test_subject;
        self.test_outcome = [];
        
    def read_test(self):
        """
        Test for read function from text file and makes sure result input is valid
        """
        # Input type check (pass = string)
        self.assertIsInstance(io_test_.test_subject, str)
        with assertRaises()