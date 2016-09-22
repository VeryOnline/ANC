##########################################################################################################
#                    DECLARATIONS
##########################################################################################################

##########################################################################################################
#                    IMPORTS and CnC VARIABLES
import sys
sys.path.append('C:\\Users\\Administrator\\Documents\\GitHub\\ANC\\dep')
sys.path.append('C:\\Users\\Administrator\\Documents\\GitHub\\ANC\\test')
sys.path.append('C:\\Users\\Administrator\\Documents\\GitHub\\ANC\\src')
import unittest;
from anc_tools import io;

##########################################################################################################

##########################################################################################################
#                    MAIN
class TEST_IO(unittest.TestCase): 
    def setUp(self):
        """
        Initialize test fixtures.
        """
        # Test text file (test_text.txt)
        self.test_subject_txt = open('test_text.txt', 'w');
        self.test_subject_txt.write('This is line 1 \n');
        self.test_subject_txt.write('This is line 2 \n');
        self.test_subject_txt.close();
        
        # Test binary file
        self.test_subject_bin = open('./test_bin', 'wb');
        self.test_subject_bin.write(bytearray([0x13, 0x00, 0x00, 0x00, 0x08, 0x00]));
        self.test_subject_bin.close();
        
        # Create IO object reading from file
        self.IO_txt = io.IO('./test_text.txt');
        self.IO_bin = io.IO('./test_bin', 'bin');
        
    def tearDown(self):
        """
        Deconstructs test fixtures.
        """
        del self.test_subject_txt;
        del self.test_subject_bin;
        del self.IO_txt;
        del self.IO_bin;
            
    def testRead_fromObj(self):
        '''
        Test for correctness in reading internal objects. String is not
        tested as this coincides with entering a path to the read function. 
        Non-path strings are to be entered enclosed in list ['asdf'] by convention.
        '''
        self.assertEqual(io.IO(['asdf']).Push(), ['asdf'], msg='Read list error' );
        self.assertEqual(io.IO(True).Push(), True, msg='Read bool error');
        self.assertEqual(io.IO(b'\x13\x00').Push(), b'\x13\x00', msg='Read byte error');
    
    def testRead_fromPath(self):
        """
        Test for correctness in reading files
        // Reading text files must result in a list with each element a string
        // Reading binary files must result in a list of hex
        """
        self.assertIs(type(self.IO_txt.Push()[0]), type('test'), msg='Text read error: text not stored as string');
        self.assertIs(type(self.IO_bin.Push()), list, msg='Binary read error: data not stored as list');
        self.assertIs(type(self.IO_bin.Push()[0]), bytes, msg='Binary read error: data list elements not bytes');
    
    def testPull(self):
        '''
        Test correctness of Pull function. Objects pulled must be stored correctly
        '''
        self.assertEqual(self.IO_txt.Pull(['asdf']), ['asdf'], msg='Incorrect pull: list');
        self.assertEqual(self.IO_txt.Pull(True), True, msg='Incorrect pull: bool');
        self.assertEqual(self.IO_txt.Pull(b'\x00\x13'), b'\x00\x13', msg = 'Incorrect pull: byte');
    
    def testWrite_nonBinary(self):
        '''
        Test text write mode. All data structures are converted to strings
        '''
        self.IO_txt.Pull([b'\x00\x01']);
        self.IO_txt.Write('./test_text.txt');
        self._test = io.IO('./test_text.txt');
        self.assertEqual(self._test.Push()[0], "[b'\\x00\\x01']", msg='Write function error: Text mode');

    def testWrite_Binary(self):
        '''
        Test binary write mode. All data structures are converted to binary
        '''
        self.IO_txt.Pull(b'\x00\x01');
        self.IO_txt.Write('./test_bin', 'binary');
        self._test = io.IO('./test_bin', 'binary');
        self.assertEqual(self._test.Push()[0], b'\x00\x01', msg='Write function error: Binary mode');

if __name__ == '__main__':
    unittest.main();
    
# suite = unittest.TestLoader().loadTestsFromTestCase(TEST_IO);
# unittest.TextTestRunner(verbosity=2).run(suite);