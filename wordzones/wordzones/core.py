from typing import List


class Select(object):
    pass


class Paint(object):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def show_canvas(
        self,
        zones: List[List[str]] = [
            ["assignment", "points", "test", "expect", "work"],
            ["molecules", "receptor", "binding", "protein"],
        ],
    ):
        pass
