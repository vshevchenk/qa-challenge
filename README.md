# qa-challenge

## Prerequisites
- Python 3.6^ is installed
- [Poetry](https://python-poetry.org/) is installed
- create `credentials.yml` file at project root based on [credentials.yaml.template]
(credentials.yaml.template)

Use your email and password

## Run tests:
`poetry run pytest` at project root

## Check code-style
`Poetry run flake8` at project root

## Portability
- tested with Google Chrome 81^ on Ubuntu 18.04
- other combinations should be available from the box but behavior may differ
- for compatibility reasons requirements.txt has been added and can be used to run project without 
poetry