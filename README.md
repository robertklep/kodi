# Kodi scripts

This is a small selection of scripts for [Kodi](https://kodi.tv) that are useful to me, and perhaps to you as well.

## Installation/Use

These aren't proper add-ons, so the process of using them is a bit elaborate.

The scripts are meant to be triggered by a key, which means creating your own custom `keymap.xml` (if you haven't got one already). [Here](http://kodi.wiki/view/Keymap) is more info on that process.

My general setup:

``` 
KODIROOT
    |
    +-- userdata/
    |      |
    |      +-- keymaps/     <- where keymap is stored
    |      |
    |      +-- scripts/     <- where scripts are stored
    |      |
    |      ...
    |
    ...
```

For example, I use the following keybinding for the `remove-video.py` script:

``` xml
<keymap>
  ...
  <videolibrary>
    <keyboard>
      ...
      <d>xbmc.RunScript(special://userdata/scripts/remove-video.py)</d>
    </keyboard>
  </videolibrary>
</keymap>
```

This assigns the script to the `d` key when the video library is active. You can obviously use your own preferred key for any of the scripts.

## The scripts

### remove-video.py

I find the operation of removing a TV show episode extremely tedious:

* `c` to open the context menu
* `Manage…`
* `Remove from library`
* _"Are you sure you want to remove it from the library?"_
* _"Are you sure you want to remove the file itself?"_

This script will ask you a single question: _"Are you sure?"_. If you don't cancel that question (using `Esc`), it will remove the episode from both the library and the filesystem.

### switch-directory.py

It regularly happens that Kodi shows an empty library folder even though there are files in the underlying filesystem folder (usually because the filenames aren't properly formatted, or the season/episode values don't match up with the scraper). This script will open the underlying filesystem folder so do you don't have to navigate there yourself.
