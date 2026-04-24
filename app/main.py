import os
import sys

from core.factory import create_app

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = create_app()


if __name__ == "__main__":
    from core.server import run
    run()
