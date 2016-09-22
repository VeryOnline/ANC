##########################################################################################################
#                    DECLARATIONS
##########################################################################################################

##########################################################################################################
#                    IMPORTS and CnC VARIABLES
import sys #remove this line, this is for window only, to import all lib on window
sys.path.append('C:\\Users\\Administrator\\Documents\\GitHub\\ANC\\dep')
sys.path.append('C:\\Users\\Administrator\\Documents\\GitHub\\ANC\\test')
sys.path.append('C:\\Users\\Administrator\\Documents\\GitHub\\ANC\\src')
import sounddevice as sd
from struct import * #packing and unpacking data
#import numpy #May not needed if read from raw Stream
##########################################################################################################

##########################################################################################################
#                    MAIN
#New child class of list just for some test math
class numlist(list):
    def __mul__(self,other):
        tmps=numlist()
        for i in self:
            tmps.append(i*other)
        return tmps
#add other method to this class later
#handy function
def fmtezstr(fmt,fmtlen):
    res=''
    if type(fmtlen) is int:
        for i in range(fmtlen):
            res+=fmt
        return res
    else:
        print('Invalid length')

#other
def main():
    fs=48000 #Sample rate = 48000Hz
    dura=10 #5 second duration
    nrs=sd.RawStream(samplerate=fs,dtype='int32',channels=2) #type can be float32, int24 kinda hard to work with
    nrs.start()
    rdata=nrs.read(fs*dura) #record from input for 5 second
    #here instead of using callback (which do continuous read/write prediocally), we use block read/write for 
    #research, add additional reason why or why not here
    #rdata[0] contain rawdata, rdata[1] is overflow flag, whether it overflowed or not, need clarification
    #read more about struct function, particularly pack and unpack.
    #This will take 5 second of recording, triple the volume and play it back, handle with float is much more smoothly.
    fmv=fmtezstr('i',fs*10) #2 channels, each second have fs=48000 samples, so fs*2*duration(=5)
    nlst=numlist(unpack(fmv,rdata[0][0:fs*10*4])) #each int32 is 4 bytes
    n=pack(fmv,*(nlst*3)) #triple the volume
    nrs.write(n+rdata[0][fs*10*4:])
    nrs.stop()

    
