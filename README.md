# Installing for Hung Wei's Class

## Installation steps

First pick your python interpreter for the host your are installing
on.  It needs to be the one that will be used by the users.  On
jupyter hosts, it's the interpreter used by jupyter notebook.  On
other hosts, it's the one in a typical user's path.  It needs to be Python 3.

```
PYTHON=python3
```

Second, make sure you have pip and git.

```
apt-get install python3-pip git
```

Then install: 

```
git clone -b devel https://github.com/NVSL/cfiddle.git
cd cfiddle
sudo bin/cfiddle_install_prereqs.sh
sudo `which python` -m pip install .
cd ..
git clone  https://github.com/NVSL/delegate-function.git
cd delegate-function
sudo `which python` -m pip install .
cd ..
git clone https://github.com/NVSL/hungwei-class.git
cd hungwei-class
sudo `which python` -m pip install .
```

Run some tests on cfiddle:

```
`set-cfiddle-ld-path` # note backticks
cd cfiddle/tests
pytest
```

Should pass except maybe `test_doctest.py`

Test running in slurm:

```
cd hungwei-class
pytest
```

Finally, in jupyter notebook:  Open `Example.ipynb` and run it.
