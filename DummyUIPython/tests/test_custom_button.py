"""Unit Tests to ensure robust button functionality."""

import unittest
import tkinter as tk
from src.components.custom_button import CustomButton


class TestCustomButton(unittest.TestCase):
    """Test for the Custom Button Component."""

    def setUp(self):
        # Setup the root Tkinter instance for testing
        self.root = tk.Tk()
        self.button_title = "Test Button"

    def test_button_initialization(self):
        """Test to ensure the button is correctly initialized."""
        # Initialize the CustomButton
        button: CustomButton = CustomButton(
            parent=self.root, button_title=self.button_title
        )

        # Verify the button title text
        self.assertEqual(
            button["text"], self.button_title, "Button title text does not match!"
        )

        # Verify the parent of the button
        self.assertEqual(button.parent, self.root, "Button parent is incorrect!")

    def tearDown(self):
        # Destroy the root instance to prevent tkinter errors
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
