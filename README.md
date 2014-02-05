# Emacs-like Sublime Modeline

Parse Emacs-like modelines, and set buffer-local settings for Sublime Text 2 and 3.


## Installing

I highly recommend installing via [Package Control](http://wbond.net/sublime_packages/package_control).


## Usage

Somewhere within the first five lines of a file, add a line matching the following:

	-*- key: value; key2: value2 -*-

or

	-*- syntax -*-

Besides the built in `coding`, `indent-tabs-mode`, `mode` and `tab-width`, any Sublime Text view
setting can be set. You can find all of the possible settings in Prefences / Settings - Default.
Prefix any of the sublime settings with `st-`, `sublime-`, `sublime-text-` or `sublimetext-`. For
example, specifying `st-trim_automatic_white_space: false` disables automatic whitespace trimming.

The values for `mode` are the root filename of the .tmLanaguge file. Most of
the time these are obvious and match the syntax name but not all the time. For
example the 'Graphviz (DOT)' syntax is simply 'dot'. To find out the correct
value you can run this command in the console (ctrl+\`) when the syntax you want is in
use:

	view.settings().get('syntax')
	# u'Packages/Graphviz/DOT.tmLanguage' -> 'DOT' is the mode value needed.

If you want to use the same mode line settings with an Emacs user you might need
to set up mappings from the Emacs names to the Sublime syntax names. To do this
look at the `mode_mappings` key in the settings file (which you can edit via the
menu Preferences, Package Settings, Emacs Modelines). As an example this package
ships with a mapping from "Bash" (emacs) to "Shell-Unix-Generic" (sublime).

If you want to preserve the default `mode_mappings`, you can also add your own
to `user_mode_mappings`.


## Examples

Sets the syntax to "lua", and adds rulers at location 39 and 80:

    -- -*- mode: lua; sublime-rulers: [39, 80]; -*-



## Alternatives

* [Vim-style modelines](https://github.com/SublimeText/Modelines)
* [More Emacs-style hacks](http://software.clapper.org/ST2EmacsMiscellanea/)


## Meta

Created by Kenneth Vestergaard.

Patches contributed by [Ash Berlin](https://github.com/ashb) and [Roy Ivy III](https://github.com/rivy).

Released under the MIT License: http://www.opensource.org/licenses/mit-license.php
