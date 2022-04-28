# Import OR-Tools wrapper for linear programming
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver('Maximize Arrecadação', pywraplp.Solver.SCIP_MIXED_INTEGER_PROGRAMMING)

# Create the variables we want to optimize
x1 = solver.IntVar(0, solver.infinity(), 'unidade simples')
x2 = solver.IntVar(0, solver.infinity(), 'unidade dupla')
x3 = solver.IntVar(0, solver.infinity(), 'unidade tripla')
x4 = solver.IntVar(0, solver.infinity(), 'unidade quádrupla')
x5 = solver.IntVar(0, solver.infinity(), 'casa antigas a demolir')

# Add constraints for each resource
solver.Add(0.18 * x1 + 0.28 * x2 + 0.4 * x3 + 0.5 * x4 - 0.2125 * x5 <= 0) #área ocupada pelas novas casas
solver.Add(x5 <= 300) #Limite de casa demolidas
solver.Add(x1 - 0.2 * (x1 + x2 + x3 + x4) >= 0 ) #unidade simples deve representar no mínimo 20% de todas as unidades
solver.Add(x2 - 0.1 * (x1 + x2 + x3 + x4) >= 0 ) #unidade dupla devem representar no mínimo  10% de todas as unidades
solver.Add(x3 + x4 - 0.25 * (x1 + x2 + x3 + x4) >= 0) # unidades tripals e quádruplas devem representar no mínimo 25% de todas as unidades

solver.Maximize(1000 * x1 + 1900 * x2 + 2700 * x3 + 3400 * x4)

status = solver.Solve()

# If an optimal solution has been found, print results
if status == pywraplp.Solver.OPTIMAL:
  print('================= Solution =================')
  print(f'Solved in {solver.wall_time():.2f} milliseconds in {solver.iterations()} iterations\n')
  print(f'Arrecadação_Max = {solver.Objective().Value()}')
  print(f' - Unidades simples = {x1.solution_value()}')
  print(f' - Unidades duplas = {x2.solution_value()}')
  print(f' - Unidades triplas = {x3.solution_value()}')
  print(f' - Unidades quádruplas = {x4.solution_value()}')
  print(f' - Unidades demolidas = {x5.solution_value()}')
  
else:
  print('The solver could not find an optimal solution.')