guardian_quizzes = [
    {
        "question": "In the workshop, what is the primary Google Cloud service used for building automated CI/CD pipelines?",
        "answers": ["Cloud Functions", "Cloud Build", "Cloud Composer", "Jenkins"],
        "correct_index": 1
    },
    {
        "question": "Which serverless compute platform is used to deploy the containerized LLM services (Ollama and vLLM)?",
        "answers": ["App Engine", "Google Kubernetes Engine", "Cloud Run", "Compute Engine"],
        "correct_index": 2
    },
    {
        "question": "What is the key advantage of the vLLM deployment strategy over the Ollama strategy as shown in the lab?",
        "answers": ["Faster cold start time", "Easier for beginners", "Flexibility to update the model without rebuilding the container", "Lower memory usage"],
        "correct_index": 2
    },
    {
        "question": "What service is used to create a secure, unified gateway with a single IP for both LLM services?",
        "answers": ["Cloud Armor", "Cloud NAT", "Regional External Application Load Balancer", "Cloud VPN"],
        "correct_index": 2
    },
    {
        "question": "What technology is used to inspect traffic for malicious prompts, PII, and jailbreak attempts? [3]",
        "answers": ["Cloud IDS", "VPC Flow Logs", "Model Armor", "Identity-Aware Proxy"],
        "correct_index": 2
    },
    {
        "question": "How does the vLLM service on Cloud Run access the model files stored in a Cloud Storage bucket?",
        "answers": ["It downloads them via a public URL", "It uses the Cloud Storage API in the code", "It mounts the bucket as a local folder using Cloud Storage FUSE", "The model is baked into the container"],
        "correct_index": 2
    },
    {
        "question": "In the Ollama deployment, where are the LLM model weights stored?",
        "answers": ["In a Cloud Storage bucket", "On a persistent disk", "Baked directly into the container image", "In Secret Manager"],
        "correct_index": 2
    },
    {
        "question": "What is the function of a Serverless Network Endpoint Group (NEG) in this architecture? [2]",
        "answers": ["To store container images", "To connect a Load Balancer to serverless backends like Cloud Run", "To manage user permissions", "To monitor GPU performance"],
        "correct_index": 1
    },
    {
        "question": "What is attached to the vLLM service as a sidecar container to scrape detailed performance metrics? [4]",
        "answers": ["Fluentd", "Prometheus exporter", "Cloud Logging agent", "OpenTelemetry Collector"],
        "correct_index": 1
    },
    {
        "question": "Which tool allows you to view the complete journey of a single request through the agent to diagnose latency? [1]",
        "answers": ["Metrics Explorer", "Cloud Profiler", "Cloud Trace", "Cloud Logging"],
        "correct_index": 2
    },
    {
        "question": "Where is the Hugging Face access token stored securely to be used by Cloud Build?",
        "answers": ["In the Dockerfile", "In an environment variable in cloudbuild.yaml", "In Secret Manager", "In a Cloud Storage file"],
        "correct_index": 2
    },
    {
        "question": "What open-source framework is mentioned for building the Guardian Agent?",
        "answers": ["LangChain", "Hugging Face Transformers", "Google's Agent Development Kit (ADK)", "TensorFlow"],
        "correct_index": 2
    },
    {
        "question": "What is the configuration file format that defines the steps for a Cloud Build pipeline?",
        "answers": ["JSON", "XML", "YAML", "Python script"],
        "correct_index": 2
    },
    {
        "question": "What is the purpose of enabling Private Google Access for the VPC subnet in the vLLM deployment?",
        "answers": ["To give the service a public IP address", "To allow Cloud Run to reach Google APIs (like Cloud Storage) without using the public internet", "To block all incoming traffic", "To enable SSH access to the container"],
        "correct_index": 1
    },
    {
        "question": "What component is essential for connecting the Load Balancer to Model Armor to inspect traffic? [3, 7]",
        "answers": ["A firewall rule", "A Service Extension", "A VPC Peering connection", "A Cloud DNS record"],
        "correct_index": 1
    },
    {
        "question": "What is a primary downside of the vLLM deployment strategy (mounting from GCS) mentioned in the workshop?",
        "answers": ["It is less secure", "It cannot be automated", "It has a longer initial 'cold-start' time", "It does not support GPUs"],
        "correct_index": 2
    },
    {
        "question": "The vLLM service is specifically engineered to maximize what in a production environment? [9]",
        "answers": ["Model fine-tuning speed", "LLM serving throughput and efficiency", "Ease of local development", "Cross-cloud compatibility"],
        "correct_index": 1
    },
    {
        "question": "What is the purpose of the 'A2A Inspector' tool used in the workshop?",
        "answers": ["To scan source code for vulnerabilities", "To interact with and debug deployed agents via a web UI", "To inspect network packets", "To analyze GPU memory usage"],
        "correct_index": 1
    },
    {
        "question": "What does the `adk run` command do?",
        "answers": ["Deploys the agent to Cloud Run", "Runs the agent server locally for testing", "Builds the agent's Docker container", "Runs a performance test on the agent"],
        "correct_index": 1
    },
    {
        "question": "What is the core technology behind vLLM's efficient memory management, as mentioned in the text?",
        "answers": ["Model sharding", "PagedAttention", "Quantization", "Knowledge distillation"],
        "correct_index": 1
    }
]
