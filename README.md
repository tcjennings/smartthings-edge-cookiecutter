# Install Cookiecutter

See [cookiecutter](https://github.com/cookiecutter/cookiecutter).

For macOS, [homebrew](https://brew.sh) gets you started:

```
brew install cookiecutter
```

# User Config

To save time now and in the future, set up a user configuration file.

```
cat <<EOF >> ~/.cookiecutterrc
default_context:
  full_name: "Your Name"
  email: "your.name@example.com"
abbreviations:
  smartthings: https://github.com/tcjennings/smartthings-edge-cookiecutter.git
```

# Create a New Project

Create a new project by calling `cookiecutter` in your preferred local working directory with the abbreviation set in your user config.

```
cd ~/git
cookiecutter smartthings
cd ~/git/my-project-slug
code .
```

# Using The Project

## Prerequisites

- `node`
- `nvm`
