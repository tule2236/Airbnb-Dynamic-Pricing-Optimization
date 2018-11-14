##ISYE 4803 
##Airbnb Project 
from __future__ import division
from pyomo.environ import *
import pyomo.opt
import math
import pprint 
import csv



#####Please substitute the input with the real input data
##########Parameters##########
Cv = 20.0
I0 = 300.0
X_0=100.0


##########Decision_Variables###########
# i = 1.......12 
# j = 1, 2, 3, 4/ j = 5,6,7
# binary variable(if customer decide to book airbnb property)


numDays = 6
model = ConcreteModel()

month = [1,2,3,4,5,6,7,8,9,10,11,12]

model.month = Set(initialize = month)
model.day = RangeSet(1,7)

model.alpha_ij = Var(model.month, model.day, within=Binary)
model.x_ij = Var(model.month,model.day, within=PositiveReals)
model.d_ij = Var(model.month,model.day, within=PositiveReals)

model.boundX = ConstraintList()
for m in model.month:
	for d in model.day:
		model.boundX.add(model.x_ij[m,d] == model.alpha_ij[m,d] * X_0)
		# model.boundX.add(model.x_ij[m,d] = model.alpha_ij[m,d]*X_0)
		model.boundX.add(model.d_ij[m,d] == -0.2417 * model.x_ij[m,d]*model.x_ij[m,d] +18.039*model.x_ij[m,d]+551.46)
model.obj = Objective(expr = sum(model.alpha_ij[m,d] * model.x_ij[m,d]
	-model.alpha_ij[m,d]*Cv-I0 for m in model.month for d in model.day), sense = maximize)

opt = SolverFactory('gurobi')
instance = model.create()
results = opt.solve(instance)
instance.display()
