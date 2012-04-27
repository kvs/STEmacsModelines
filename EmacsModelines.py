# Emacs-like modeline parser
#
# Parses any '-*- ... -*-'-style modeline within the first 5 lines of a
# view, and sets a few variables.
#
# Currently supports setting mode (syntax), tab-width and tab-mode.

# URLref: [Emacs - Specifying File Variables] http://www.gnu.org/software/emacs/manual/html_node/emacs/Specifying-File-Variables.html @@ http://www.webcitation.org/66xWWwjTt
# URLref: [Emacs - Coding Systems] http://www.gnu.org/software/emacs/manual/html_node/emacs/Coding-Systems.html @@ http://www.webcitation.org/66xX3pMc1
# URLref: [Emacs - Specifying a File's Coding System] http://www.gnu.org/software/emacs/manual/html_node/emacs/Specify-Coding.html @@ http://www.webcitation.org/66xZ1nDWp

import sublime
import sublime_plugin
import re
import os

MODELINE_RE = r'.*-\*-\s*(.+?)\s*-\*-.*'
MODELINE_MAX_LINES = 5


def to_json_type(v):
    # from "https://github.com/SublimeText/Modelines/blob/master/sublime_modelines.py"
    """"Convert string value to proper JSON type.
    """
    if v.lower() in ('true', 'false'):
        v = v[0].upper() + v[1:].lower()

    try:
        return eval(v, {}, {})
    except:
        raise ValueError("Could not convert to JSON type.")


class EmacsModelinesListener(sublime_plugin.EventListener):

    settings = None

    def __init__(self):
        self._modes = {}

        for root, dirs, files in os.walk(sublime.packages_path()):
            for f in files:
                if f.endswith('.tmLanguage'):
                    langfile = os.path.relpath(os.path.join(root, f), sublime.packages_path())
                    name = os.path.splitext(os.path.basename(langfile))[0].lower()
                    syntax_file = os.path.join('Packages', langfile)
                    # ST2 (as of build 2181) requires unix/MSYS style paths for the 'syntax' view setting
                    syntax_file = syntax_file.replace("\\", "/")
                    self._modes[name] = syntax_file

        # Load custom mappings from the settings file
        self.settings = sublime.load_settings(__name__ + ".sublime-settings")

        if self.settings.has("mode_mappings"):
            for modeline, syntax in self.settings.get("mode_mappings").items():
                self._modes[modeline] = self._modes[syntax.lower()]

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
                modeline = m.group(1).lower()

                # Split into options
                for opt in modeline.split(';'):
                    opts = re.match('\s*(st-|sublime-text-|sublime-|sublimetext-)?(.+):\s*(.+)\s*', opt)

                    if opts:
                        key, value = opts.group(2), opts.group(3)

                        if opts.group(1):
                            #print "settings().set(%s, %s)" % (key, value)
                            view.settings().set(key, to_json_type(value))
                        elif key == "coding":
                            value = re.match('(?:.+-)?(unix|dos|mac)', value).group(1)
                            if value == "dos":
                                value = "windows"
                            if value == "mac":
                                value = "CR"
                            view.set_line_endings(value)
                        elif key == "indent-tabs-mode":
                            if value == "nil" or value.strip == "0":
                                view.settings().set('translate_tabs_to_spaces', True)
                            else:
                                view.settings().set('translate_tabs_to_spaces', False)
                        elif key == "mode":
                            if value in self._modes:
                                view.settings().set('syntax', self._modes[value])
                        elif key == "tab-width":
                            view.settings().set('tab_size', int(value))
                    else:
                        # Not a 'key: value'-pair - assume it's a syntax-name
                        if opt.strip() in self._modes:
                            view.settings().set('syntax', self._modes[opt.strip()])

                # We found a mode-line, so stop processing
                break
