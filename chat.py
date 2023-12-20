import os
from dotenv import load_dotenv
import openai
from completion import openai_completion


def create_message(role: str, message: str) -> dict:
    return {"role": role, "content": message}


#def completion(prompt: str) -> dict:    
#    return create_message("system", "I am not saying anything.")


def main():    
    chat_history = {"messages": []}
    preamble = {"role": "system", "content": "You are a helpful assistant."}
    chat_history["messages"].append(preamble)

    should_exit = False
    while(not should_exit):
        
        user_input = input("> ")

        if user_input.lower() == "quit" or user_input.lower() == "exit":
            print("Goodbye!")
            should_exit = True


        user_message = create_message("user", user_input)
        chat_history["messages"].append(user_message)
        system_response = openai_completion(chat_history["messages"])
        chat_history["messages"].append(system_response)
        print(chat_history)




if __name__ == "__main__":
    load_dotenv(dotenv_path=".env")
    openai.api_key = os.getenv("OPENAI_API_KEY")  
    main()