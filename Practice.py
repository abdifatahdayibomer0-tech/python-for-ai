import requests


def run_joke_machine():
    user_name = input("Enter your name: ")

    agify_url = f"https://api.agify.io/?name={user_name}"
    joke_url = "https://official-joke-api.appspot.com/random_joke"

    print(f"\n--- Fetching data for {user_name}... ---\n")

    try:
        # ---- Task A: Predict Age ----
        age_response = requests.get(agify_url, timeout=5)
        age_response.raise_for_status()
        age_data = age_response.json()

        predicted_age = age_data.get("age", "unknown")
        print(f"Based on your name, I guess you are {predicted_age} years old!")

        # --- TASK B: Get a joke ---

        joke_response = requests.get(joke_url, timeout=5)
        joke_response.raise_for_status()
        joke_data = joke_response.json()

        print(f"😂 Here is a joke for you:")
        print(f"Setup: {joke_data['setup']}")
        input("... (Press Enter for the punchline)...")
        print(f"Punchline: {joke_data['punchline']}")

    except requests.exceptions.ConnectionError:
        print("❌ Error: Check your internet connection!")
    except requests.exceptions.HTTPError as err:
        print(f"❌ API Error: The server returned a{err.response.status_code} errors.")
    except Exception as e:
        print(f"❌ Something went wrong: {e}")
    finally:
        print("\n--- Program finished safely! ---")


run_joke_machine()
