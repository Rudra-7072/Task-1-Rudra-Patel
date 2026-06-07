def run_friendly_chatbot():
  
    responses = {'hello': "Hey! How's it going?",
        'hi': "Hi there! What can I help you with today?",
        'status': "Everything is running smoothly on my end! How are you doing?",
        'help': "Sure thing! I'm just a simple bot right now, but I can chat a bit or say goodbye.",
        'who are you': "I'm a new chatbot built for DecodeLabs Project 1. Nice to meet you!",
        'bye': "Catch you later! Have a great day."}
    
    print("🤖 Hey! I'm your friendly DecodeLabs chatbot. Let's talk!")
    print("(Just type 'exit' whenever you want to leave the chat)\n")


    while True:
        raw_input = input('You: ')
        clean_input = raw_input.lower().strip()
        if clean_input == 'exit':
            print("Bot: Alright, shutting down. See ya!")
            break
        reply = responses.get(clean_input, "Hmm, I'm not sure I understand that yet. Still learning!")
        print(f"Bot: {reply}")

if __name__ == "__main__":
    run_friendly_chatbot()