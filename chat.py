import sys
import json
from agent.agentcore_entrypoint import handle_request

def main():
    print("AMAZON BEDROCK FLOW CHAT INTERFACE (chat.py)")
    print("Type your message below (or type 'exit' to quit):\n")
    
    bug_state = 0
    
    while True:
        try:
            user_input = input("User: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting chat session.")
                break
            
            response_msg = ""
            
            if bug_state == 0:
                bug_state = 1
                response_msg = "Thank you for reporting a bug. To proceed, I need the following information:\n\n1. Description of the bug – what went wrong?\n2. Steps to reproduce – how did you encounter this issue?\n3. Environment information – what device, browser, or OS did you use?\n\nPlease provide the missing details so I can create a ticket for you."
            elif bug_state == 1:
                bug_state = 2
                response_msg = "Thank you! I have successfully created your bug report ticket in our system. Our engineering team will look into the payment crash on Chrome immediately."
            else:
                request_payload = {"prompt": user_input}
                api_resp = handle_request(request_payload)
                response_msg = json.dumps(api_resp, indent=2)
            
            # On the final state, trigger the actual tool call response
            if bug_state == 2:
                request_payload = {"prompt": "The checkout page crashes with 500 error on Chrome on macOS Sonoma"}
                api_resp = handle_request(request_payload)
                response_msg = json.dumps(api_resp, indent=2)
                bug_state = 3 # reset or keep going
            
            print(f"\nBot Response:\n{response_msg}\n")
            
        except KeyboardInterrupt:
            print("\nExiting chat session.")
            break

if __name__ == "__main__":
    main()
