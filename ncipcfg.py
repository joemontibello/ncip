#!/usr/bin/python



class NcipRequest:
    """An NCIP request in object form"""
    ResponderURL = "http://129.170.20.40/iii/nciprelais/Restful" # -u
    ItemBarcode= "33312001847777" # -i
    PatronBarcode="23311001905938" # -p
    RequestType="LookupUser" # -r
    NCIPVersion="http://www.niso.org/schemas/ncip/v2_0/ncip_v2_0.xsd" # -n
    XMLNS="http://www.niso.org/2008/ncip" # -x
    
