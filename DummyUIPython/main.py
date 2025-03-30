"""Main entry point to the application."""

from src.infrastructure.app import App


if __name__ == "__main__":
    app = App()
    app.run()
