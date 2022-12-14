#!/usr/bin/env python3
from typing \
    import Final

from var \
    import configuration


var_extension_name = '.conf'

class variables:
    def __init__( self ):
        global var_extension_name

        self.extension_name: Final = var_extension_name
        self.configuration = configuration()


# generates a generic template that has to be filled out by a user.
# gives a nice starting point.
def generic( name ):
    if isinstance( name, str ):
        return _generic_make( name )


def _generic_make( name ):
    defaults = variables()
    filename = _combine_filename( name, defaults.extension_name )
    returnConfig = \
        {          \
            "file" : filename, \
            "interface": None, \
            "peers":[]         \
        }
    
    returnConfig[ "interface" ] = _template_interface( defaults )
    returnConfig[ "peers" ] = _template_peers( defaults, returnConfig[ "peers" ] )

    return returnConfig


def _template_interface( vars ):

    return None


def _template_peers( vars, peers ):
    returnPeer = []

    return returnPeer
    
    

    

def _combine_filename( filename, ext ): 
    return str( filename + ext )


if __name__ == '__main__':
    print( generic( 'test' ) )