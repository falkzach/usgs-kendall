# USGS Seasonal Mann-Kendall Search

## Purpose
The purpose of this project is to wrap the USGS Seasonal Mann-Kendall fortran implementation in a tool that can automate many tests and aggregate results.

## Environment
This tool will only function in a unix environment as pexpect relies on PTYs. 

[WSL](https://docs.microsoft.com/en-us/windows/wsl/install-win10) is a good option for windows users.

### Python Dependencies
* python3
* pandas
* pexpect

If your environment lacks python3, pandas, or pexpect, they can be installed with ```apt-get```.

```
sudo apt-get install python3 python3-pandas python3-pexpect
```

### Acquiring the USGS Mann-Kendall Fortran Code
I cannnot find information on the Licenseing of the USGS Mann-Kendall code, therefor I am not including it in the repository at this time. It can be acquired with the following command.

``` 
wget https://pubs.usgs.gov/sir/2005/5275/downloads/Kendall-new.for
```

### Compiling the USGS Mann-Kendall Fortran Code
If your environment lacks make or the fortran compiler they can be installed with ```apt-get```.

```
sudo apt-get install make gfortran
```

Call ```make``` to compile the USGS Kendal fortran code
```
make
```

### Project Organization

```
usgs-kendall
├── data    - place datasets here
├── results - aggregated experiment results
├── tmp     - temporary intermediate date files and unparsed results, 
├── ...
├── README.md
```

the tmp directory may consume large amounts of disk space if many datasets are run; they must be deleted manually.

```
rm tmp/*
```

## Usage
Experiment parameters are defined in ```main.py```.

```
python3 main.py
```

## License
 
The MIT License (MIT)

Copyright (c) 2019 Zachary Falkner

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
