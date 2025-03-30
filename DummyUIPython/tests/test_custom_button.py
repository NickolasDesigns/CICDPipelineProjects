"""Unit Tests to ensure robust button functionality."""

import unittest
import tkinter as tk
from unittest.mock import Mock, patch
from src.components.custom_button import CustomButton


class TestCustomButton(unittest.TestCase):
    """Test for the Custom Button Component."""

    def setUp(self) -> None:
        # Setup the root Tkinter instance for testing
        self.root = tk.Tk()
        self.button_title = "Test Button"

    def test_button_initialization(self) -> None:
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

        # Verify the instance reference
        self.assertIsInstance(
            button, tk.Button, "Button is not a tk.Button instance as expected."
        )

    @patch("tkinter.messagebox.showinfo")  # Mock the messagebox.showinfo method
    def test_button_click_opens_dialog(self, mock_showinfo: Mock) -> None:
        """Test to ensure the button click opens a dialog."""
        button = CustomButton(parent=self.root, button_title="Test Button")

        # Simulate button click
        button.invoke()

        # Assert that messagebox.showinfo was called with correct parameters
        mock_showinfo.assert_called_once_with(
            "Button Clicked", "Hello! You clicked the button."
        )

    def tearDown(self) -> None:
        # Destroy the root instance to prevent tkinter errors
        self.root.destroy()


if __name__ == "__main__":
    unittest.main()
