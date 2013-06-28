"""
"""

#-----------------------------------------------------------------------------
# Copyright (c) 2013, the IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Stdlib imports
import string
import json
import IPython.core.display

#-----------------------------------------------------------------------------
# Classes and functions
#-----------------------------------------------------------------------------

class Plot():
    '''
    '''
    
    def create_plot_placeholder( self, name, **kargs ):
        src = """
        <div id="%(n)s" style="width:600px;height:300px;"/>   
        """%{'n':name}
        IPython.core.display.display_html(IPython.core.display.HTML(data=src))
        #print (src)
    
    def plot( self, data, options, name = None):
        """
           data = [(x1,y1,options1),(x2,y2,options2),...]
        """
        if name is None:
            name = str(self.nextName)
            self.nextName += 1
            self.create_plot_placeholder(name)
        src = ''
        encoder = json.JSONEncoder()

        src += 'var plot%(n)s = $.plot($("#%(n)s"), ['%{'n':name}
        
        for sernum,ser in enumerate(data):
            src += "{data :  %s , %s },\n"%(encoder.encode(zip(ser[0],ser[1])), encoder.encode(ser[2])[1:-1])

        src += '], %s);'%encoder.encode(options)

        IPython.core.display.display_javascript(IPython.core.display.Javascript(data=src,
                                                                                lib=["http://cdnjs.cloudflare.com/ajax/libs/flot/0.7/jquery.flot.min.js","http://cdnjs.cloudflare.com/ajax/libs/flot/0.7/jquery.flot.navigate.min.js","http://cdnjs.cloudflare.com/ajax/libs/flot/0.7/jquery.flot.selection.min.js"]))

        #print (src)        
        
                       

