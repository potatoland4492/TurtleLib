# TurtleLib

![v1.0.0](https://img.shields.io/badge/version-1.0.0-informational) ![py-version](https://img.shields.io/pypi/pyversions/PythonTurtle.svg) ![license-gnugpl](https://img.shields.io/badge/license-GNU%20General%20Public%20License-green) ![checks](https://img.shields.io/badge/checks-passing-success) ![tests](https://img.shields.io/badge/tests-passing-success) ![maintainer-akhilpillai](https://img.shields.io/badge/maintainer-Akhil%20Pillai-lightgrey)

TurtleLib is a library of scripts that interact with the PythonTurtle module to create games, drawings, and more!

## Using the Scripts

Copy or download a script to your current working directory. Start python3 and run `import <script-name>`. The program should run automatically.

## Scripts

### Race

This script sets up a simple race layout for two players, one green and the other blue. When the game is set up, the script will prompt you to start the game. Press `Enter` on your keyboard to begin.

[race.py](./scripts/race.py)

### Cone

`cone` creates a nice cone shape using circles. When you import the script, you will be prompted for a size. The recommended range is from 100-250. However, bigger cones will take longer to make. Do not go below 50, as this will result in a very small cone that is hard to see.

[cone.py](./scripts/cone.py)

---

## All Downloads

[TurtleLib_v1.0.0.zip](./downloads/TurtleLib_v1.0.0.zip)

## Installing PythonTurtle

### Debian

```BASH
$ sudo apt-get install --no-install-recommends python3-wxgtk4.0
# Installed dependency
$ sudo apt-get install --no-install-recommends python3-tk
# Installed Tkinter module
$ sudo apt-get install --no-install-recommends python3-pip
# Installed pip if not installed yet
$ python3 -m pip install --user PythonTurtle
# Installed PythonTurtle
```

### Other

See [PythonTurtle's git repository on Github](https://github.com/PythonTurtle/PythonTurtle).
