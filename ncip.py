#!/usr/bin/python

import sys
sys.path.append('./')
import ncipcfg
import getopt

#testing only
x=ncipcfg.NcipRequest()
#print x.PatronBarcode

def usage():
    print "this is a usage statement"

#accept arguments
def main(argv):                                       
    try:                                
        #opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
        opts, args = getopt.getopt(argv, "hu:i:p:r:n:x:", ["help", "ResponderURL=", "ItemBarcode=", "PatronBarcode=", "RequestType=", "NCIPVersion=", "XMLNS="])
    except getopt.GetoptError:           
        usage()                          
        sys.exit(2)                     
        if __name__ == "__main__":
            #print "name=main"
            main(sys.argv[1:])
            for opt, arg in opts:
                if opt in ("-h", "--help"):      
                    usage()                     
                    sys.exit()
                elif opt == '-d':                
                    global _debug               
                    _debug = 1
                else:
                    usage()

