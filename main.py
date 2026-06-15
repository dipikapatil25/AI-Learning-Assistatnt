from google.adk.runners import Runner
from agent import learning_assistant

runner = Runner(agent=learning_assistant)

print("AI Learning Assistant Started!")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = runner.run(user_input)

    print("Bot:", response)
