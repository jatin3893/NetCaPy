from Filter import Filter

#################################################################
class Custom(Filter):
    def __init__(self):
        Filter.__init__(self)
        print "Custom Filter Base Class"