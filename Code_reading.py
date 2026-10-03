def agent_loop():
    state = 0

    for step in range(2):
        print("Step:", step + 1)

        # Observe
        observation = state
        print("Observe:", observation)

        # Decide
        if observation == 0:
            action = "MOVE"
        else:
            action = "STOP"

        print("Decide:", action)

        # Act
        if action == "MOVE":
            state += 1
            print("Action: Moving")
        else:
            print("Action: Stopping")


agent_loop()