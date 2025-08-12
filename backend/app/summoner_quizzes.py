summoner_quizzes = [
         {
            "question": "In the workshop, why are the tools (like the 'Elemental Fonts') built as separate services?",
            "answers": [
                "To make the project more complicated.",
                "So you can update a tool without having to change the main agent.",
                "To make sure all tools are in the same programming language.",
                "To stop the agents from using any tools."
            ],
            "correct_index": 1
        },
        {
            "question": "Which type of agent is used to make sure tasks happen one after another, in a specific order?",
            "answers": [
                "ParallelAgent (for doing things at the same time)",
                "LoopAgent (for repeating things)",
                "SequentialAgent (for doing things in a sequence or order)",
                "LlmAgent (the basic brain agent)"
            ],
            "correct_index": 2
        },
        {
            "question": "How does the main 'Summoner' agent learn what the 'Familiar' agents can do?",
            "answers": [
                "By guessing their abilities.",
                "By reading their public 'Agent Card', which lists their skills.",
                "By having their code built-in from the start.",
                "By asking the user what they do."
            ],
            "correct_index": 1
        },
        {
            "question": "What's the main difference between a 'Callback' and a 'Plugin' for adding rules like a cooldown?",
            "answers": [
                "A Callback is for just one agent, while a Plugin can be used for many agents at once.",
                "Plugins are simple, Callbacks are complicated.",
                "Callbacks are for making agents faster, Plugins are for making them slower.",
                "There is no difference."
            ],
            "correct_index": 0
        },
        {
            "question": "When the Summoner remembers which Familiar it just used so it doesn't use it again right away, what kind of memory is this?",
            "answers": [
                "Long-Term Memory (remembering things forever)",
                "No Memory (forgetting everything instantly)",
                "Short-Term Memory (remembering things for just the current conversation)",
                "Database Memory (storing it in the Librarium)"
            ],
            "correct_index": 2
        },
        {
            "question": "The workshop uses a `tools.yaml` file to create the database tools. Why is this a good approach?",
            "answers": [
                "Because it requires writing more Python code.",
                "It's an easy way to define database tools without writing a lot of custom server code.",
                "It's the only way to connect to a database.",
                "It makes the tools run slower but more securely."
            ],
            "correct_index": 1
        },
        {
            "question": "Which agent is best for a task that needs to be repeated several times, like charging up an attack?",
            "answers": [
                "The SequentialAgent",
                "The ParallelAgent",
                "The LoopAgent",
                "The SummonerAgent"
            ],
            "correct_index": 2
        },
        {
            "question": "What does a 'before_agent_callback' allow you to do?",
            "answers": [
                "Run some code *after* the agent finishes its job.",
                "Run a check or rule *before* the agent starts its main job.",
                "Change the agent's name.",
                "Delete the agent permanently."
            ],
            "correct_index": 1
        },
        {
            "question": "How does the workshop keep the database password in `tools.yaml` safe when deploying?",
            "answers": [
                "By writing it directly in the code.",
                "By emailing it to the developer.",
                "By loading it from a secure service called Google Secret Manager.",
                "By asking the user to type it in every time."
            ],
            "correct_index": 2
        },
        {
            "question": "What is the main job of the `RemoteA2aAgent`?",
            "answers": [
                "To perform a powerful attack.",
                "To act as a 'remote control' for a Familiar that is running on a different server.",
                "To store the agent's memory.",
                "To design the agent's user interface."
            ],
            "correct_index": 1
        },
        {
            "question": "The Water Elemental attacks with multiple spells at once and then combines the damage. What is this pattern called?",
            "answers": [
                "A sequential pattern.",
                "A loop pattern.",
                "A 'fan-out, fan-in' pattern (spread out, then come back together).",
                "A failure pattern."
            ],
            "correct_index": 2
        },
        {
            "question": "How does the code save the name of the last used Familiar into short-term memory?",
            "answers": [
                "By writing it to a file.",
                "By using `tool_context.state['last_summon']`.",
                "By printing it to the screen.",
                "By calling another agent."
            ],
            "correct_index": 1
        },
        {
            "question": "What is the purpose of using Cloud Build in the workshop?",
            "answers": [
                "To write the Python code for the agents.",
                "To provide an automated way to build and deploy the agents to the cloud.",
                "To test the agents on your local computer.",
                "To design the agent's personality."
            ],
            "correct_index": 1
        },
        {
            "question": "What does `max_iterations=2` mean for the Earth Elemental's LoopAgent?",
            "answers": [
                "The attack will be twice as powerful.",
                "The agent will wait for 2 seconds before starting.",
                "The charging loop will run a maximum of two times.",
                "The agent can only be used twice in total."
            ],
            "correct_index": 2
        },
        {
            "question": "What is the main role of the 'Summoner' agent in the system?",
            "answers": [
                "To perform all the attacks itself.",
                "To look at a problem and choose the best 'Familiar' to handle it.",
                "To store all the data in its database.",
                "To provide a chat window for the user."
            ],
            "correct_index": 1
        },
        {
            "question": "What is the `adk web` command used for?",
            "answers": [
                "To deploy the agent to the internet.",
                "To start a local test server with a user interface in your browser.",
                "To check the agent's code for errors.",
                "To download the agent from the web."
            ],
            "correct_index": 1
        },
        {
            "question": "What is the purpose of the `statement` field in the database tool's `tools.yaml` file?",
            "answers": [
                "A friendly description of the tool.",
                "The username for the database.",
                "The actual SQL command that the tool will run.",
                "The name of the tool."
            ],
            "correct_index": 2
        },
        {
            "question": "What is the main purpose of the `instruction` you give to an agent?",
            "answers": [
                "To tell it which server to run on.",
                "To give it a name.",
                "To tell it what its job is, how to behave, and what rules to follow.",
                "To set its password."
            ],
            "correct_index": 2
        },
        {
            "question": "Why is it a good idea to keep the agent's logic (the 'Familiars') separate from the tools they use (the 'Fonts')?",
            "answers": [
                "It's not a good idea.",
                "So you can change the agent's strategy without having to rewrite the underlying tool.",
                "To make sure all the code is in one giant file.",
                "Because tools are less important than agents."
            ],
            "correct_index": 1
        },
        {
            "question": "What is the main problem that the Agent-to-Agent (A2A) protocol solves?",
            "answers": [
                "It helps agents work alone.",
                "It provides a standard way for different agents to talk to each other and work as a team.",
                "It is a programming language.",
                "It is a type of database."
            ],
            "correct_index": 1
        },
        {
            "question": "What's the main difference between Short-Term and Long-Term memory for an agent?",
            "answers": [
                "There is no difference.",
                "Short-term is for the current chat only, while long-term is for remembering things forever.",
                "Short-term memory is faster, but long-term memory is smarter.",
                "Only Summoners have long-term memory."
            ],
            "correct_index": 1
        },
        {
            "question": "What Cloud service is used to run the deployed agents as scalable, serverless services?",
            "answers": [
                "Google Cloud Storage",
                "Cloud SQL",
                "Cloud Run",
                "Google Drive"
            ],
            "correct_index": 2
        }
]
