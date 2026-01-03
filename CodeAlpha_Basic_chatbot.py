def chatbot():
    print("Chatbot: Hello! I am a simple bot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm functioning perfectly!")
        elif "name" in user_input:
            print("Chatbot: My name is AlphaBot.")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Could you try saying 'hello'?")

chatbot()