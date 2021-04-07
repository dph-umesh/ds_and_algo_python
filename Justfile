# Install poetry from here https://github.com/python-poetry/poetry#osx--linux--bashonwindows-install-instructions
# Install pre-commit from here https://pre-commit.com/#install

setup-dev:
  pre-commit install
  poetry install

# code
lint:
  pre-commit-validate-config
format:
  black .
