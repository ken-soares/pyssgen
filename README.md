# pyssgen

pyssgen is a lightweight alternative to hugo and other static site generators.
I used it to build my static blog and included the templates and css that I use along with it.

Please note that it's only a side project and might not be suitable for bigger
websites.


## Installation

### via pip

```python
>>> pip install --user pyssgen
```

### via git

```bash
git clone https://github.com/ken-soares/pyssgen.git
pip install -r requirements.txt
chmod +x pyssgen/pyssgen/pyssgen.py
```


## Usage

### if installed with pip

```python
>>> python3 -m pyssgen <input-dir> <output-dir> (optional: <templates-dir>)
```
### if installed with git

```bash
cd path/to/pyssgen
./pyssgen.py <input-dir> <output-dir> (optional: <templates-dir>)
```

## Customisation

### templates

You can create your own templates folder following theses naming conventions:
* `base.html` is common part between all pages.
* `home.html` is the name used for the main page template.
* `post.html` is the name used for posts template.

### css

Simply replace the existing css file in `dist/static/styles.css` with your own.
