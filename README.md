# SZE academic tutorials

This repository contains various tutorials teached at the Széchenyi István University (SZE) located in Győr, Hungary.
The tutorials are mostly in hungarian.

## szim2017 branch
### Dependencies

Not every script requires all the packages, but in order to use this repo you may need the following version (or higher) Python packages:

``` python
Python==3.5.2
ipykernel==4.5.2
ipython==5.3.0
ipython-genutils==0.1.0
jupyter-client==5.0.0
jupyter-core==4.3.0
matplotlib==2.0.0
numpy==1.12.0
numpydoc==0.6.0
opencv-python==3.2.0.6
scikit-learn==0.18.1
spyder==3.1.3
tensorflow==1.0.0
notebook==4.4.1
jupyter==1.0.0
Pillow==4.1.0
scipy==0.19.0
wxPython==4.0.0a2
```

### Installation notes on Windows

Download Python 3.5.2 e.g. form here: [python.org/downloads/release/python-352](https://www.python.org/downloads/release/python-352/).
Make sure you check Add Python 3.5 to PATH. After that open a *Command prompt (Admin)*

You can install most of the dependencies with pip install statements. You can individually `pip install package_name`, or as one statement:
```
pip install numpy matplotlib opencv-python jupyter Pillow spyder wxPython
pip3 install --upgrade tensorflow
```

Not every Python package supports Windows, so you need the unofficial Windows binaries for Python extension packages.
You need to manually downolad the `numpy+mkl` and the `scipy` packages. E.g. from here:
[www.lfd.uci.edu/~gohlke/pythonlibs/tuoh5y4k/numpy-1.12.1+mkl-cp35-cp35m-win_amd64.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/tuoh5y4k/numpy-1.12.1+mkl-cp35-cp35m-win_amd64.whl)
[www.lfd.uci.edu/~gohlke/pythonlibs/tuoh5y4k/scipy-0.19.0-cp35-cp35m-win_amd64.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/tuoh5y4k/scipy-0.19.0-cp35-cp35m-win_amd64.whlI)


Then `cd` into the directory and pip install, for example:
```
cd C:\Users\Administrator\Downloads
pip install numpy-1.12.1+mkl-cp35-cp35m-win_amd64.whl
pip install scipy-0.19.0-cp35-cp35m-win_amd64.whl
```

