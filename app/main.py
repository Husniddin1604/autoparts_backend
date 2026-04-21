from core.factory import create_app


app = create_app()


if __name__ == "__main__":
    from core.server import run
    run()
