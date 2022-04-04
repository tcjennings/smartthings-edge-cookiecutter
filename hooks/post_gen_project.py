from collections import OrderedDict
from pathlib import Path

from cookiecutter.main import cookiecutter
from cookiecutter.utils import make_executable
from jinja2 import Environment, FileSystemLoader


def get_capabilities(context):
    capabilities = []
    print("Enter SmartThings Device Capabilities for your Driver (Ctrl-D to end):")
    print("  Refer to https://developer-preview.smartthings.com/docs/devices/capabilities/capabilities-reference")
    try:
        while True:
            capabilities.append(input())
    except Exception as e:
        print(e)

    return {
        **context,
        "_capabilities": capabilities,
    }


def get_categories(context):
    categories = []
    print("Enter SmartThings Device Categories for your Driver (Ctrl-D to end):")
    print("  Refer to https://developer-preview.smartthings.com/docs/devices/device-profiles#categories")
    try:
        while True:
            categories.append(input())
    except Exception as e:
        print(e)

    return {
        **context,
        "_categories": categories,
    }


def render_profile(context):
    """Renders the device profile configuration file based on the provided list of capabilities and categories."""
    env = Environment(
        loader=FileSystemLoader("driver/profiles"),
    )
    template = env.get_template("{{cookiecutter.device_name}}.yaml")
    profile = template.render({"cookiecutter": context})
    with open("driver/profiles/{{cookiecutter.device_name}}.yaml", "w") as f:
        f.write(profile)


def remove_unnecessary_files():
    cruft = []

    if "{{cookiecutter.device_network_type}}" == "LAN":
        cruft += [
            Path() / "fingerprints.yaml"
        ]

    for p in cruft:
        try:
            p.unlink()
        except OSError:
            ...


def scripts_to_rule_them_all():
    """Ensures shell scripts are executable."""
    for script in (Path() / "script").iterdir():
        make_executable(script)


def main():
    context: dict = {{ cookiecutter }}
    context = get_capabilities(context)
    context = get_categories(context)
    render_profile(context)
    remove_unnecessary_files()
    scripts_to_rule_them_all()


if __name__ == "__main__":
    main()
