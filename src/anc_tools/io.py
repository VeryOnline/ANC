class IO:
    """
    Class of input objects and their associated IO methods
    """
    def __init__(self, read_path=None, mode='txt', write_path=None):
        """
        Constructs input object from source object specified by path.
        All inputs and outputs of the object to file are specified by
        the input and output paths. Write path defaults to None but can
        be specified later through the Write function. If no write path
        is specified for the class, raise error during write operation.
        
        Default IO mode is text.
        Other IO mode is binary (must be specified, else default is used).
        """
        import anc_tools;
        
        # Variable declaration
        self._internal = [];
        self._write_path = write_path;
        self._read_path = read_path;
        self._mode = mode;
        
        # CASE Read path is OTHER DATA STRUCTURE
        if type(self._read_path) is not str:
            self._internal = self._read_path;
        # CASE read path is PATH TO FILE
        else: 
            ###########################################
            # File type handling (Add case as needed) #
            ###########################################
            # Text files - interpret contents as plain text#
            if self._mode == 'txt':
                try:
                    self._source = open(self._read_path, 'r'); # Open file as read only
                except IOError:
                    print('File could not be found or file is corrupt'); ## UPDATE TO WRITE TO FILE MORE DETAILS
                else:
                    for i in self._source: # Converts source file to internal array (1 line = 1 array entry)
                        self._internal = self._internal + [i.rstrip('\n')];             
                    self._source.close(); # Close file
            # All other file types - interpret as binary #
            else:
                try:
                    self._source = open(self._read_path, 'rb'); # Try to open file as binary
                    for i in self._source: # Converts source file to internal array (1 bit = 1 array entry)
                        self._internal = self._internal + [i];
                except IOError:
                    print('File format not recognized and could not be read as binary');
        # Store instance object data type and report type to console
        self._internaltype = type(self._internal);
         
    def Push(self):
        """
        Pushes class instance into object to be manipulated
        """
        return(self._internal);
    
    def Pull(self, source=None):
        """
        Update class instance.
        
        --source: source to update element
        """
        if source is None:
            print('No source specified for update.');
        else:
            self._internal = source;
        # Warns of object change
        if self.Type() is not self._internaltype:
            print('Object type has changed');
            self._internaltype = self.Type(); # Update instance object type
        
        return(self._internal);
    
    def Type(self):
        """
        Returns class instance object type
        """
        return(type(self._internal));
        
    def Write(self, write_path_internal=None, mode='txt'):
        """
        Method to write class instance object to file.
        """    
        if self._write_path is None:
            self._write_path = write_path_internal;
        if self._write_path is not None:
            if mode == 'txt':
                self._write_object = open(self._write_path, 'w');
                self._write_object.write(str(self._internal)); # Convert to str
                self._write_object.close();
            else:
                self.write_object = open(self._write_path, 'wb');
                self.write_object.write(self._internal);
                self.write_object.close();
                
        return();

class STR_CONV:
    def __init__(self):
        '''
        Defines conversion procedures to convert string data to other
        data structures
        '''
    
    def ToList(self):
        pass;
        
    def ToByte(self):
        pass;