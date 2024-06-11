import sublime
import sublime_plugin


class SplitSelectionIntoCharactersCommand(sublime_plugin.TextCommand):
    
    def run(self, edit):
        new_regions = []
        for region in self.view.sel():
            for i in range(region.begin(), region.end()):
                new_regions.append(sublime.Region(i,i+1))
        self.view.sel().clear()

        for region in new_regions:
            self.view.sel().add(region)