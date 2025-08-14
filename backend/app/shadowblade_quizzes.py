shadowblade_quizzes = [
    {
      "question": "What is the primary function of the Gemini CLI's 'reason and act' (ReAct) loop?",
      "answers": [
        "To check for syntax errors in your code.",
        "To analyze user intent, select a tool, execute it, and observe the result to complete a task.",
        "To translate code from Python to another language.",
        "To format the code according to style guidelines."
      ],
      "correct_index": 1
    },
    {
      "question": "What is the purpose of the `gemini --sandbox` command?",
      "answers": [
        "To run the agent with administrative privileges.",
        "To share your session with other developers.",
        "To create a temporary, isolated container to safely test commands without affecting your main environment.",
        "To connect the Gemini CLI directly to a production server."
      ],
      "correct_index": 2
    },
    {
      "question": "In the Gemini CLI, what does the `/memory show` command do?",
      "answers": [
        "It displays the amount of RAM the CLI is using.",
        "It shows the persistent, project-level instructions loaded from files like GEMINI.md.",
        "It lists all the commands you have previously run.",
        "It provides a summary of the agent's capabilities."
      ],
      "correct_index": 1
    },
    {
      "question": "What is the role of a Model Context Protocol (MCP) server?",
      "answers": [
        "It's a database for storing agent conversations.",
        "It's a security layer that encrypts all communication.",
        "It's a specialized portal that allows the Gemini CLI to connect to and use external tools like Gitea.",
        "It's a web server for hosting the agent's user interface."
      ],
      "correct_index": 2
    },
    {
      "question": "Which file is used to configure the Gemini CLI with the locations of MCP servers?",
      "answers": [
        "~/.bashrc",
        "~/.gemini/settings.json",
        "requirements.txt",
        "Dockerfile"
      ],
      "correct_index": 1
    },
    {
      "question": "According to the workshop, what is the main purpose of creating a design document before coding?",
      "answers": [
        "To have a document to show to managers.",
        "To force clarity on goals and functions, aligning the team and preventing wasted effort.",
        "To automatically generate the entire codebase from the document.",
        "To satisfy a mandatory but unimportant process step."
      ],
      "correct_index": 1
    },
    {
      "question": "What is the special significance of the `GEMINI.md` file in a project directory?",
      "answers": [
        "It is the main documentation file for the project, like a README.",
        "The Gemini CLI automatically finds and loads its contents into the AI's working memory as persistent instructions.",
        "It contains the agent's final Python code.",
        "It stores the user's authentication credentials for Google Cloud."
      ],
      "correct_index": 1
    },
    {
      "question": "What is the primary role of the Agent Development Kit (ADK) in this workshop?",
      "answers": [
        "It is a code editor specifically for writing agents.",
        "It is a framework for building, running, and creating automated evaluation suites for agents.",
        "It is the AI model that powers the agent.",
        "It is a deployment tool for pushing agents to production."
      ],
      "correct_index": 1
    },
    {
      "question": "What is the purpose of the `sample.evalset.json` file used with the ADK?",
      "answers": [
        "It configures the agent's network settings.",
        "It defines a 'golden dataset' of test cases, each with an input and an expected outcome or tool usage.",
        "It stores the agent's conversation history.",
        "It lists the Python packages the agent depends on."
      ],
      "correct_index": 1
    },
    {
      "question": "In the ADK's `test_config.json`, what does the `tool_trajectory_avg_score` evaluate?",
      "answers": [
        "The semantic similarity of the agent's final text response.",
        "How quickly the agent responds.",
        "How well the agent's sequence of tool usage matches the expected sequence.",
        "The total number of tools the agent used."
      ],
      "correct_index": 2
    },
    {
      "question": "What is the main benefit of using `pytest` to run agent evaluations?",
      "answers": [
        "It provides a web interface for watching the tests run.",
        "It allows evaluation logic to be written in code, which is essential for automation in a CI/CD pipeline.",
        "It is the only way to test an agent's visual output.",
        "It automatically fixes any errors found in the agent's code."
      ],
      "correct_index": 1
    },
    {
      "question": "What Google Cloud service is used to define and execute the automated Continuous Integration (CI) pipeline?",
      "answers": [
        "Cloud Run",
        "Cloud Storage",
        "Artifact Registry",
        "Cloud Build"
      ],
      "correct_index": 3
    },
    {
      "question": "What is the purpose of the `cloudbuild.yaml` file?",
      "answers": [
        "It contains the agent's core Python logic.",
        "It defines the steps for the automated CI pipeline, such as running tests and building a container.",
        "It lists the permissions the agent needs to run.",
        "It's a design document that outlines the agent's architecture."
      ],
      "correct_index": 1
    },
    {
      "question": "In the CI pipeline, what is the purpose of the 'Run Pytest Ward' step?",
      "answers": [
        "To install the agent's dependencies.",
        "To push the agent's container image to the registry.",
        "To automatically run the evaluation tests to ensure the code changes haven't introduced regressions.",
        "To deploy the agent to Cloud Run."
      ],
      "correct_index": 2
    },
    {
      "question": "What is the final output of a successful Cloud Build run in this workshop?",
      "answers": [
        "A detailed report on the agent's performance.",
        "A deployed and running agent on Cloud Run.",
        "A container image of the agent stored in Artifact Registry.",
        "A new Git repository with the agent's code."
      ],
      "correct_index": 2
    },
    {
      "question": "What does the concept of 'synthetic data generation' refer to in the workshop?",
      "answers": [
        "Using real user data to test the agent.",
        "Creating fake user profiles for the agent to interact with.",
        "Commanding an AI to create new, realistic test cases from a template to scale up testing.",
        "Generating code automatically from a design document."
      ],
      "correct_index": 2
    },
    {
      "question": "What is the purpose of using type hints in the Python code, as per the coding guidelines?",
      "answers": [
        "To add comments to the code.",
        "To make the code run faster.",
        "To specify the expected data type for variables and function returns, improving clarity and catching errors.",
        "To automatically generate documentation."
      ],
      "correct_index": 2
    }
]
