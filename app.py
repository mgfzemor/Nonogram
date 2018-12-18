from flask import Flask,jsonify, render_template, request
from reduction import *
app = Flask(__name__)

matrix = []

@app.route("/")
def hello():
	threeDM = {'M' : [['x1','y1','z1'],['x1','y2','z3'],['x2','y2','z3'],['x2','y3','z2'],['x3','y2','z3'],['x3','y3','z2']],
               'X' : {'x1':1,'x2':2,'x3':3},
               'Y' : {'y1':1,'y2':2,'y3':3},
               'Z' : {'z1':1,'z2':2,'z3':3},
               'q' : 3}
	nonogram = reduction(threeDM)
	threeDM['M'] = mToNonoM(threeDM['M'])
	threeDM['X'] = sorted(threeDM['X'],key=threeDM['X'].get)
	threeDM['Y'] = sorted(threeDM['Y'],key=threeDM['Y'].get)
	threeDM['Z'] = sorted(threeDM['Z'],key=threeDM['Z'].get)
	global matrix 
	matrix = createMatrixP(nonogram['h'],nonogram['w'])
	print(matrix)
	return render_template('index.html',nonogram=nonogram,threeDM=threeDM)

@app.route('/paint_cell')
def add_numbers():
	lin = request.args.get('lin', 0, type=int)
 	col = request.args.get('col', 0, type=int)
	global matrix
	matrix[lin][col] = 1
	print(matrix)
	return jsonify(result=[lin,col])


@app.route('/reduce', methods=['POST'])
def reduce():
	tdm = request.form['tdm']
	threeDM = eval(tdm)
	print(threeDM)
	nonogram = reduction(threeDM)
	threeDM['M'] = mToNonoM(threeDM['M'])
	threeDM['X'] = sorted(threeDM['X'],key=threeDM['X'].get) 
	global matrix 
	matrix = createMatrixP(nonogram['h'],nonogram['w'])
	print(matrix)
	return render_template('index.html',nonogram=nonogram,threeDM=threeDM)
