#!/usr/bin/env python

import xbmc

# Get the currently selected item's path.
path = xbmc.getInfoLabel('ListItem.Path')

# If it's a library item, select it and get its filesystem path
if 'videodb://' in path:
    xbmc.executebuiltin('XBMC.Action(Select)')
    xbmc.sleep(500)
    path = xbmc.getInfoLabel('ListItem.Path')

# Open it.
xbmc.executebuiltin('XBMC.ActivateWindow(Video, %s)' % path)
