#################################################################################
# NetCaPy v1.0                                                                  #
# A Python based Network Packet capturing tool built on top of ScaPy and PyQt4  #
#                                                                               #
#################################################################################
#                                                                               #
# Module: Custom                                                                #
# Description:                                                                  #
#                                                                               #
#################################################################################

from Filter import Filter

'''
Description:

'''
class Custom(Filter):
    def __init__(self):
        Filter.__init__(self)
        print "Custom Filter Base Class"