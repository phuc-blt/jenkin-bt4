# Mark this directory as a Python package.

# Optional: Define metadata for the package
__version__ = "1.0.0"
__author__ = "Nguyen Trong Phuc"
__description__ = "A simple FastAPI app to check prime numbers and return version"

# You can import important components here to make them easily accessible
# For example, making app.main available directly as app
from .main import app

# You can also expose commonly used functions or variables here for easier access
# Example: making 'check_prime' function easily accessible from the package
from .main import check_prime
