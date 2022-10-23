# pyssgen

[![PyPI version](https://badge.fury.io/py/pyssgen.svg)](https://badge.fury.io/py/pyssgen)

pyssgen is a lightweight alternative to hugo and other static site generators.
I used it to build my static blog and included the templates and css that I use along with it.

Please note that it's only a side project and might not be suitable for bigger
websites.


## Installation

```python
>>> pip install --user pyssgen
```

## Usage

```python
>>> python3 -m pyssgen <input-dir> <output-dir> (optional: <templates-dir>)
```

## customizing

You can make your own templates and css by adding the following files to your
custom templates folder:
* `base.html` common to all files
* `home.html` main page template
* `posts.html` other pages templates

and adding a `styles.css` to `static/` directory.

