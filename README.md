# Emacs-like Sublime Modeline

Parse Emacs-like modelines, and set buffer-local settings.


## Installing

I highly recommend installing via [Package Control](http://wbond.net/sublime_packages/package_control).


## Usage

Somewhere within the first five lines of a file, add a line matching the following:

	-*- key: value; key2: value2 -*-

or

	-*- syntax -*-

Currently, only 'mode', 'tab-width' and 'indent-tabs-mode' are supported.


## Alternatives

* [Vim-style modelines](https://github.com/SublimeText/Modelines)
* [More Emacs-style hacks](http://software.clapper.org/ST2EmacsMiscellanea/)
