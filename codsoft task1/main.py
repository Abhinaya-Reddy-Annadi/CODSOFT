def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. How can I assist you today?")
    
    while True:
        # Get user input and convert it to lowercase for easier pattern matching
        user_input = input("You: ").lower()
        
        # Respond to different types of user inputs
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you?")
        elif "how are you" in user_input:
            print("Chatbot: I am just a program, but I’m doing well! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I am a rule-based chatbot.")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break  # Exit the loop and end the conversation
        else:
            print("Chatbot: I'm sorry, I don't understand that. Could you please rephrase?")

# Main function to start the chatbot
if __name__ == "__main__":
    chatbot()
