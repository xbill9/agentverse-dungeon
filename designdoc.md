# Design Document: AgentVerse Dungeon

## 1. Overview

AgentVerse Dungeon is a web-based, single-player RPG where a player or a party of players fights against a boss. The core gameplay loop revolves around a turn-based combat system. Player actions are not chosen from a static list of abilities but are generated dynamically by answering class-specific quizzes. The narrative and flavor text for attacks and events are enhanced by a generative AI agent system, creating a unique experience in each playthrough.

The project is split into two main parts: a React-based frontend for the user interface and a Python FastAPI backend that manages game logic and AI agent integration.

## 2. Architecture

The application follows a classic client-server architecture.

*   **Frontend**: A React Single-Page Application (SPA) that provides the user interface. It is responsible for rendering the game state, capturing user input (character selection, quiz answers), and communicating with the backend.
*   **Backend**: A Python server using the FastAPI framework. It exposes a RESTful API that the frontend consumes. Its responsibilities include:
    *   Managing the game lifecycle (starting, progressing, ending).
    *   Handling all game logic (turn order, damage calculation, state changes).
    *   Storing game state in memory.
    *   Integrating with the AI agent system to generate dynamic content.
*   **AI Agent System**: Built using the `google-adk` library. This system is called by the backend to generate player actions and narrative text, which are then used to create quizzes for the player.

## 3. Frontend Design

The frontend is built with React and uses several libraries for its core functionality:

*   `react-router-dom` for navigation between different screens (main menu, combat, etc.).
*   `axios` for making HTTP requests to the backend API.
*   `react-draggable` to allow the user to move the quiz modal.

### 3.1. Component Structure

The UI is broken down into reusable components located in `src/components/`:

*   **`App.js`**: The root component that manages routing and top-level game state.
*   **`HomePage.js`**: The main menu screen where players choose the game mode.
*   **`MiniBossPage.js` & `UltimateBossPage.js`**: Screens for setting up the parameters for a new game (selecting player class, boss, and A2A endpoints).
*   **`PreCombatScreen.js`**: A screen that displays the player and boss before the fight begins.
*   **`CombatScreen.js`**: The main screen for the fight. It orchestrates the display of characters, the quiz modal, and status messages. It handles the core combat flow on the client-side, polling the backend for state updates.
*   **`Player.js` & `Boss.js`**: Components to display the player and boss characters, including their HP bars and current status.
*   **`QuizModal.js`**: A draggable modal that displays the current question and answer choices for the player.
*   **`HpBar.js`, `DialogBubble.js`, `DamageIndicator.js`**: Smaller, reusable components for displaying character health, dialogue, and damage taken.

### 3.2. State Management

*   **Component State (`useState`)**: Most of the game state is managed within the `App.js` and `CombatScreen.js` components. This includes the main `gameState` object, error messages, and UI-specific state like whether to show the quiz modal.
*   **Context API (`useBackground`)**: A `BackgroundContext` is used to manage the background image of the application globally, allowing any component to change it.

### 3.3. Routing

The application uses `react-router-dom` to define the following routes:

*   `/`: The home page/main menu.
*   `/mini-boss`: The setup page for a mini-boss battle.
*   `/ultimate-boss`: The setup page for the ultimate boss battle.
*   `/pre-combat`: The pre-fight summary screen.
*   `/combat`: The main combat screen.

## 4. Backend Design

The backend is a FastAPI application that serves the game logic via a REST API.

### 4.1. API Endpoints

The API is defined in `app/api.py`:

*   `POST /api/miniboss/start`: Creates a new mini-boss game.
*   `POST /api/ultimateboss/start`: Creates a new ultimate boss game.
*   `GET /api/game/{game_id}`: Retrieves the current state of a game. This endpoint also triggers the boss's turn if it is the boss's turn to act.
*   `POST /api/game/{game_id}/action`: Submits a player's action (an answer to a quiz).
*   `GET /api/config`: Retrieves the current game configuration (HP values).
*   `PUT /api/config`: Updates the game configuration.

### 4.2. Game Logic

*   **Turn-Based System**: The game progresses in turns, with the order defined in a `turn_order` list in the `GameState` model. The `advance_turn` function cycles through this list.
*   **Action Handling**: When a player submits a quiz answer via the `/action` endpoint, the backend calculates the damage based on the correctness of the answer, updates the boss's HP, and checks for game-over conditions.
*   **Boss AI**: When it is the boss's turn, the `process_turn` function is called. It generates a narrative attack message, calculates damage to players, updates their HP, and checks for game-over conditions.
*   **Persistence**: Game state is stored in a simple in-memory dictionary (`game_db` in `app/crud.py`). This means all game progress is lost when the server restarts.

### 4.3. Data Models

Pydantic models in `app/models.py` are used to define the structure of the data:

*   **`GameState`**: The main model that encapsulates the entire state of a single game.
*   **`Player`**, **`Boss`**: Models for the characters in the game.
*   **`Quiz`**: Defines the structure of a quiz question.
*   **Request/Response Models**: `StartMiniBossRequest`, `ActionRequest`, etc., define the expected JSON bodies for API requests.

### 4.4. AI Agent Integration

A key feature is the use of `google-adk` to generate dynamic content. This is handled in `app/single_agent.py`.

*   **`create_heroic_action_agent`**: This function constructs a `SequentialAgent`.
    1.  It first calls a **`RemoteA2aAgent`** (`player_agent`). This is an external agent (specified by the `a2a_endpoint` from the frontend) that returns a narrative description of a heroic action.
    2.  The output of the remote agent is then fed into a local **`LlmAgent`** (`HeroicScribeAgent`), which uses `gemini-1.5-flash`. This agent's role is to parse the narrative text and convert it into a structured JSON object containing a `damage_point` and a `message`.
*   **`process_player_action`**: This function executes the agent chain using an `InMemoryRunner` and returns the parsed JSON data.
*   **Quiz Generation**: The structured data from the agent is then used by `mock_damage_quiz_agent` in `crud.py` to select a relevant quiz from the class-specific quiz files (`shadowblade_quizzes.py`, etc.) and associate the agent-generated damage with it.

## 5. Coding Rules and Conventions

### 5.1. General

*   **Separation of Concerns**: Maintain a strict separation between the frontend and backend codebases.
*   **API Contract**: All communication between frontend and backend must be done via the defined REST API, using JSON as the data format.
*   **Configuration**: Game balance values (HP, etc.) are stored in a central `Config` object in the backend to allow for easy tuning.

### 5.2. Backend (Python)

*   **Framework**: Use FastAPI for all web server and API functionality.
*   **Data Validation**: Use Pydantic models for all API request and response bodies to ensure type safety and data validation.
*   **Asynchronous Code**: Use `async` and `await` for all I/O-bound operations, especially for API endpoints and agent calls.
*   **Naming**:
    *   Variables and function names should be `snake_case`.
    *   Class names should be `PascalCase`.
*   **Modularity**: Keep logic separated into distinct files (e.g., `api.py` for routes, `crud.py` for data access, `models.py` for data structures).
*   **Type Hinting**: Use Python type hints for all function signatures and variable declarations to improve code clarity and allow for static analysis.

### 5.3. Frontend (React)

*   **Component-Based Architecture**: Build the UI from small, reusable functional components.
*   **Hooks**: Use React Hooks (`useState`, `useEffect`, `useContext`) for state and side effects. Avoid class components.
*   **Naming**:
    *   Component files and functions should be `PascalCase` (e.g., `CombatScreen.js`).
    *   Non-component functions and variables should be `camelCase`.
*   **File Structure**: Organize files logically into `components/`, `pages/`, and `contexts/` directories.
*   **Styling**: Use standard CSS in a single `styles.css` file. Use meaningful class names to avoid conflicts.
*   **HTTP Requests**: Use `axios` for all API calls to the backend. Centralize API URLs and configurations where possible.
