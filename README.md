# CatMan: Photo Catalog Manager

Index large sets of photos for detailed natural language search.


### Environments
Three environments are included: unpinned for debugging, latest used for dev work, and crossplatform useful for CI.
```
conda env create -f environment.yml -n env-unpinned
conda env create -f environment-latest.yml -n env-latest
conda env create -f environment-crossplatform.yml -n env-crossplat
```

### Build & Installation
Choose an appropriate environment to use. Unpinned will resolve the best for the arch you are building on.
```
conda activate env-unpinned
```
Run tests to check that setup is good.
```
pytest test
```
Build wheel and install with `pip`. Clear existing stale builds if they exist.
```
rm -rf build/ dist/ *.egg-info
python3 -m build
pip install --force-reinstall dist/catman-0.1-py3-none-any.whl
```

### Usage
Create a catalog, then search photos with any text description to get the best matches
```
catman create path/to/my/photos path/to/my/ouput_catalog
catman search path/to/my/ouput_catalog "query"
```

Example
```
catman create ~/photos ~/photos/catalog
catman search ~/photos/catalog "a cat wearing sunglasses outside in the sun"
```

```
catman create  ~/Desktop/test_images ~/Desktop/test_images/demo_catalog 
catman search ~/Desktop/test_images/demo_catalog "a whale jumping out of water"
```

Full Help Menu
```
usage: catman [-h] [--log {debug,info,warning,error,critical}] {create,search} ...

CatMan: Catalog Manager for Fast Image Search

positional arguments:
  {create,search}
    create              Loads all jpgs in a directory and creates a catalog
    search              Searches a catalog for the closest images that match query

options:
  -h, --help            show this help message and exit
  --log {debug,info,warning,error,critical}
                        Set the logging level (default: warning)
```

### Support
Works on Windows, Ubuntu, MacOS[Arm, Intel], and Python >=3.9, <=3.11