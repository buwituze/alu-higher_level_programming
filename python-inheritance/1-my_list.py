#!/usr/bin/python3
"""MyList Class inheriting from list."""


class MyList(list):
    """Implement sorted printing."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
