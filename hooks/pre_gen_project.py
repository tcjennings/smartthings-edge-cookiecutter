def get_capabilities(context):
    capabilities = []
    print("Enter SmartThings Device Capabilities for your Driver (Ctrl-D to end):")
    try:
        while True:
            capabilities.append(input())
    except Exception as e:
        print(e)

    return {
        **context,
        "capabilities": capabilities
    }


def main():
    context: dict = {{ cookiecutter }}
    get_capabilities(context)


if __name__ == "__main__":
    main()
