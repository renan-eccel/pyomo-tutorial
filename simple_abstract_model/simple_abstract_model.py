from __future__ import division
import pyomo.environ as poe

model = poe.AbstractModel()

# parameter m
model.m = poe.Param(within=poe.NonNegativeIntegers)
# parameter n
model.n = poe.Param(within=poe.NonNegativeIntegers)

# set I
model.I = poe.RangeSet(1, model.m)
# set J
model.J = poe.RangeSet(1, model.n)

# parameter a
model.a = poe.Param(model.I, model.J)
# parameter b
model.b = poe.Param(model.I)
# parameter c
model.c = poe.Param(model.J)

# variable x
model.x = poe.Var(model.J, within=poe.NonNegativeReals)


def obj_expression(model):
    return poe.summation(model.c, model.x)


model.OBJ = poe.Objective(rule=obj_expression)


def ax_constraint_rule(model, i):
    # return the expression for the constraint for i
    return sum(model.a[i, j] * model.x[j] for j in model.J) >= model.b[i]


# the next line creates one constraint for each number of the set model.I
model.AxbConstraint = poe.Constraint(model.I, rule=ax_constraint_rule)
