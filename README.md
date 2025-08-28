# AgentVerse Dungeon

AgentVerse Dungeon is a web-based, single-player RPG where a player or a party of players fights against a boss. The core gameplay loop revolves around a turn-based combat system. Player actions are not chosen from a static list of abilities but are generated dynamically by answering class-specific quizzes. The narrative and flavor text for attacks and events are enhanced by a generative AI agent system, creating a unique experience in each playthrough.

## Getting Started

### Prerequisites

- Node.js and npm
- Python 3.12+ and pip

### Installation and Running

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd agentverse-dungeon
    ```

2.  **Install frontend dependencies:**
    ```bash
    cd frontend
    npm install
    cd ..
    ```

3.  **Install backend dependencies:**
    ```bash
    pip install -r backend/requirements.txt
    ```

4.  **Start the application:**
    ```bash
    ./start.sh
    ```
    This will start the backend server on port 8000 and serve the frontend.

## Project Structure

```
/home/user/agentverse-dungeon/
├───.dockerignore
├───.gcloudignore
├───.gitignore
├───balance.md
├───cloudbuild.yaml
├───designdoc.md
├───Dockerfile
├───init.sh
├───package-lock.json
├───package.json
├───run_cloudbuild.sh
├───runonce.sh
├───set_env.sh
├───spec.md
├───start.sh
├───.git/...
├───.idx/
│   ├───dev.nix
│   └───integrations.json
├───backend/
│   ├───requirements.txt
│   └───app/
│       ├───api.py
│       ├───crud.py
│       ├───guardian_quizzes.py
│       ├───main.py
│       ├───models.py
│       ├───scholar_quizzes.py
│       ├───shadowblade_quizzes.py
│       ├───single_agent_old.py
│       ├───single_agent.py
│       ├───summoner_quizzes.py
│       └───__pycache__/
└───frontend/
    ├───package-lock.json
    ├───package.json
    ├───public/
    │   ├───index.html
    │   ├───manifest.json
    │   └───assets/
    │       └───images/
    └───src/
        ├───App.js
        ├───index.js
        ├───styles.css
        ├───components/
        ├───contexts/
        └───pages/
```

### Key Files

-   **`Dockerfile`**: Defines the container for deploying the application. It builds the frontend and sets up the Python environment for the backend.
-   **`cloudbuild.yaml`**: Configuration for Google Cloud Build to automate the deployment of the application to Google Cloud Run.
-   **`designdoc.md`**: The design document for the project, outlining the architecture, features, and implementation details.
-   **`spec.md`**: The project specification, detailing the gameplay mechanics, character classes, bosses, and API structure.
-   **`start.sh`**: A script to start the application locally.
-   **`backend/`**: Contains the Python FastAPI backend.
    -   **`app/api.py`**: Defines the main API endpoints for the game.
    -   **`app/crud.py`**: Handles the game's data and logic.
    -   **`app/models.py`**: Contains the Pydantic models for the application's data structures.
    -   **`app/single_agent.py`**: Manages the integration with the AI agent system.
-   **`frontend/`**: Contains the React frontend.
    -   **`src/App.js`**: The main component of the application, which handles routing and state management.
    -   **`src/components/`**: Contains reusable React components.
    -   **`src/pages/`**: Contains the main pages of the application.

## Build and Deployment

This project is configured for automated deployment to Google Cloud Run using Google Cloud Build. The `cloudbuild.yaml` file defines the build and deployment steps. To deploy the application, you can run the `run_cloudbuild.sh` script, which will trigger a Cloud Build job.

The `Dockerfile` is used to create a container image for the application. It first builds the frontend and then copies the build artifacts and the backend code into a Python-based image.
