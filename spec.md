## **Boss Fight Dungeon App**

### 1. Introduction

This document outlines the design and architecture for a turn-based boss fighting dungeon application. The game will be a web-based application featuring a JavaScript frontend and a Python backend. It will incorporate AI-driven interactions through the use of Google's Agent Development Kit (ADK) and the Agent-to-Agent (A2A) communication protocol.

Players will choose from four distinct classes to battle a series of seven mini-bosses or team up with all four classes to take on an ultimate final boss. The core combat mechanic revolves around turn-based fighting, with a unique integrated quiz system to determine attack effectiveness.


### 2. System Architecture

The application will be built on a client-server model.

- **Frontend (Client-Side):**

  - **Technology:** JavaScript (React or Vue.js recommended for component-based UI).

  - **Responsibilities:**

    - Rendering all user interfaces, including menus, character and boss sprites, HP bars, and dialogs.

    - Capturing user input (selecting bosses, answering quizzes, initiating actions).

    - Communicating with the backend via RESTful API calls.

    - Displaying real-time game state updates received from the backend.

- **Backend (Server-Side):**

  - **Technology:** Python (FastAPI recommended for its asynchronous capabilities).

  - **Responsibilities:**

    - Managing the core game logic and state, including HP and turn order.

    - Serving the frontend application.

    - Hosting and managing the A2A agents.

    - Handling all API requests from the frontend.

- **Database:**

  - **Technology:** A simple database like SQLite or PostgreSQL.

  - **Responsibilities:** Storing adjustable HP values for all player classes and bosses.

- **A2A Agent Architecture:**

  - **Boss Attack Agent:** Generates creative and thematic attack dialog for the current boss.

  - **Damage & Quiz Agent:** Processes the player's agent response, calculates damage, and generates a corresponding quiz.

  - The player provides their own A2A agent endpoint for mini-boss fights.


### 3. Player Classes

Players choose from four classes. Their base HP will be adjustable in the application settings.

|                 |                                                                 |
| --------------- | --------------------------------------------------------------- |
| **Class**       | **Turn Mechanic (Mini-Boss)**                                   |
| **Shadowblade** | Gets **two** consecutive turns after the boss's initial attack. |
| **Scholar**     | Gets **two** consecutive turns after the boss's initial attack. |
| **Guardian**    | Gets a single turn after the boss attacks.                      |
| **Summoner**    | Gets a single turn after the boss attacks.                      |


### 4. Boss Design

#### 4.1. Mini-Bosses

|                     |                                                                      |                          |
| ------------------- | -------------------------------------------------------------------- | ------------------------ |
| **Mini-Boss**       | **Description**                                                      | **Weakness**             |
| **Procrastination** | A languid entity that feeds on inaction.                             | `Inescapable Reality`    |
| **Hype**            | A dazzling figure that lives on promises, not results.               | `Inescapable Reality`    |
| **Dogma**           | A rigid inquisitor that attacks any deviation from "best practices." | `Revolutionary Rewrite`  |
| **Legacy**          | A gargantuan monster built from mismatched old code.                 | `Revolutionary Rewrite`  |
| **Perfectionism**   | An angelic being that traps designers in endless refinement.         | `Elegant Sufficiency`    |
| **Obfuscation**     | A spider-like horror that spins tangled webs of convoluted code.     | `Elegant Sufficiency`    |
| **Apathy**          | A ghostly figure that drains passion and shared responsibility.      | `Unbroken Collaboration` |


#### 4.2. The Ultimate Boss

- **Name:** The Monolith of Managerial Oversight

- **Description:** A towering, multifaceted crystalline entity. It attacks with directives, scope creep, and demoralizing "synergy."

- **Weaknesses:** Possesses all four weaknesses: `Inescapable Reality`, `Revolutionary Rewrite`, `Elegant Sufficiency`, and `Unbroken Collaboration`.


### 5. Gameplay Mechanics

#### 5.1. Game Flow

1. **Main Menu:** The user chooses "Mini-Boss" or "Ultimate Boss Fight."

2. **Mini-Boss Setup:** Player selects a class, a boss, and enters their A2A agent endpoint.

3. **Ultimate Boss Setup:** A party with one of each class is automatically formed.

4. **Combat:** The fight proceeds according to the turn-based rules.


#### 5.2. Turn-Based Combat

- **Turn Initiation:** The boss always attacks first.

- **HP Management:** The backend manages all HP values.

- **Mini-Boss Turn Order:**

  - **Shadowblade/Scholar:** `Boss -> Player -> Player -> Boss...`

  - **Guardian/Summoner:** `Boss -> Player -> Boss -> Player...`

- **Ultimate Boss Turn Order:**

  - `Boss -> Shadowblade -> Scholar -> Summoner -> Shadowblade -> Guardian -> Boss -> Scholar -> Shadowblade -> Summoner -> Shadowblade -> Scholar -> Shadowblade -> (Repeat)`


#### 5.3. Agent-Driven Attack Cycle

1. **Boss Attack:**

   - The backend triggers the **Boss Attack Agent**. This agent generates a creative attack message that **must include the boss's weakness** as part of the text.

   - This complete message is sent to the player's A2A agent endpoint (for both mini and ultimate bosses). A version of the message is also displayed on the screen in a dialog bubble.

   - The player's HP is deducted by the backend, and the game state is updated on the frontend.

2. **Player Agent Response:**

   - The player's A2A agent receives the boss's attack message (containing the weakness) and returns a response message detailing its intended action.

3. **Damage & Quiz Generation:**

   - On the player's turn, the backend uses the return message from the player's agent to call the **Damage & Quiz Agent**.

   - This agent processes the player's attack message and generates a JSON object to be sent to the frontend. The structure is as follows:

     codeJson

         {
           "question": "A simple, common-sense question.",
           "answers": ["Answer 1", "Answer 2", "Answer 3"],
           "correct_index": 1,
           "damage_point": 200,
           "msg": "A cleaned-up attack message from the player's agent for display."
         }

   - The frontend will display the player's attack `msg` in a dialog bubble.

4. **Frontend Quiz & Damage Application:**

   - The frontend displays the quiz from the JSON object as a modal with multiple-choice buttons.

   - If the user answers correctly, the full `damage_point` value is sent to the backend and deducted from the boss's HP.

   - If the user answers incorrectly, half of the `damage_point` value is deducted.


### 6. UI/UX Design

- **Main Menu Screen:**

  - A clean, simple interface with two large, clickable buttons: "Enter Mini-Boss Dungeon" and "Face the Ultimate Boss."

- **Combat Screen:**

  - **Layout:** The boss is rendered on the left side of the screen. The player character (or party of four) is on the right. For the ultimate fight, the four players are arranged in a semi-circle.

  - **HP Bars:** A clear HP bar is displayed above each character and boss.

  - **Dialog Bubbles:** Attack messages from the boss appear in a speech bubble originating from the boss sprite. The player's return attack is also represented by a dialog.

  - **Quiz Interface:** When a quiz is triggered, a modal or overlay appears with the question and clickable buttons for each multiple-choice answer.

  - **Turn Indicator:** A visual cue will clearly indicate whose turn it is.


### 7. API and Data Structure Specification

#### 7.1. API Endpoints

|            |                              |                                      |
| ---------- | ---------------------------- | ------------------------------------ |
| **Method** | **Endpoint**                 | **Description**                      |
| `POST`     | `/api/miniboss/start`        | Starts a new mini-boss fight.        |
| `POST`     | `/api/ultimateboss/start`    | Starts the ultimate boss fight.      |
| `GET`      | `/api/game/{game_id}`        | Fetches the current state of a game. |
| `POST`     | `/api/game/{game_id}/action` | Submits the player's quiz answer.    |
| `GET`      | `/api/config`                | Fetches adjustable HP values.        |
| `PUT`      | `/api/config`                | Updates the adjustable HP values.    |


#### 7.2. JSON Data Structures

- **Game State Object (Backend to Frontend):**

  ```json
      {
        "game_id": "unique_game_id",
        "game_type": "mini" or "ultimate",
        "game_over": false,
        "player_won": null,
        "current_turn": "player_1",
        "boss": {
          "name": "Procrastination",
          "hp": 850,
          "max_hp": 1000
        },
        "players": [
          {
            "id": "player_1",
            "player_class": "Shadowblade",
            "hp": 450,
            "max_hp": 500,
            "a2a_endpoint": "http://localhost:8080/player-agent"
          }
        ],
        "last_boss_attack": "The boss whispered sweet nothings about tomorrow.",
        "active_quiz": {
            "question": "What is the color of the sky on a clear day?",
            "answers": ["Blue", "Green", "Red", "Yellow"],
            "correct_index": 0,
            "damage_point": 200,
            "msg": "Feel the heat! The very air ignites as the Inferno Resonance unleashes its true might! Flames surge forth, consuming all!"
        }
      }
  ```

- **Start Ultimate Boss Request (Frontend to Backend):**
  ```json
  {
    "a2a_endpoints": {
      "Shadowblade": "http://...",
      "Scholar": "http://...",
      "Guardian": "http://...",
      "Summoner": "http://..."
    }
  }
  ```

