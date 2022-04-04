from pathlib import Path

from cookiecutter.utils import make_executable


def scripts_to_rule_them_all():
    """Ensures shell scripts are executable."""
    for script in (Path() / "script").iterdir():
        make_executable(script)


def main():
    scripts_to_rule_them_all()


if __name__ == "__main__":
    main()
