PROFILE = {
    "name": "Gauransh Sharma",
    "tagline": "Full-stack engineer specializing in LLM orchestration, RAG pipelines, and agentic workflows.",
    "summary": "Full-stack engineer with hands-on experience shipping production AI systems, cross-platform mobile apps, and scalable backend services. Specialized in LLM orchestration, RAG pipelines, and agentic workflows — with a track record of owning features end-to-end across Flutter, FastAPI, and AWS. Comfortable operating at the intersection of AI research and product engineering.",
    "location": "India",
    "website": "https://gauranshsharma.com",
    "email": "gauransh@gauranshsharma.com",
    "github": "https://github.com/gauransh18",
    "linkedin": "https://linkedin.com/in/gauransh18",
    "twitter": "https://x.com/gauransh18_",
}

AVAILABILITY = {
    "open_to_work": True,
    "message": "Open to full-time roles and contracts in AI/ML product engineering, backend systems, and cross-platform mobile. Reach out at gauransh@gauranshsharma.com.",
}

SKILLS = [
    {"category": "Languages",      "skills": ["Python", "Go", "SQL", "JavaScript", "Dart", "Swift", "C++"]},
    {"category": "Mobile",         "skills": ["Flutter", "React Native", "Cross-Platform Architecture", "Background Sync", "State Management", "Animations"]},
    {"category": "AI & Data",      "skills": ["LangChain", "LangGraph", "DSPy", "RAG", "Pinecone", "ChromaDB", "Mem0", "AWS Bedrock", "Llama-3", "LLM Orchestration"]},
    {"category": "Backend & Infra","skills": ["FastAPI", "Flask", "PostgreSQL", "Supabase", "Firebase", "REST APIs", "Microservices", "Auth", "Rate Limiting"]},
    {"category": "DevOps & Tools", "skills": ["AWS", "Docker", "Prometheus", "Fluentd", "GitHub Actions", "CI/CD", "Git", "Linux"]},
]

EXPERIENCE = [
    {
        "company": "Prana",
        "url": "https://www.prana.health/",
        "role": "Software Engineer",
        "location": "USA · Remote",
        "start": "December 2024",
        "end": "June 2026",
        "highlights": [
            "Designed and shipped a unified LLM coaching agent on AWS Bedrock (Claude Sonnet) with LangChain tool-calling, SSE streaming, a thread-scoped tool cache, and multi-stage pipelines for onboarding, DEXA scan processing, and blood biomarker extraction via AWS Textract.",
            "Implemented a hybrid RAG pipeline using Pinecone (BM25 + Titan Embeddings v2) and Mem0 for persistent cross-session user memory, enabling personalized coaching context that compounds over time.",
            "Architected a large-scale FastAPI + PostgreSQL backend with dual-auth (Supabase JWT + SHA256-hashed MCP API keys), row-locking transaction helpers, Supabase RLS policies, and a custom in-memory rate limiter.",
            "Engineered a production Flutter client with real-time AI chat (SSE streaming with embedded charts), offline-first data persistence with background sync, and fluid drag-and-drop interactions.",
        ],
    },
    {
        "company": "BlindMe",
        "role": "Lead Product Engineer",
        "location": "Turkey · Remote",
        "start": "January 2024",
        "end": "March 2025",
        "highlights": [
            "Designed a two-tier matching system combining geospatial indexing with a weighted compatibility scoring engine, exposed via optimized REST APIs and consumed in a React Native client.",
            "Optimized React Native state management to achieve smooth 60fps gesture-driven animations; built and maintained GitHub Actions CI/CD pipelines enforcing test coverage and API contract validation.",
        ],
    },
    {
        "company": "Edventures",
        "url": "https://edventures.ai/",
        "role": "Flutter Engineer and Advisor",
        "location": "Sweden · Remote",
        "start": "December 2023",
        "end": "February 2024",
        "highlights": [
            "Defined the mobile architecture roadmap and led migration to a serverless backend; mentored the team on Flutter Clean Architecture, reducing technical debt through structured code reviews.",
        ],
    },
]

PROJECTS = [
    {
        "name": "commitai",
        "url": "https://github.com/gauransh18/commitai",
        "description": "Go CLI that reads staged git diffs and generates conventional commit messages using Kimi K2 via NVIDIA NIM. Installable via go install or Homebrew.",
        "tech": ["Go", "Kimi K2", "NVIDIA NIM", "CLI"],
    },
    {
        "name": "Darwinian Dialectics",
        "url": "https://github.com/gauransh18/darwinian-dialectics",
        "description": "Self-correcting reasoning engine on LangGraph with a recursive Generator-Critic loop. Includes a Lifelong Learning memory system using ChromaDB (Vector RAG) + DSPy BootstrapFewShot and a Human-in-the-Loop Chainlit interface.",
        "tech": ["LangGraph", "DSPy", "Llama-3", "ChromaDB", "RAG", "Chainlit"],
    },
    {
        "name": "Lenk",
        "url": "https://lenk-chat.web.app/",
        "description": "Chat application with AI-driven sentiment analysis to suggest replies and analyze user emotions. Cross-platform Flutter client with real-time messaging and Firebase backend.",
        "tech": ["Flutter", "Firebase", "Sentiment Analysis"],
        "paper": "https://ieeexplore.ieee.org/document/10921967",
    },
    {
        "name": "Resilient Microservices Architecture",
        "url": "https://github.com/gauransh18/Resilience-Lab",
        "description": "User/Order microservices with real-time monitoring via Prometheus/Fluentd, implementing fault tolerance through Circuit Breaker patterns, retry mechanisms, and chaos testing.",
        "tech": ["Python", "Flask", "Docker", "Prometheus", "Chaos Engineering"],
    },
    {
        "name": "FasFasTyping",
        "url": "https://fasfastyping.web.app/",
        "description": "Minimalist typing speed test built with vanilla JavaScript. Three test modes, floating real-time caret, live WPM and accuracy tracking, and a post-test performance chart on Canvas API with no charting libraries.",
        "tech": ["JavaScript", "Canvas API", "Firebase", "Vanilla JS"],
    },
]

EDUCATION = [
    {
        "school": "Vellore Institute of Technology (VIT)",
        "degree": "Bachelor of Technology in Computer Science and Engineering",
        "cgpa": "8.41/10",
        "start": "2021",
        "end": "2025",
    }
]

CERTIFICATIONS = [
    {"name": "AWS Solution Architect Associate", "issued": "February 2024", "url": "https://cp.certmetrics.com/amazon/en/public/verify/credential/66e19f5651d549d892f51b5dbc1d8302"},
    {"name": "AWS Cloud Practitioner",           "issued": "January 2024",  "url": "https://cp.certmetrics.com/amazon/en/public/verify/credential/GCYF2KQBYF41QSG9"},
    {"name": "IBM DevOps",                       "issued": "April 2023",    "url": None},
]
