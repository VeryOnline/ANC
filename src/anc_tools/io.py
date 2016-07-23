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
        from anc_tools import ARRAY_TOOLS;
        import os;
        
        # Variable declaration
        self._init = [];
        self._write_path = write_path;
        
        # Extract file extension
        self._norm_path = os.path.normcase(read_path); # Normalizes path
        self._ftype = os.path.splitext(self._norm_path)[1]; # Takes 2nd element as file name
        
        # Cases to handle different file types (Add elif cases as needed)
        ######################################
        # Text files #
        if self._ftype == '.txt':
            try:
                self._source = open(self._norm_path, 'r'); # Open file as read only
            except IOError:
                print('File could not be found or file is corrupt'); ## UPDATE TO WRITE TO FILE MORE DETAILS
            
            for i in self._source: # Converts source file to internal array (1 line = 1 array entry)
                self._init = self._init + [i.rstrip('\n')];
            
            self._source.close(); # Close file 
        
        # File extension not recognized #
        else:
            try:
                self._source = open(self._norm_path, 'r'); # Try to open file as if file was plain text
            except IOError:
                print('File format not recognized and could not be read');
        
    def Push(self):
        """
        Pushes class instance into object to be manipulated
        """
        return(self._init);
    
    def Pull(self, source=None):
        """
        Update class instance.
        
        --source: source to update element
        """
        if source is None:
            print('No source specified for update.');
        else:
            self._init = source;
        
        return(self._init);
    
    def Write(self, write_object=None, write_path=None):
        """
        Method to write object to file.
        """
        
        print(self._init);
#         if write_object is None:
#             try:
#                 write_object = self._internal; # Default to instance object
#             except :

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
            