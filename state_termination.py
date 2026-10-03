def check_goal(goal):
    if goal == "complete":
        return "SUCCESS"
    else:
        return "FAILURE"


# Example
goal = input("Enter goal status (complete/not complete): ")

result = check_goal(goal)

print("Return State:", result)