#!/usr/bin/python3
"""test module for console.py"""
from io import StringIO
import unittest
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """TestConsloe class"""
    def _helper(self, cmd):
        with patch('sys.stdout', new=StringIO()) as f:
            result = HBNBCommand().onecmd(cmd)
        return result, f.getvalue()

    def test_help(self):
        """tests for help cmd"""
        _, output = self._helper("help quit")
        self.assertIn("quit", output.lower())

    def test_quit_output(self):
        """tests for quit cmd"""
        result, output = self._helper("quit")

        self.assertEqual(output, '')
        self.assertEqual(result, True)

    def test_EOF(self):
        """tests EOF"""
        result, output = self._helper("EOF")

        self.assertEqual(output, '\n')
        self.assertEqual(result, True)

    def test_emptyline(self):
        _, output = self._helper("")
        self.assertEqual(output, '')

        _, output = self._helper("   ")
        self.assertEqual(output, '')
