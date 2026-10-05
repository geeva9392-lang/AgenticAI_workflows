def agent_action(action):
    if action == "start":
        return {"status": "success", "action": "started"}

    elif action == "stop":
        return {"status": "success", "action": "stopped"}

    elif action == "pause":
        return {"status": "success", "action": "paused"}

    else:
        return {
            "status": "error",
            "error": "Invalid action",
            "action": action
        }


# Test cases
print(agent_action("start"))
print(agent_action("pause"))
print(agent_action("hello"))