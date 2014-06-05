import sublime, sublime_plugin
import re

class CssUnminifierCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        selections = self.view.sel()

        for selection in selections:
            self.view.replace(
                edit,
                selection,
                self.unminify(self.view.substr(selection))
            )

    def unminify(self, code):
        tab_len = 4
        tab_char = ' '

        code = code.split('\t')
        code = (tab_char*tab_len).join(code)

        code = re.sub(r'\s*{\s*', ' {\n    ', code)
        code = re.sub(r';\s*', ';\n    ', code)
        code = re.sub(r',\s*', ', ', code)
        code = re.sub(r'[ ]*\}\s*', '}\n', code)
        code = re.sub(r'\}\s*(.+)', r'}\n\1', code)
        code = re.sub(r'\n    ([^:]+):\s*', r'\n    \1: ', code)
        code = re.sub(r'([A-z0-9\)])}', r'\1;\n}', code);

        return code
