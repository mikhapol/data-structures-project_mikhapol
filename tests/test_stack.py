"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Stack


class TestStack(unittest.TestCase):
    def test_push(self):
        test_stack_push = Stack()
        test_stack_push.push("One")
        self.assertEqual(test_stack_push.top.data, "One")
        test_stack_push.push("Two")
        self.assertEqual(test_stack_push.top.data, "Two")
        self.assertEqual(test_stack_push.top.next_node.data, "One")
