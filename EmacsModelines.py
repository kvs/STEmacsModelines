# Emacs-like modeline parser
#
# Parses any '-*- ... -*-'-style modeline within the first 5 lines of a
# view, and sets a few variables.
#
# Currently supports setting mode (syntax), tab-width and tab-mode.

import sublime
import sublime_plugin
import re
import os

MODELINE_RE = r'.*-\*-\s*(.+?)\s*-\*-.*'
MODELINE_MAX_LINES = 5


class EmacsModelinesListener(sublime_plugin.EventListener):
    def __init__(self):
        self._modes = {}

        for root, dirs, files in os.walk(sublime.packages_path()):
            for f in files:
                if f.endswith('.tmLanguage'):
                    f = os.path.join(root, f)
                    name = os.path.splitext(os.path.basename(f))[0].lower()
                    syntax_file = re.match(r'^.+/(Packages/.+)$', f).group(1)
                    self._modes[name] = syntax_file

    def on_load(self, view):
        self.parse_modelines(view)

    def on_activated(self, view):
        self.parse_modelines(view)

    def on_post_save(self, view):
        self.parse_modelines(view)

    def parse_modelines(self, view):
        # Grab lines from beginning of view
        regionEnd = view.text_point(MODELINE_MAX_LINES, 0)
        region = sublime.Region(0, regionEnd)
        lines = view.lines(region)

        # Look for modeline regexp
        for line in lines:
            m = re.match(MODELINE_RE, view.substr(line))
            if m:
                modeline = m.group(1)

                # Split into options
                for opt in modeline.split(';'):
                    opts = re.match('\s*(.+):\s*(.+)\s*', opt)

                    if opts:
                        key, value = opts.group(1), opts.group(2)

                        if key == "mode":
                            view.settings().set('syntax', self._modes[value])
                        elif key == "indent-tabs-mode":
                            if value == "nil" or value.strip == "0":
                                view.settings().set('translate_tabs_to_spaces', True)
                            else:
                                view.settings().set('translate_tabs_to_spaces', False)
                        elif key == "tab-width":
                            view.settings().set('tab_size', int(value))
                        elif key == "sublime":
                            # FIXME: missing
                            pass
                    else:
                        # Not a 'key: value'-pair - assume it's a syntax-name
                        if opt.strip() in self._modes:
                            view.settings().set('syntax', self._modes[opt.strip()])

                # We found a mode-line, so stop processing
                break
