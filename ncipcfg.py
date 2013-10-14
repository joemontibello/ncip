#!/usr/bin/python

import sys
sys.path.append('/Users/dltg/ncip')


class NcipRequest:
    """An NCIP request in object form"""
    def __init__(self):
        ResponderURL = "http://129.170.20.40/iii/nciprelais/Restful"
        ItemBarcode= "33312001847777"
        PatronBarcode="23311001905938"
        RequestType="LookupUser"
        NCIPVersion="http://www.niso.org/schemas/ncip/v2_0/ncip_v2_0.xsd"
        XMLNS="http://www.niso.org/2008/ncip"

