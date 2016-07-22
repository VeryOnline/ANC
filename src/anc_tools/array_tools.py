class ARRAY_MAN:
    def __init__(self):
        """
        Contains functions for array manipulation
        """
    
    def Dimension(self, dim_object, counter=1):
        """
        Function for array dimension counting (CUSTOMIZE FOR OTHER NON SQUARE MATRIX)
        
        --dim_object: object to count dimension
        """
        self._count = counter;
        try:
            if type(dim_object[0]) is list:
                self._count = self._count + 1;
                self._count = ARRAY_MAN().Dimension(dim_object[0], self._count);
            else:
                pass;
        except IndexError:
            pass;
        
        return self._count;
    
    def Constuct(self, const_object=[], dim_counter):
        """
        Function to construct array template. (UPDATE FOR NON SQUARE ARRAYS)
        
        --const_object: object iterator
        --dim_counter: dimension counter for object iterator
        """
        
        
    def Decompose(self, decom_object=None) :
        """
        Decomposes array into array of elements for manipulation
        
        --decom_object: object to decompose
        """
        if decom_object is None: # Default to instance object
            print('No object specified for decomposition');
        
        self._dim = ARRAY_MAN().Dimension(decom_object); # Returns array dimensions
    
        self._internal = [[] for self._i in range(0, len(decom_object))];
        self._data = ''; # Data place holder
          
        for self._i in range(0, len(decom_object)):
            for self._j in range(0, len(decom_object[self._i])):
                if self._j < (len(decom_object[self._i]) - 1) : # End line check
                    if decom_object[self._i][self._j] != ' ':
                        self._data = self._data + decom_object[self._i][self._j];     
                    else:
                        self._internal[self._i] = self._internal[self._i] + [self._data];
                        self._data = ''; # Resets data placeholder
                else:
                    if decom_object[self._i][self._j] != ' ':
                        self._internal[self._i] = self._internal[self._i] + [decom_object[self._i][self._j]];
                    else:
                        self._internal[self._i] = self._internal[self._i] + ['x']; # Sets error marker
                     
        return self._internal;