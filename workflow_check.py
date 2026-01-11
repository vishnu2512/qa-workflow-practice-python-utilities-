def validate_workflow(state):
    valid_states = ["created", "processing", "completed"]

    if state not in valid_states:
        return "Invalid workflow state"

    if state == "created":
        return "Workflow created"
    elif state == "processing":
        return "Workflow in progress"
    else:
        return "Workflow completed successfully"

if __name__ == "__main__":
    user_state = input("Enter workflow state: ").lower()
    result = validate_workflow(user_state)
    print(result)
