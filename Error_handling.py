def perform_action(action):
    if action == "start":
        return {"status": "success", "message": "Action started"}

    elif action == "stop":
        return {"status": "success", "message": "Action stopped"}

    else:
        return {
            "status": "error",
            "error": "Invalid action",
            "message": f"'{action}' is not a valid action"
        }


# Test
result = perform_action("jump")

print(result)
