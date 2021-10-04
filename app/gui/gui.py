import tkinter as tk
from tkinter import *
import json
import os
from run_am import run_sim

def test_var(x):
    aux = tk.StringVar()
    aux.set(x)
    return aux.get()

values = {}
root = tk.Tk()

test_dict = {'Dimension' : test_var("3"), 
                'Units' : test_var("lj"), 
                'Boundary' : test_var("p p p"), 
                'Atom style' : test_var("atomic"), 
                'Neighbor' : test_var("0.3"), # Optional
                'Modify neighbor list' : test_var("20,0"), # Optional
                'Lattice' : test_var("fcc"), # Could implement random inside this
                'Lattice parameter' : test_var("0.8442"),
                'Region x min' : test_var("0"),
                'Region x max' : test_var("20"), 
                'Region y min' : test_var("0"),
                'Region y max' : test_var("20"), 
                'Region z min' : test_var("0"),
                'Region z max' : test_var("20"),
                'Mass' : test_var("2.0"),
                'Temperature' : test_var("0.1"),
                'Pair style' : test_var("lj/cut 2.5"),
                'Pair coefficients' : test_var("1.0 1.0 2.5"),
                'Fix' : test_var("nve"), 
                'Time step' : test_var("0.01"),
                'Steps' : test_var("1000")}

root.geometry("1920x1080")
rowNumberLabel = 1
rowNumberBox = 2


def define_row_label():
    global rowNumberLabel 
    rowNumberLabel += 1
    return rowNumberLabel

def define_row_box():
    global rowNumberBox
    rowNumberBox += 1
    return rowNumberBox

def setValues():
    global values
    values = {'Dimension' : dimensionValue.get(), 
             'Units' : unitsValue.get(), 
             'Boundary' : boundaryValue.get(), 
             'Atom style' : AtomStyleValue.get(), 
             'Neighbor' : neighborValue.get(), # Optional
             'Modify neighbor list' : neighborModifyValue.get(), # Optional
             'Lattice' : latticeValue.get(), # Could implement random inside this
             'Lattice parameter' : latticeParameterValue.get(),
             'Region x min' : regionMinXValue.get(),
             'Region x max' : regionMaxXValue.get(), 
             'Region y min' : regionMinYValue.get(),
             'Region y max' : regionMaxYValue.get(), 
             'Region z min' : regionMinZValue.get(),
             'Region z max' : regionMaxZValue.get(),
             'Mass':massValue.get(),
             'Temperature' : temperatureValue.get(),
             'Pair style' : pairStyleValue.get(),
             'Pair coefficients' : pairCoefficientsValue.get(),
             'Fix' : fixValue.get(), 
             'Time step' : timeStepValue.get(),
             'Steps' : stepsValue.get()}

def submit():
    setValues()
    #print(values)
    #os.system('python3 run_am.py')
    run_sim(values)

def submit_test():
    run_sim(test_dict)
    

# Variables 
dimensionValue = tk.StringVar()
unitsValue = tk.StringVar()
boundaryValue = tk.StringVar()
AtomStyleValue = tk.StringVar()
neighborValue = tk.StringVar()
neighborModifyValue = tk.StringVar()
latticeValue = tk.StringVar()
latticeParameterValue = tk.StringVar()
regionsValue = tk.StringVar()
regionMinXValue = tk.StringVar()
regionMaxXValue = tk.StringVar()
regionMinYValue = tk.StringVar()
regionMaxYValue = tk.StringVar()
regionMinZValue = tk.StringVar()
regionMaxZValue = tk.StringVar()
pairStyleValue = tk.StringVar()
pairCoefficientsValue = tk.StringVar()
massValue = tk.StringVar()
temperatureValue = tk.StringVar()
fixValue = tk.StringVar()
timeStepValue = tk.StringVar()
stepsValue = tk.StringVar()


#Title
title = Label(text="MaterialsGUI",font=("Roma",25)).grid(row=1, column=6)

#Labels
#Initialize
initializeLabel = Label(text="Initialization",font=("Roma",17))

dimensionLabel = Label(text="Dimension:",font=("Roma",12))
unitsLabel = Label(text="Units:",font=("Roma",12))
boundaryLabel = Label(text="Boundary:",font=("Roma",12))
atomStyleLabel = Label(text="Atom Style:",font=("Roma",12))
neighborLabel = Label(text="Neighbor:",font=("Roma",12))
neighborModifyLabel = Label(text="Neighbor Modify:",font=("Roma",12))

initializeLabel.grid(row=define_row_label(), column=1)

dimensionLabel.grid(row=define_row_label(), column=1)
unitsLabel.grid(row=define_row_label(), column=1)
boundaryLabel.grid(row=define_row_label(), column=1)
atomStyleLabel.grid(row=define_row_label(), column=1)
neighborLabel.grid(row=define_row_label(), column=1)
neighborModifyLabel.grid(row=define_row_label(), column=1)


#System definition
systemDefinitionLabel = Label(text="System Definition",font=("Roma",17))

latticeLabel = Label(text="Lattice:",font=("Roma",12))
latticeParameterLabel = Label(text="Laticce Parameter:",font=("Roma",12))
regionsLabel = Label(text="Region:",font=("Roma",12))
regionMinXLabel = Label(text="Min x:",font=("Roma",12))
regionMaxXLabel = Label(text="Max x:",font=("Roma",12))
regionMinYLabel = Label(text="Min y:",font=("Roma",12))
regionMaxYLabel = Label(text="Max y:",font=("Roma",12))
regionMinZLabel = Label(text="Min z:",font=("Roma",12))
regionMaxZLabel = Label(text="Max z:",font=("Roma",12))

systemDefinitionLabel.grid(row=define_row_label(), column=1)

latticeLabel.grid(row=define_row_label(), column=1)
latticeParameterLabel.grid(row=define_row_label(), column=1)

regionsLabel.grid(row=define_row_label(), column=1)
regionMinXLabel.grid(row=define_row_label(), column=1)
regionMaxXLabel.grid(row=rowNumberLabel, column=3)
regionMinYLabel.grid(row=define_row_label(), column=1)
regionMaxYLabel.grid(row=rowNumberLabel, column=3)
regionMinZLabel.grid(row=define_row_label(), column=1)
regionMaxZLabel.grid(row=rowNumberLabel, column=3)


#Simulation Settings
simulationSettingsLabel = Label(text="Simulation Settings",font=("Roma",17))

pairStyleLabel = Label(text="Pair Style:",font=("Roma",12))
pairCoefficientsLabel = Label(text="Pair Coefficents:",font=("Roma",12))
MassLabel = Label(text="Mass:",font=("Roma",12))
temperatureLabel = Label(text="Temperature",font=("Roma",12))

simulationSettingsLabel.grid(row=define_row_label(), column=1)

pairStyleLabel.grid(row=define_row_label(), column=1)
pairCoefficientsLabel.grid(row=define_row_label(), column=1)
MassLabel.grid(row=define_row_label(), column=1)
temperatureLabel.grid(row=define_row_label(), column=1)


#Simulation Run
SimulationRunLabel = Label(text="Simulation Run",font=("Roma",17))

FixLabel = Label(text="Fix:",font=("Roma",12))
timeStepLabel = Label(text="Time Step:",font=("Roma",12))
stepsLabel = Label(text="Steps:",font=("Roma",12))

SimulationRunLabel.grid(row=define_row_label(), column=1)

FixLabel.grid(row=define_row_label(), column=1)
timeStepLabel.grid(row=define_row_label(), column=1)
stepsLabel.grid(row=define_row_label(), column=1)

#Box entries
#Initialize
dimensionBox = Entry(root,textvariable=dimensionValue)
unitsBox = Entry(root,textvariable=unitsValue)
boundaryBox = Entry(root,textvariable=boundaryValue)
atomStyleBox = Entry(root,textvariable=AtomStyleValue)
neighborBox = Entry(root,textvariable=neighborValue)
neighborModifyBox = Entry(root,textvariable=neighborModifyValue)

dimensionBox.grid(row=define_row_box(), column=2)
unitsBox.grid(row=define_row_box(), column=2)
boundaryBox.grid(row=define_row_box(), column=2)
atomStyleBox.grid(row=define_row_box(), column=2)
neighborBox.grid(row=define_row_box(), column=2)
neighborModifyBox.grid(row=define_row_box(), column=2)

#System definition
rowNumberBox += 1

latticeBox = Entry(root,textvariable=latticeValue)
latticeParameterBox = Entry(root,textvariable=latticeParameterValue)

regionMinXBox = Entry(root,textvariable=regionMinXValue)
regionMaxXBox = Entry(root,textvariable=regionMaxXValue)
regionMinYBox = Entry(root,textvariable=regionMinYValue)
regionMaxYBox = Entry(root,textvariable=regionMaxYValue)
regionMinZBox = Entry(root,textvariable=regionMinZValue)
regionMaxZBox = Entry(root,textvariable=regionMaxZValue)

latticeBox.grid(row=define_row_box(), column=2)
latticeParameterBox.grid(row=define_row_box(),column=2)

rowNumberBox += 1

regionMinXBox.grid(row=define_row_box(), column=2)
regionMaxXBox.grid(row=rowNumberBox, column=4)
regionMinYBox.grid(row=define_row_box(), column=2)
regionMaxYBox.grid(row=rowNumberBox, column=4)
regionMinZBox.grid(row=define_row_box(), column=2)
regionMaxZBox.grid(row=rowNumberBox, column=4)

#Simulation settings
rowNumberBox += 1

pairStyleBox = Entry(root,textvariable=pairStyleValue)
pairCoefficientsBox = Entry(root,textvariable=pairCoefficientsValue)
massBox = Entry(root,textvariable=massValue)
temperatureBox = Entry(root,textvariable=temperatureValue)

pairStyleBox.grid(row=define_row_box(), column=2)
pairCoefficientsBox.grid(row=define_row_box(), column=2)
massBox.grid(row=define_row_box(), column=2)
temperatureBox.grid(row=define_row_box(), column=2)


#Simulation Run
rowNumberBox += 1

fixBox = Entry(root,textvariable=fixValue)
timeStepBox = Entry(root,textvariable=timeStepValue)
stepsBox = Entry(root,textvariable=stepsValue)

fixBox.grid(row=define_row_box(), column=2)
timeStepBox.grid(row=define_row_box(), column=2)
stepsBox.grid(row=define_row_box(), column=2)

#Submit button
Button(text="submit", command=submit).grid(row=define_row_box(), column=6)
Button(text='Test', command=submit_test).grid(row=define_row_box(), column=6)


root.mainloop()

