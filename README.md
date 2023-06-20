# Travel assistant

Travel assistant will help users decide where to go

- you will tell what you wanna do, such as “I wanna do a road trip from Boston to somewhere that has some lakes or natural places with a lot of hiking trails. I can drive at most 3-4 hours, what are my options“, and this tool will give you some suggestions.
- It will use multiple tools such as
    - chatgpt or similar (bard etc)
    - wolfram alpha LLM (https://products.wolframalpha.com/llm-api/documentation) for verification
    - temperature-related tools (finding the temperature at the place at the travel dates, or previous years)
    - Nerdwallet and a bunch of other APIs

### What it can do

- here are some of the things it can do
    - help find a location
    - some kinda cost estimator (very difficult though!). Maybe direct link to NerdWallet or use NerdWallet API if exists
    - a tool to figure out temperature at travel time / temperature in the past X years
    - things about currency
    - travel guidance from the US embassy
    - tips&tricks to save money
    - some cultural insights, what to do what not to do, etc
    - links to find best sim card, best taxi app etc
    - air pollution/UV
- It can also have connections to airlines, Skyscanner, hopper, etc, and help users install their apps.

## Motivation

I used ChatGPT for this and I really like this. The whole decision process took hours though. I think such a tool may make people's lives so much easier. 

## Installation

### Prerequisite: `pyenv`

https://github.com/pyenv/pyenv-installer

On macOS you can use [brew](https://brew.sh), but you may need to grab the `--HEAD` version for the latest:

```bash
brew install pyenv --HEAD
```

or

```bash
curl https://pyenv.run | bash
```

And then you should check the local `.python-version` file or `.envrc` and install the correct version which will be the basis for the local virtual environment. If the `.python-version` exists you can run:

```bash
pyenv install
```

This will show a message like this if you already have the right version, and you can just respond with `N` (No) to cancel the re-install:

```bash
pyenv: ~/.pyenv/versions/3.8.6 already exists
continue with installation? (y/N) N
```

### Prerequisite: `direnv`

https://direnv.net/docs/installation.html

```bash
curl -sfL https://direnv.net/install.sh | bash
```


### Developer Setup

If you are a new developer to this package and need to develop, test, or build -- please run the following to create a developer-ready local Virtual Environment:

```bash
direnv allow
python --version
pip install --upgrade pip
pip install poetry
poetry install
```
