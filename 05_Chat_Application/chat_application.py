import datetime

print("===== Chat Application =====")
print("Type 'bye' to end the chat\n")

# Get usernames
user1_name = input("Enter name for User 1: ")
user2_name = input("Enter name for User 2: ")

chat_history = []

while True:

    # Current time
    time_now = datetime.datetime.now().strftime("%H:%M")

    # User 1 message
    message1 = input(f"{user1_name}: ")

    if message1.lower() == "bye":
        print("Chat ended.")
        break

    formatted_message1 = f"[{time_now}] {user1_name}: {message1}"
    chat_history.append(formatted_message1)

    # User 2 message
    time_now = datetime.datetime.now().strftime("%H:%M")

    message2 = input(f"{user2_name}: ")

    if message2.lower() == "bye":
        print("Chat ended.")
        break

    formatted_message2 = f"[{time_now}] {user2_name}: {message2}"
    chat_history.append(formatted_message2)

# Show chat history
print("\n===== Chat History =====")

for message in chat_history:
    print(message)

# Save chat to file
with open("chat_history.txt", "w") as file:
    for message in chat_history:
        file.write(message + "\n")

print("\nChat history saved successfully.")