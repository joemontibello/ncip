#!/usr/bin/python

import sys
sys.path.append('./')
import ncipcfg
import argparse
#testing only
x=ncipcfg.NcipRequest()
#print x.PatronBarcode

def usage():
    print "this is a usage statement"


parser = argparse.ArgumentParser(description='Joe\'s Python NCIP Requester')
parser.add_argument('-u', action='store', dest='ResponderURL', default='http://129.170.20.40/iii/nciprelais/Restful',
                    help='URL of the target NCIP responder')
parser.add_argument('-i', action='store', dest='ItemBarcode',
                    help='Barcode of an item for lookup or circulation')
parser.add_argument('-p', action='store', dest='PatronBarcode',
                    help='Barcode of patron for lookup or circulation')
parser.add_argument('-r', action='store', dest='RequestType', required=True, 
                    help='Type of NCIP request. Accepted values will be lookupitem, lookuppatron, checkoutitem, checkinitem, acceptitem')
parser.add_argument('-n', action='store', dest='NCIPVersion', default='http://www.niso.org/schemas/ncip/v2_0/ncip_v2_0.xsd',
                    help='Version of NCIP protocol for request. Currently only version 2.0 is supported.')
parser.add_argument('-x', action='store', dest='XMLNS', default='http://www.niso.org/2008/ncip',
                    help='XML Namespace')
parser.add_argument('--version', action='version', version='%(prog)s 0.1')
results = parser.parse_args()
print results.ResponderURL


#accept arguments
# def main(argv):                                       
#     try:                                
#         #opts, args = getopt.getopt(argv, "hg:d", ["help", "grammar="])
#         opts, args = getopt.getopt(argv, "hu:i:p:r:n:x:", ["help", "ResponderURL=", "ItemBarcode=", "PatronBarcode=", "RequestType=", "NCIPVersion=", "XMLNS="])
#         #usage()
#         #print "inside try block"
#     except getopt.GetoptError:           
#         usage()                          
#         sys.exit(2)
        
# if __name__ == "__main__":
#     print "name=main"
#     main(sys.argv[1:])
#     #print opt
#     for opt, arg in opts:
#         if opt in ("-h", "--help"):      
#             usage()                     
#             sys.exit()
#         elif opt == '-d':                
#             global _debug               
#             _debug = 1
#         else:
#             usage()

#main(sys.argv)
