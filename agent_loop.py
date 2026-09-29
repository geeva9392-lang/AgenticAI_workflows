# Observe -> Decide -> Act Agent Loop

for i in range(1, 4):

    print(f"\nIteration {i}")

    # Observe
    temperature = int(input("Observe temperature: "))

    # Decide
    if temperature > 100:
        action = "COOL"
    else:
        action = "IDLE"

    # Act
    print("Decision:", action)
    print("Agent Action:", action)

print("\nAgent loop completed!")