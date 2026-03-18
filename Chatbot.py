#Code alpha task 2



def get_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm doing great, thank you for asking! How about you?"
    
    elif "weather" in user_input:
        return "I'm not sure, but it's always sunny inside this computer! ☀️"
    
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a wonderful day!"
    
    else:
        return "I'm sorry, I don't quite understand that. Could you try saying 'hello'?"

def start_chat():
    print("--- Rule-Based Chatbot ---")
    print("(Type 'bye' to exit the conversation)")

    while True:
        user_msg = input("You: ")
        
        response = get_bot_response(user_msg)
        
        print(f"Bot: {response}")

        if "bye" in user_msg.lower():
            break

start_chat()