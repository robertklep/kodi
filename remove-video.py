#!/usr/bin/env python

import xbmc, xbmcgui, xbmcvfs, glob, os.path

def log(msg):
    xbmc.log(msg = msg, level = xbmc.LOGERROR)

# Get the necessary properties
fullpath = xbmc.getInfoLabel('ListItem.FilenameAndPath')
dbid     = xbmc.getInfoLabel('ListItem.DBID')
filename = xbmc.getInfoLabel('ListItem.Filename')

# Check if this is an actual file and the user really wants to remove it.
if not filename or not xbmcgui.Dialog().ok('Are you sure?', 'Do you want to delete:', filename):
    exit(0)

# Delete the file from the filesystem.
xbmcvfs.delete(fullpath)

# Remove any related files (with the same prefix)
directory = os.path.dirname(fullpath)
root, ext = os.path.splitext(fullpath)
dirs, files = xbmcvfs.listdir(directory)
for file in files:
    if file.startswith(os.path.basename(root)):
        filepath = os.path.join(directory, file)
        xbmcvfs.delete(filepath)

# Also delete it from the library.
rpc = '{ "jsonrpc": "2.0", "method": "VideoLibrary.RemoveEpisode", "params" : { "episodeid": %s }, "id" : 1 }' % dbid
xbmc.executeJSONRPC(rpc)
