scholar_quizzes = [
    {
      "question": "What is the primary goal of a Retrieval-Augmented Generation (RAG) system?",
      "answers": [
        "To replace the need for a database entirely.",
        "To ground a Large Language Model's responses in factual, up-to-date information, reducing hallucinations.",
        "To train a Large Language Model from scratch on new data.",
        "To translate text from one language to another."
      ],
      "correct_index": 1
    },
    {
      "question": "In the workshop, what is the main purpose of using a BigQuery External Table?",
      "answers": [
        "To permanently move data from Cloud Storage into BigQuery.",
        "To create a machine learning model directly on raw files.",
        "To query raw text files directly in Google Cloud Storage without ingesting them, saving costs and time.",
        "To encrypt the data stored in Google Cloud Storage."
      ],
      "correct_index": 2
    },
    {
      "question": "Which BigQuery ML function is used to transform unstructured text into structured JSON by calling a Gemini model?",
      "answers": [
        "ML.PREDICT",
        "ML.TRANSFORM",
        "ML.GENERATE_TEXT",
        "ML.CREATE_MODEL"
      ],
      "correct_index": 2
    },
    {
      "question": "What is the role of the pgvector extension in Cloud SQL for PostgreSQL?",
      "answers": [
        "It automatically creates backups of the database.",
        "It enables the database to store and query high-dimensional vector embeddings for semantic search.",
        "It improves the performance of standard text-based searches.",
        "It provides a direct connection to BigQuery."
      ],
      "correct_index": 1
    },
    {
      "question": "What is the main advantage of using Dataflow for the vectorization pipeline over a simple Python script?",
      "answers": [
        "It's easier to write for a single file.",
        "It provides a managed, serverless platform for scalable and parallel processing of large numbers of files.",
        "It runs the pipeline locally on your personal computer.",
        "It automatically visualizes the data in a dashboard."
      ],
      "correct_index": 1
    },
    {
      "question": "What is the final role of Cloud Run in the workshop's architecture?",
      "answers": [
        "To store the raw data files.",
        "To train the Gemini machine learning model.",
        "To run the batch Dataflow pipeline.",
        "To deploy the final RAG agent as a scalable and secure web service."
      ],
      "correct_index": 3
    },
    {
      "question": "Why is it important for the vector in the PostgreSQL table (e.g., VECTOR(768)) to have the same dimension as the embedding model's output?",
      "answers": [
        "Higher dimensions always mean better performance.",
        "The dimensions must match for the database to correctly store the data and for similarity calculations to be valid.",
        "It is a user preference and does not affect functionality.",
        "It reduces the storage cost of the vectors."
      ],
      "correct_index": 1
    },
    {
      "question": "What does the cosine similarity operator (<=>) in pgvector measure?",
      "answers": [
        "The number of matching keywords between two texts.",
        "The geographical distance between two coordinates.",
        "The similarity between two vectors based on the angle between them, indicating semantic closeness.",
        "The time it takes to retrieve a record from the database."
      ],
      "correct_index": 2
    },
    {
      "question": "What is the purpose of creating an 'ivfflat' index on a vector column in Cloud SQL?",
      "answers": [
        "To guarantee 100% accuracy on all queries.",
        "To make the data read-only.",
        "To dramatically speed up vector similarity searches by pre-organizing vectors into clusters.",
        "To compress the vectors and save storage space."
      ],
      "correct_index": 2
    },
    {
      "question": "In the RAG process, what happens during the 'Retrieve' step?",
      "answers": [
        "The Large Language Model generates a final answer.",
        "The user's query is converted to a vector and used to find the most similar documents in the database.",
        "The database tables are created for the first time.",
        "The agent is deployed to Cloud Run."
      ],
      "correct_index": 1
    },
    {
      "question": "What is the 'Augment' step in a Retrieval-Augmented Generation (RAG) agent?",
      "answers": [
        "The agent asks the user for more information.",
        "The system's performance is upgraded with more memory.",
        "The relevant text retrieved from the database is added to the prompt for the Large Language Model.",
        "The database is populated with more documents."
      ],
      "correct_index": 2
    },
    {
      "question": "Why does the workshop use a custom container image for the Dataflow workers?",
      "answers": [
        "It is the only way to run a Dataflow job.",
        "To pre-install all necessary libraries, which reduces worker start-up time and ensures a consistent environment.",
        "To give the Dataflow workers a unique name.",
        "To limit the amount of memory the workers can use."
      ],
      "correct_index": 1
    },
    {
      "question": "What is the role of Apache Beam in the workshop?",
      "answers": [
        "It's a web server for hosting the agent.",
        "It's a specific type of database.",
        "It's a model for defining the logical steps of a data processing pipeline (Read, Embed, Write) that can be run on Dataflow.",
        "It's the AI model that generates text."
      ],
      "correct_index": 3
    },
    {
      "question": "In BigQuery, what does the `SAFE.PARSE_JSON` function help accomplish?",
      "answers": [
        "It validates that a JSON string is secure.",
        "It safely converts a JSON string into a structured JSON object, preventing errors if the string is malformed.",
        "It extracts a single value from a JSON object.",
        "It connects to an external JSON database."
      ],
      "correct_index": 1
    },
    {
      "question": "What does the `task_type=\"RETRIEVAL_DOCUMENT\"` parameter do when creating embeddings?",
      "answers": [
        "It tells the model that the text is from a legal document.",
        "It optimizes the generated vector embedding specifically for being found later in a search query.",
        "It makes the embedding smaller in size.",
        "It specifies that the model should retrieve a document from the internet."
      ],
      "correct_index": 1
    },
    {
      "question": "What is the primary function of a Dataflow pipeline in this workshop?",
      "answers": [
        "To serve the RAG agent's API requests in real-time.",
        "To perform a batch process of reading text files, creating vector embeddings, and writing them to a database.",
        "To create the initial unstructured text files in Cloud Storage.",
        "To monitor the health of the Cloud Run agent."
      ],
      "correct_index": 1
    },
    {
      "question": "Which of these is a key benefit of the ELT (Extract, Load, Transform) pattern used in the BigQuery section?",
      "answers": [
        "The transformation logic is always written in Python.",
        "It requires moving the data out of the data warehouse for transformation.",
        "It performs complex, AI-powered transformations directly inside the data warehouse using SQL.",
        "It is an older, less efficient method than ETL."
      ],
      "correct_index": 2
    },
    {
      "question": "What is Cloud Build used for in this workshop?",
      "answers": [
        "To run the final RAG agent.",
        "To create the PostgreSQL database.",
        "To forge a custom container image pre-loaded with all necessary libraries for Dataflow and Cloud Run.",
        "To write the Python code for the pipeline."
      ],
      "correct_index": 2
    },
    {
      "question": "How is the RAG agent's database query different from a standard keyword search?",
      "answers": [
        "It searches for exact keyword matches in the text.",
        "It uses vector embeddings to search for semantic meaning and context, not just keywords.",
        "It can only search for numbers, not text.",
        "It is significantly slower than a keyword search."
      ],
      "correct_index": 1
    },
    {
      "question": "What is the purpose of creating a 'CONNECTION' resource in BigQuery?",
      "answers": [
        "To connect your local computer to BigQuery.",
        "To establish a secure link between BigQuery and an external resource like Cloud Storage or Vertex AI.",
        "To connect two BigQuery tables together in a query.",
        "To set the billing account for the project."
      ],
      "correct_index": 1
    }
]
