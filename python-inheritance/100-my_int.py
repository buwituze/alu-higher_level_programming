#!/usr/bin/python3
"""Defininga class MyInt that inherits from int."""


class MyInt(int):
    """Inverting int operators == and !=."""

    def __eq__(self, value):
        """Override == using != """
        return self.real != value

    def __ne__(self, value):
        """Override != using  == """
        return self.real == value
