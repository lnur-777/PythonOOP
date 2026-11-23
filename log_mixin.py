class LogMixin:
    def print_log(self):
        print(f"[LOG] Transaction recorded: {self._title}")
