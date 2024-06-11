import sublime
import sublime_plugin


class SplitSelectionOnBoundariesCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):
        new_regions = []
        for region in self.view.sel():
            new_regions.append(sublime.Region(region.begin())) # region start
            new_regions.append(sublime.Region(region.end())) # region end
        self.view.sel().clear()

        for region in new_regions:
            self.view.sel().add(region)