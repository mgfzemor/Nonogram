# :black_square_button: 3DM to NONOGRAM :white_square_button:
Presents a graphical reduction from 3DM (3-dimensional matching) to NONOGRAM used to proof the NP-Completeness of NONOGRAM the algorithm used was proposed in: Ueda, Nobuhisa; Nagao, Tadaaki (1996), NP-completeness results for NONOGRAM via Parsimonious Reductions - [View full text](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.57.5277)

#### Given a 3DM instance the algorithm generates a instance of NONOGRAM, then you can start to color the cells that satisfy row and column constraints, finally press "Verify solution" button to check that your solution is correct.
##### Example of 3DM instance
X = {x1,x2,x3}; Y = {y1,y2,y3}; Z = {z1,z2,z3}

M = { <x1,y1,z1>, <x1,y2,z3>,  <x2,y2,z3>, <x2,y3,z2>, <x3,y2,z3>, <x3,y3,z2>}

M' = { <x1,y1,z1>, <x2,y2,z3>, <x3,y3,z2>}

n = |M| = 6 

q = |M'| = |X| = |Y| = |Z| = 3
##### Output
![GitHub Logo](https://github.com/mgfzemor/Nonogram/blob/master/docs/img/example1.png)


### :floppy_disk: Prerequisites
To have this running your local machine, you only must have a Python version >= 2.7 and Virtualenv tool. 

Learn more about [Virtualenv](https://virtualenv.pypa.io/en/latest/), which is pretty useful to isolated Python environments.
- Installing Virtualenv
```bash
$ sudo apt-get install virtualenv
```

### :zap: Getting Started
- Install application requirements listed above
- clone project

```bash
$ git clone https://github.com/mgfzemor/Nonogram.git
```
- Go to project path and create a virtual environment

```bash
$ cd Nonogram/ && virtualenv env
```

- Active the virtualenv and install requirements
```bash
$ . /env/bin/activate && pip install -r requirements.txt
```

- Run application
```bash
$ flask run
```
