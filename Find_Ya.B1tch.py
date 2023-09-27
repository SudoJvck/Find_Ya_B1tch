import requests
import json
import os
import pyfiglet

def search_google_cse(query, api_key, cx):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        if 'items' in data and data['items']:
            return data['items']
        else:
            return None
    else:
        print(f"\nError: Unable to retrieve results. Status code: {response.status_code}")
        return None

def save_to_file(search_results, filename):
    with open(filename, 'w') as file:
        file.write("Search Results:\n\n")
        for index, item in enumerate(search_results, start=1):
            file.write(f"Result {index}:\n")
            file.write(f"Title: {item['title']}\n")
            file.write(f"Link: {item['link']}\n\n")
        print(f"Results saved to {filename}")

def get_input():
    while True:
        input_text = input("Please enter ya bitch: ").strip()
        if input_text:
            return input_text
        else:
            print("Invalid ho. Please enter a solid bitch.")

def ask_another_search():
    while True:
        answer = input("\nDo you want to search for another bitch or have you found your ho? (yes or no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer
        else:
            print("Invalid answer nigga. Please enter 'yes' or 'no'.")

def ask_save_to_file():
    while True:
        answer = input("\nDo you want to save this bitch results to a text file to present later? (yes or no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer
        else:
            print("Invalid answer nigga. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console

    # Banner using pyfiglet
    ascii_banner = pyfiglet.figlet_format("FIND YA' BITCH")
    print(ascii_banner)
    
    api_key = "AIzaSyDFjeHJY4_NOLKqo6tk5-68PtFmzcxFQ_E"
    cx = "303baf3c573c84af5"  # Replace with your Custom Search Engine ID

    while True:
        # Get a valid query
        user_query = get_input()
        print(f"\nSearching for: {user_query}\n")
        search_results = search_google_cse(user_query, api_key, cx)

        if search_results:
            for index, item in enumerate(search_results, start=1):
                print(f"\nResult {index}:")
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}")

            save_choice = ask_save_to_file()
            if save_choice == 'yes':
                filename = input("Enter a filename to save this bitch results: ").strip()
                save_to_file(search_results, filename)
        else:
            print("No search results found.")

        another_search = ask_another_search()
        if another_search == 'no':
            print("Thank you for using Find Ya' Bitch! Goodbye!")
            break
