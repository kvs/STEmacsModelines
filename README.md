# Emacs-like Sublime Modeline

Parse Emacs-like modelines, and set buffer-local settings for Sublime Text 2 and 3.


## Installing

I highly recommend installing via [Package Control](http://wbond.net/sublime_packages/package_control).


## Usage

Somewhere within the first five lines of a file, add a line matching the following:

	-*- key: value; key2: value2 -*-

or

	-*- syntax -*-

Supported settings are '`mode`', '`tab-width`', '`indent-tabs-mode`', '`coding`', and '`sublime-*`.

Specifying '`sublime-`' (or '`st-`') allows changing Sublime Text preferences for that view. For
example, specifying '`st-trim_automatic_white_space: false`' disables automatic whitespace trimming.

The values for '`mode`' are the root filename of the .tmLanaguge file. Most of
the time these are obvious and match the syntax name but not all the time. For
example the 'Graphviz (DOT)' syntax is simply 'dot'. To find out the correct
value you can run this command in the console (ctrl+\`) when the syntax you want is in
use:

	view.settings().get('syntax')
	# u'Packages/Graphviz/DOT.tmLanguage' -> 'DOT' is the mode value needed.

If you want to use the same mode line settings with an emacs user you might need
to set up mappings from the emacs names to the sublime syntax names. To do this
look at the `mode_mappings` key in the settings file (which you can edit via the
menu Preferences, Package Settings, Emacs Modelines). As an example this package
ships with a mapping from "Bash" (emacs) to "Shell-Unix-Generic" (sublime).

## Alternatives

* [Vim-style modelines](https://github.com/SublimeText/Modelines)
* [More Emacs-style hacks](http://software.clapper.org/ST2EmacsMiscellanea/)


## Meta

Created by Kenneth Vestergaard.

Patches contributed by [Ash Berlin](https://github.com/ashb) and [Roy Ivy III](https://github.com/rivy).

Released under the MIT License: http://www.opensource.org/licenses/mit-license.php
