# GH-PY

[![Build Status](https://github.com/JessicaTegner/gh-py/actions/workflows/ci.yaml/badge.svg)](https://github.com/JessicaTegner/gh-py/actions/workflows/ci.yaml)
[![GitHub Releases](https://img.shields.io/github/tag/JessicaTegner/gh-py.svg)](https://github.com/JessicaTegner/gh-py/releases)
[![gh-py PyPI Version](https://img.shields.io/pypi/v/gh-py?label=gh-py+pypi+version)](https://pypi.org/project/gh-py/)
[![Development Status](https://img.shields.io/pypi/status/gh-py.svg)](https://pypi.python.org/pypi/gh-py/)
[![gh-py Python version](https://img.shields.io/pypi/pyversions/gh-py.svg)](https://pypi.python.org/pypi/gh-py/)
![License](https://img.shields.io/pypi/l/gh-py.svg)


gh-py gh extensions, now made easy in python.

gh-py makes it possible to write gh extensions, and interact with the gh cli directly from python.

### Installation

gh-py can be installed in a few different ways.

#### From GH.

To use this method, you'll have to have at least gh version 2.0.0 or newer installed.

```
gh extension install JessicaTegner/gh-py
```


#### from pip

gh-py is also available on pip.

```
$ pip install gh-py
```



#### From GitHub

You can also clone and install gh-py from GitHub, useful if you want to contribute to gh-py development.

```
$git clone https://github.com/JessicaTegner/gh-py.git
$ cd gh-py
$ poetry install
```

### Usage:

#### Creating your extension

To get started, create your extension scaffolding.

```
$ gh py create gh-example
# or if you installed through pip
$ gh-py create gh-example
Installing extension environment.
Extension environment installed.
Creating extension gh-example
Creating scaffolding...
Created extension gh-example
````

Then go into your newly created directory, and take a look.

* .gitignore - A default python gitignore, including the exclusion of gh-py files that shouldn't be committed to git
* extension.py - Here is the entry point to your extension.
* gh-example (or what ever else you called your extension) - This is the file that is the bridge between ghs extension system and our python world.
* pyproject.toml - Basic pyproject.toml file, used to describe our project to poetry.


#### Useful tips while developing your extension

When using gh-py's scaffolding, you have the full power of [poetry](https://python-poetry.org/) at your disposal.  
That means you can add, update, change or remove dependencies as you wish.  

The way to do it here, is to use the build in poetry command in the scaffolding, like so:

```
# Here's some examples.
# Note the "gh-example" is the executable for your extension.

$ gh-example poetry add requests
$ gh-example poetry remove requests

```

When you update your extension down the line, the scaffolding will take care to update the extension environment, when the end user updates your extension.  
Note: For this to work, it is important to **not** commit the generated **poetry.lock** file.


#### Publishing your Extension

After writing your python code, the way to publish your extension, is as with any other.

```
# setup a git repository
$ git init -b main
$ git add .
$ git commit -m "Initial extension code."
# then create the repository on GitHub
$ gh repo create
```


### Contributing

Contributions are welcome. When opening a PR, please keep the following guidelines in mind:

1. Before implementing, please open an issue for discussion.
2. Make sure you have tests for the new logic.
3. Add yourself to contributors at `README.md` unless you are already there. In that case tweak your contributions.


#### Contributors

* [Jessica Tegner](https://github.com/JessicaTegner) - Maintainer


### License

Py-GH is available under MIT license. See LICENSE for more details.
