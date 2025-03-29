"""Main application source code."""

import tkinter as tk
from importlib.metadata import PackageNotFoundError, version

from src.components.custom_button import CustomButton

# Global Constants
APP_NAME = "DummyUIApp"


class App:
    """Demo App sets up the UI using tkinter."""

    def __init__(self):
        self.version = self._get_package_version()
        self.root: tk.Tk = tk.Tk()
        self.root.title(APP_NAME + f"v{self.version}")
        self.root.geometry(self._build_window_geometry())
        # Create UI Components
        self._build_ui()

    def _get_package_version(self):
        try:
            # Dynamically fetch the package version
            return version(APP_NAME)
        except PackageNotFoundError:
            # Fallback if package metadata is unavailable
            return "<ERROR GETTING VERSION>"

    def _build_window_geometry(self):
        # Calculate dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set desired width (30% of screen) and height (20% of screen)
        width = int(screen_width * 0.3)
        height = int(screen_height * 0.2)

        # Calculate position to center the window
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set the geometry of the window
        return f"{width}x{height}+{x}+{y}"

    def _build_ui(self):
        # Add version label
        version_label = tk.Label(self.root, text=f"App Version: {self.version}")
        version_label.pack(pady=10)

        # Add button
        action_button = CustomButton(self.root, button_title="Submit Command")
        action_button.pack(pady=10)

    def run(self):
        """Call the mainloop of Tk."""
        self.root.mainloop()
