# pyssgen

[![PyPI version](https://badge.fury.io/py/pyssgen.svg)](https://badge.fury.io/py/pyssgen)

pyssgen is a lightweight alternative to hugo and other static site generators.
I used it to build my static blog and included the templates and css that I use along with it.

Please note that it's only a side project and might not be suitable for bigger
websites.


## Installation

### via pip (recommended)

```python
>>> pip install --user pyssgen
```


## Usage

### if installed with pip

```python
>>> python3 -m pyssgen <input-dir> <output-dir> <templates-dir>
```

## templates

In order for pyssgen to work you need to provide a `templates/` directory containing:
* `base.html` the shared headers between all pages,
* `home.html` for the main page of the website,
* `post.html` for "posts" or any other pages

If you don't know how to write templates using jinja,
you can copy the premade [templates](https://github.com/ken-soares/pyssgen/tree/main/pyssgen/templates) folder.

## css
For the program to work you also need the `static/` directory in which you can include the `styles.css` file (not required to work).
Again, you can just copy the provided folders if you want.
