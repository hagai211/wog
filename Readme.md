# WorldOfGames

## Overview  
WorldOfGames is a collection of **three interactive games** designed to challenge players' skills in memory, guessing, and currency conversion. The project is built using Python and includes a **score-tracking system** hosted on a Flask web server.  

This project is containerized using **Docker**, managed with **Docker Compose**, and deployed using **Jenkins CI/CD** for automation.  

---

## 📌 Games Included  
### 1️⃣ Guess Game – `guess_game.py`  
A number guessing game where the player must guess a **randomly generated number** within a given difficulty range.  

#### 🔹 Functions:  
- **`generate_number()`** – Generates a random number between `0` and `difficulty`.  
- **`get_guess_from_user()`** – Prompts the player to enter a guess.  
- **`compare_results()`** – Compares the guessed number with the secret number.  
- **`play()`** – Runs the game and returns `True` if the player wins, `False` otherwise.  

---

### 2️⃣ Currency Roulette Game – `currency_roulette_game.py`  
A game where the player must guess the **equivalent value of a randomly generated USD amount in Israeli Shekels (ILS)**, based on real-time exchange rates.  

#### 🔹 Functions:  
- **`get_money_interval()`** – Retrieves the USD to ILS exchange rate and calculates an acceptable range based on difficulty.  
- **`get_guess_from_user()`** – Asks the player to guess the converted value.  
- **`compare_results()`** – Checks if the guessed amount is within the allowed range.  
- **`play()`** – Runs the game and returns `True` if the guess is within the correct range.  

---

### 3️⃣ Memory Game – `memory_game.py`  
A game that tests players' memory skills by displaying a sequence of numbers and asking them to recall it.  

#### 🔹 Functions:  
- **`generate_sequence()`** – Creates a sequence of random numbers based on difficulty.  
- **`get_list_from_user()`** – Captures the player's response.  
- **`is_list_equal()`** – Compares the input sequence with the generated one.  
- **`play()`** – Runs the game and returns `True` if the sequences match.  

---

## 🏆 Score Management  
### **Utils Module – `utils.py`**  
A utility module containing helper functions:  
- **`SCORES_FILE_NAME`** – The filename storing the player's total score (`Scores.txt`).  
- **`BAD_RETURN_CODE`** – A predefined error code for failed operations.  
- **`screen_cleaner()`** – Clears the console screen between games.  

### **Score System – `score.py`**  
Manages the player's accumulated score.  
- **`add_score(difficulty)`** – Updates the `Scores.txt` file with the player's new score using the formula:  
  ```  
  POINTS_OF_WINNING = (DIFFICULTY × 3) + 5  
  ```  

### **Score Server – `main_score.py`**  
A Flask-based web application that serves the current score over **HTTP**.  
- **`score_server()`** – Reads `Scores.txt` and displays it in an HTML page.  

---

## 🚀 Docker Setup  
### **Dockerfile**  
- Builds a **Flask-based score server** (`main_score.py`).  
- Runs the application in a **containerized** environment.  
- Updates the score dynamically as games are played.  

### **Docker Compose (`docker-compose.yml`)**  
- Builds the **Flask application** with the correct **port configurations**.  
- **Mounts `Scores.txt` as a volume**, ensuring persistent score updates.  

To start the project using Docker Compose:  
```sh  
docker-compose up -d --build  
```

---

## 🛠️ Jenkins CI/CD Pipeline  
A **Jenkinsfile** automates the deployment process with the following stages:  

1️⃣ **Checkout Repository** – Clones the latest code from GitHub.  
2️⃣ **Build & Run Using Docker Compose** – Builds and launches the containers.  
3️⃣ **Test the Application (`e2e.py`)** – Runs automated end-to-end tests.  
4️⃣ **Tag & Push Image to Docker Hub** – Pushes the latest image to Docker Hub.  

---

## 🔄 Continuous Deployment with GitHub & Jenkins  
To **automatically trigger Jenkins** on every push:  

1. **Enable Webhooks in GitHub**  
   - Go to your repo → **Settings** → **Webhooks** → **Add Webhook**.  
   - Set the **Payload URL**:  
     ```  
     http://your-jenkins-server/github-webhook/  
     ```  
   - Select **Just the push event** and click **Add Webhook**.  

2. **Enable Webhooks in Jenkins**  
   - Go to **Jenkins Dashboard** → Your Job → **Configure**.  
   - Under **Build Triggers**, select **GitHub hook trigger for GITScm polling**.  

---

## 🛋️ Running the Project Locally  
### **Without Docker**  
1. Clone the repository:  
   ```sh  
   git clone https://github.com/hagai211/wog.git  
   cd wog  
   ```  
2. Install dependencies:  
   ```sh  
   pip install -r requirements.txt  
   ```  
3. Run the games:  
   ```sh  
   python main.py  
   ```  
4. Start the score server:  
   ```sh  
   python main_score.py  
   ```  

### **With Docker**  
```sh  
docker-compose up -d --build  
```
Then, open a browser and go to:  
```
http://localhost:5000  
```

---

## 📝 License  
This project is open-source and available for free use.  

---

**Enjoy playing WorldOfGames!** 🚀  

