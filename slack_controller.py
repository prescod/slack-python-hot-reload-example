from pathlib import Path


class SlackController:
    def __init__(self, filename, app):
        self.filename = Path(filename)
        self.context = {"app": app}
        assert self.filename.exists()

    def __getattr__(self, name):
        with open(self.filename) as f:
            globs = {}
            exec(f.read(), globs)
            func = globs[name]
            return lambda kwargs: func(self.context, **kwargs)
