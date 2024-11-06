from sympy import *
import argparse

init_printing(use_unicode= True)

L1, Rc, Lp, Lc, Lt, alpha_max, Rv, V, h = symbols("L1 Rc Lp Lc Lt alpha_max Rv V h")

# systems of equations to solve 
equations = [
    Eq(L1 + Rc, Lc + Lp - Lt),
    Eq(sin(alpha_max), Rc / L1),
    Eq(sin(alpha_max), V / Rv),
    Eq(cos(alpha_max), h / Rv)
]

def validate(inputs):
    # Check if at least 5 inputs are provided:
    if sum(val is not None for val in inputs.values()) < 5:
        raise ValueError("At least 5 inputs are required")
    
    # Check that at least two of [Lc, Lp, Lt] are provided:
    vars = [inputs["L1"], inputs["Lp"], inputs["Lc"]]
    if sum(val is not None for val in vars) < 2:
        raise ValueError("At least 2 of [Lc, Lp, Lt] are required")
    
    # If all [Lc, Lp, Lt] values are given, check for at least one of [L1, Rc]:
    if all(val is not None for val in vars) and not (inputs["L1"] or inputs["Rc"]):
        raise ValueError("If all of [Lc, Lp, Lt] values are given, at least one of [L1, Rc] must be given") 
    
    return True

def solve_system(inputs):
    
    if not validate(inputs):
        return
    
    known_values = [Eq(symbol, value) for symbol, value in zip(
        [L1, Rc, Lp, Lc, Lt, alpha_max, Rv, V, h], 
        [inputs['L1'], inputs['Rc'], inputs['Lp'], inputs['Lc'], inputs['Lt'], inputs['alpha_max'], inputs['Rv'], inputs['V'], inputs['h']]
    ) if value is not None]

    solution = solve(equations + known_values, dict = True)
    if solution:
        print(f"Solution: {solution}")
    else:
        print("No solution was found with the given inputs")

def parse_args():
    parser = argparse.ArgumentParser(description= "Solve a system of equations with given inputs. You must include at least 5 values.")
    parser.add_argument(
        "values", 
        type = float, 
        nargs = "*",
        help = "Values for L1, Rc, Lp, Lc, Lt, AM, Rv, V, h in order. Omit values you don't know."
    )

    args = parser.parse_args()
    values = args.values + [None] * (9 - len(args.values))

    return dict(zip(['L1', 'Rc', 'Lp', 'Lc', 'Lt', 'alpha_max', 'Rv', 'V', 'h'], values))

if __name__ == "__main__":
    # inputs = parse_args()

    inputs = {
        'L1': 5,
        'Rc': None,
        'Lp': 3,
        'Lc': 4,
        'Lt': None,
        'alpha_max': 0.5,
        'Rv': None,
        'V': 2,
        'h': None
    }

    solve_system(inputs)
