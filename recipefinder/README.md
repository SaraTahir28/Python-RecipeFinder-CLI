**🥕 Recipe Finder CLI (Python)**
A simple, interactive command‑line application that lets users search for recipes by ingredient and diet type using the Edamam Recipes API (v2).
Users can view results, save favourites, and manage stored recipes — all from the terminal.

**📌 Features**
🔍 Search recipes by ingredient and diet (balanced, high‑protein, low‑fat, etc.)

📄 Save recent search results to recipes.txt

⭐ Mark favourite recipes and store them in favorites.txt

📂 View saved recipes directly from the CLI

🧹 Clear stored files when needed

🔐 Uses a .env file to securely load API credentials

🌐 Fully integrated with Edamam Recipes API v2 (with required headers)

**🛠️ Tech Stack**
Python 3

requests — API calls

python-dotenv — environment variable loading

Edamam Recipes API v2

**📦 Installation & Setup**
1. Clone the repository
cd recipefinder
2. Create and activate a virtual environment
bash
python3 -m venv venv
source venv/bin/activate
3. Install dependencies
bash
pip install requests python-dotenv
4. Create a .env file in the project root
Code
APP_ID=your_edamam_app_id
APP_KEY=your_edamam_app_key
APP_USER=your_edamam_account_user

**▶️ Running the Application**
In your terminal run
python3 main.py
You’ll see:

Code
Welcome to Recipe Finder
1. Search for a new recipe
2. View recent search results
3. View favorites
4. Clear saved recipes
5. Exit
🔍 How Searching Works
When you choose Search, the app will:

Ask for an ingredient

Ask for a diet type

Query the Edamam API

Display recipe names + URLs

Save results to recipes.txt

Allow you to mark favourites

**Runtime Files (Not Included in Repo)**

The application generates two text files during use:

- `recipes.txt` — stores the most recent search results  
- `favorites.txt` — stores recipes marked as favourites  

These files are created automatically when the program runs and are intentionally **not included** in the repository.
🧹 Clearing Saved Data
Choose option 4 in the menu to clear either:

recipes.txt

favorites.txt

🧪 Example API Call (Python)
The app uses:

python
url = "https://api.edamam.com/api/recipes/v2"
params = {
    "type": "public",
    "q": ingredient,
    "app_id": app_id,
    "app_key": app_key,
    "diet": diet
}
headers = {
    "Edamam-Account-User": app_user,
    "Accept": "application/json"
}
This matches the Edamam v2 requirements.

🚀 Future Improvements
Pagination support (Edamam “next page” links)

Better error handling and validation

Colourful terminal UI

Export favourites to JSON or CSV

Optional local caching
