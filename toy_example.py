from z3 import And, Int, Solver, sat

# Employee information
months_worked = Int("months_worked")
hours_worked = Int("hours_worked")

# Simplified leave eligibility policy
eligible = And(
    months_worked >= 12,
    hours_worked >= 1250
)

# Example: employee worked 14 months and 1100 hours
solver = Solver()
solver.add(months_worked == 14)
solver.add(hours_worked == 1100)
solver.add(eligible)

result = solver.check()

print("Z3 result:", result)

if result == sat:
    print("Policy verdict: ELIGIBLE")
else:
    print("Policy verdict: NOT ELIGIBLE")