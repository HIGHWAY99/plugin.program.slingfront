

"""
    Plugin for Launching SlingFront
"""


import sys
import os
import fnmatch
import xbmc
import xbmcgui
import xbmcplugin

import time
import re
import urllib
import subprocess_hack
import xml.dom.minidom
import socket
import exceptions

import random
from traceback import print_exc

import shutil



from xbmcaddon import Addon
import xbmcaddon
addon=xbmcaddon.Addon()




class Main:
    
    slingfront = {}
    
    def __init__( self ):
        
        if ( xbmc.Player().isPlaying() ):
            xbmc.executebuiltin('PlayerControl(Play)')
        xbmc.sleep(400)            
        
        
        
        # store an handle pointer
        self._handle = int(sys.argv[ 1 ])

        self._path = sys.argv[ 0 ]
       

        #PLUGIN_DATA_PATH = xbmc.translatePath( os.path.join( "special://home", "addons", "plugin.program.slingfront") )
        PLUGIN_DATA_PATH = xbmc.translatePath( addon.getAddonInfo('path') ) ## << ## This will allow the plugin to work reguardless of what the addon folder is named.
        info = subprocess_hack.STARTUPINFO()
        info.dwFlags = 1
        info.wShowWindow = 0
        #ap = PLUGIN_DATA_PATH + "\\launch.bat"
        ap = os.path.join( PLUGIN_DATA_PATH, "launch.bat" )
        arguments = ""
        apppath = PLUGIN_DATA_PATH
        startproc = subprocess_hack.Popen(r'%s %s' % (ap, arguments), cwd=apppath, startupinfo=info)
   


 
        startproc.wait()
        xbmc.sleep(200)


        #ap = xbmc.translatePath("special://xbmc") + "\\xbmc.exe"
        ap = xbmc.translatePath( os.path.join( "special://xbmc", "XBMC.exe" ) )
        if (os.path.exists(ap)==False) or (os.path.isfile(ap)==False):
            #ap = xbmc.translatePath("special://xbmc") + "\\Kodi.exe"
            ap = xbmc.translatePath( os.path.join( "special://xbmc", "Kodi.exe" ) )
        arguments = ""
        apppath = xbmc.translatePath("special://xbmc")
        startproc = subprocess_hack.Popen(r'%s %s' % (ap, arguments), cwd=apppath, startupinfo=info)
 
        # startproc.wait()
        xbmc.sleep(200)
        xbmc.executebuiltin('PlayerControl(Play)') 
        xbmc.sleep(400)
        
        #




