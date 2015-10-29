#!/usr/bin/env python

import xbmc, xbmcgui, xbmcvfs

# Get the necessary properties
fullpath   = xbmc.getInfoLabel('ListItem.FilenameAndPath')
dbid       = xbmc.getInfoLabel('ListItem.DBID')
filename   = xbmc.getInfoLabel('ListItem.Filename')

# Check if this is an actual file and the user really wants to remove it.
if not filename or not xbmcgui.Dialog().ok('Are you sure?', 'Do you want to delete:', filename):
    exit(0)

# Delete the file from the filesystem.
xbmcvfs.delete(fullpath)

# Also delete it from the library.
rpc = '{ "jsonrpc": "2.0", "method": "VideoLibrary.RemoveEpisode", "params" : { "episodeid": %s }, "id" : 1 }' % dbid
xbmc.executeJSONRPC(rpc)