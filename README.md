# GH-PY

gh-py gh extensions, now made easy in python

### Installation

gh-py can be installed in afew different ways.

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

After installing gh-py you can utilize it through either gh or it's own cli (where you'll create the scaffolding for your extension), or through python (where you can access gh functionality).


#### Creating your extension

To get started, create your extension scaffolding.

```
$ gh py create gh-example
Installing extension environment.
Extension environment installed.
Creating extension gh-example
Creating scaffolding...
Created extension gh-example
````

Then go into your newly created directory, and take a look.

* extension.py - Here is the entry point to your extension.
* gh-example (or what ever else you called your extension) - This is the file that is the bridge between ghs extension system and our python world.
* pyproject.toml - Basic pyproject.toml file, used to describe our project to poetry.


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


