class ARRAY_TOOLS:
    def __init__(self):
        """
        Contains functions for general array manipulation
        """
    
    def Dimension(self, dim_object=None, counter=1):
        """
        Function for array dimension counting (CUSTOMIZE FOR OTHER NON SQUARE MATRIX)
        
        --dim_object: object to count dimension
        --counter: incremental counter to count dimensions (normally use default value)
        """
        # Check object is specified
        if dim_object is None:
            print("No object specified to extract dimensions");
            self._count = 0;
    
        self._count = counter;
        try:
            if type(dim_object[0]) is list:
                self._count = self._count + 1;
                self._count = ARRAY_TOOLS().Dimension(dim_object[0], self._count);
            else:
                pass;
        except IndexError:
            pass;
            
        return self._count;
    
    def Constuct(self, dim_counter, const_object=[]):
        """
        Function to construct array template. (UPDATE FOR NON SQUARE ARRAYS)
        INCOMPLETE
        --const_object: object iterator
        --dim_counter: dimension counter for object iterator
        """
        pass;
        
        
    def Decompose(self, decom_object=None):
        """
        Decomposes objects into arrays. If object is already an array, 
        each element of the array is converted into an array, making
        up the elements of the original array.
        
        --decom_object: object to decompose
        """
        # Check if object is specified
        if decom_object is None:
            print('No object specified for decomposition');
        
        # Decompose according to object type
        ####################################
        # Array #
        if type(decom_object) is list:
            self._internal = [];
            for self._i in range(0, len(decom_object)):
                self._internal = self._internal + [[decom_object[self._i]]];
                
        # String #
        elif type(decom_object) is str:
            self._internal = [];
            self._data = ''; # Data place holder
              
            for self._i in range(0, len(decom_object)):
                if self._i < (len(decom_object) - 1) : # End line check
                    if decom_object[self._i] != ' ':
                        self._data = self._data + decom_object[self._i];     
                    else:
                        self._internal = self._internal + [self._data];
                        self._data = ''; # Resets data placeholder
                else:
                    if decom_object[self._i] != ' ':
                        self._data = self._data + decom_object[self._i];
                        self._internal = self._internal + [self._data];
            for self._i in range(0, len(self._internal)): # Space cleanup
                if self._internal[self._i] == '':
                    del(self._internal[self._i]);
            
        return(self._internal);