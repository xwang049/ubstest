from flask import Flask, request

app = Flask(__name__)
import json
import logging


from routes import app
# Helper function to evaluate conditions
def evaluate_condition(left, operator, right, variables):
    try:
        left_val = int(left)
    except ValueError:
        left_val = variables.get(left, 0)  # Use 0 if not found in variables
    
    try:
        right_val = int(right)
    except ValueError:
        right_val = variables.get(right, 0)  # Use 0 if not found in variables
    
    if operator == "==":
        return left_val == right_val
    elif operator == "!=":
        return left_val != right_val
    elif operator == ">":
        return left_val > right_val
    elif operator == "<":
        return left_val < right_val
    
    return False


def perform_operation(target, operator, operand, variables, int1):
    try:
        operand_val = int(operand)
    except ValueError:
        operand_val = variables.get(operand, 0)  # Use 0 if not found in variables
    
    if operator == "+":
        variables[target] = int1 + operand_val
    elif operator == "-":
        variables[target] = int1 - operand_val
    elif operator == "*":
        variables[target] = int1 * operand_val
    elif operator == "/":
        variables[target] = int1 // operand_val

def handle_operation(statement, variables):
    parts = statement.split()
    target = parts[0]
    int1 = parts[2]
    operator = parts[3]
    operand = parts[4]

    try:
        int1_val = int(int1)
    except ValueError:
        int1_val = variables.get(int1, 0)  # Use 0 if not found in variables

    perform_operation(target, operator, operand, variables, int1_val)

# Modify the swissbyte function
def swissbyte(code, cases):
    outcomes = []

    for case in cases:
        variables = case.copy()
        is_solvable = True
        i = 0

        while i < len(code):
            line = code[i]
            parts = line.split()

            if parts[0] == "if":
                condition = parts[1]
                if not evaluate_condition(condition, parts[2], parts[3], variables):
                    # Skip to endif
                    level = 1
                    while level > 0:
                        i += 1
                        if code[i] == "if":
                            level += 1
                        elif code[i] == "endif":
                            level -= 1
            elif parts[0] == "endif":
                pass  # End of if block, continue to the next line
            elif parts[0] == "fail":
                is_solvable = False
                break
            elif len(parts) == 3:  # Assignment
                target = parts[0]
                operator = parts[1]
                operand = parts[2]

                if operator == "=":
                    try:
                        operand_val = int(operand)
                    except ValueError:
                        operand_val = variables.get(operand, 0)  # Use 0 if not found in variables

                    variables[target] = operand_val
            elif len(parts) == 5:  # Operation
                handle_operation(line, variables)

            i += 1  # Move to the next line

        outcome = {"is_solvable": is_solvable, "variables": variables}
        outcomes.append(outcome)

    return {"outcomes": outcomes}



@app.route('/swissbyte', methods=['POST'])
def swissbyteRun():
    data = request.get_json()
    code = data.get("code")
    cases = data.get("cases")
    res = swissbyte(code,cases)
    return json.dumps(res)


