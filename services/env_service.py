import os
from pathlib import Path

class Env:
    def __int__(self):
        self.os = os.environ.get()
        self.base_dir = Path(__file__).resolve().parent.parent