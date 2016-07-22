class IO:
    """
    Class of input objects and their associated IO methods
    """
    def __init__(self, read_path, write_path=None):
        """
        Constructs input object from source object specified by path.
        All inputs and outputs of the object to file are specified by
        the input and output paths. Write path defaults to None but can
        be specified later through the Write function. If no write path
        is specified for the class, raise error during write operation.
        """
        from anc_tools import ARRAY_MAN;
        
        self._init = [];
        self._write_path = write_path;
        
        try:
            self._source = open(read_path, 'r'); # Open file as read only
        except IOError:
            print('File could not be found or file is corrupt'); ## UPDATE TO WRITE TO FILE MORE DETAILS
        
        for i in self._source: # Converts source file to internal array (1 line = 1 array entry)
            self._init = self._init + [i.rstrip('\n')];
        
        self._source.close(); # Close file 
    
        self._init = ARRAY_MAN().ArrayDecom(self._init); # Decomposes input into elements
        print(self._init);
        
    def Element(self, extract_object=None, key=None):
        """
        Extracts an element in decomposed input that matches key.
        
        --extract_object: object from which to extract element. Must be
        an array or array of arrays
        --key: specify key to element
        """
        if extract_object is None:
            extract_object = self._init;
        if key is None:
            print('No key specified');
             
        pass;
    
    def Write(self, write_object=None, write_path=None):
        """
        Method to write object. A different write path can be specified here.
        """
        pass;
#         if write_object is None:
#             try:
#                 write_object = self._internal; # Default to instance object
#             except :
#                 
        
        # Write path update and validation    
#         if write_path is not None:
#             self._write_path = write_path;
#         if self._write_path is None:
#             print("No write path for class instance");
#             
#         self._file = open(self._write_path, 'w'); # Opens file to write
#         self._data = '';
#         for self._i in range(0, len(write_object)): # Reassembles disparate object array
#             for self._j in range(0, len(write_object[self._i])):
#                 self._data = self._data + write_object[self._i][self._j] + ' ';
#             self._data = self._data.rstrip(' ') + '\n'; # Strips right most space
#             self._file.write(self._data);
#             self._data = '';
#             
#         self._file.close();
            