import openai

# Set up your OpenAI API credentials
openai.api_key = 'enter API KEY here'

# Define a function to generate a response from ChatGPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n = 1,
        stop=None
    )
    return response.choices[0].text.strip()

# Main chat loop
print("Bot: Hello! How can I assist you today?")
while True:
    user_input = input("User: ")

    # Exit the loop if the user says goodbye
    if user_input.lower() in ['bye', 'goodbye']:
        print("Bot: Goodbye! Have a great day!")
        break

    # Generate a response from ChatGPT
    prompt = f"User: {user_input}\nBot:"
    bot_response = generate_response(prompt)
    print("Bot:", bot_response)
