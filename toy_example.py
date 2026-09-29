from z3 import And, Int, Not, Solver, sat, unsat

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

# Check whether ELIGIBLE is possible
solver.push()
solver.add(eligible)
eligible_result = solver.check()
solver.pop()

# Check whether NOT ELIGIBLE is possible
solver.push()
solver.add(Not(eligible))
not_eligible_result = solver.check()
solver.pop()

print("Eligible result:", eligible_result)
print("Not eligible result:", not_eligible_result)

if eligible_result == sat and not_eligible_result == unsat:
    print("Policy verdict: ELIGIBLE")
elif eligible_result == unsat and not_eligible_result == sat:
    print("Policy verdict: NOT ELIGIBLE")
elif eligible_result == sat and not_eligible_result == sat:
    print("Policy verdict: NO DECISION")
elif eligible_result == unsat and not_eligible_result == unsat:
    print("Policy verdict: INCONSISTENT FACTS")
else:
    print("Policy verdict: UNKNOWN")c