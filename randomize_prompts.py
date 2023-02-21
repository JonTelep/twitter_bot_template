import random


def give_me_a_prompt():
    prompt_templates = [
        "Generate a joke about {tech_topic}.",
        "Generate a joke about {code_language}.",
        "Generate a joke about {tech_position}.",
        "Generate a joke about {tech_company}.",
        "Tell me a tech tip about {tech_topic} today?",
        "Tell me a tech tip about {code_language} today?",
        "Tell me an interesting fact about {tech_topic}.",
        "Tell me an interesting fact about {tech_company}.",
        "Tell me an interesting fact about {code_language}.",
        "Tell me a historic fact about {tech_topic}?",
        "Tell me a historic fact about {code_language}?",
        "Tell me a historic fact about {tech_company}?"
    ]

    tech_topics = ["Artificial Intelligence",    "Machine Learning",    "Deep Learning",    "Computer Vision",    "Natural Language Processing",    "Big Data",    "Cloud Computing",    "Internet of Things",    "Blockchain",    "Cybersecurity",    "Virtual Reality",
                "Augmented Reality",    "5G Technology",    "Robotics",    "Autonomous Vehicles",    "Drones",    "Quantum Computing",    "Software Development",    "Mobile App Development",    "Web Development",    "Data Science",    "DevOps",    "IT Infrastructure", "Crypto", "Cryptocurrency", "Etheruem"]

    coding_languages = [
        "Java",    "C",    "Python",    "C++",    "JavaScript",    "C#",    "Ruby",    "Swift",    "Go",    "PHP",    "TypeScript",    "Objective-C",    "R",    "Kotlin",    "Scala",    "SQL",    "Visual Basic .NET",    "Rust",    "Assembly",    "Dart",    "Lisp",    "Perl",    "Haskell",    "Prolog",    "Erlang",    "Common Lisp", "Solidity", "React JS", "Astro JS"]

    tech_positions = ["Software Engineer",    "Data Scientist",    "DevOps Engineer",    "Full-Stack Developer",    "Mobile Developer",    "Front-End Developer",    "Back-End Developer",    "Cloud Engineer",    "Systems Administrator",    "Database Administrator",    "Network Engineer",
                    "Security Analyst",    "Information Security Engineer",    "Quality Assurance Engineer",    "Product Manager",    "Project Manager",    "UX Designer",    "UI Designer",    "Business Analyst",    "Technical Writer",    "IT Support Specialist",    "Tech Sales Representative"]

    tech_companies = ["Apple",    "Amazon",    "Google",    "Microsoft",    "Facebook",    "Alphabet",    "Intel",    "Oracle",    "IBM",    "Samsung",    "Alibaba",    "Tencent",
                    "Baidu",    "Nvidia",    "HP",    "Dell",    "Cisco",    "Qualcomm",    "AMD",    "Intel",    "Tesla",    "Uber",    "Netflix",    "Spotify", "Red Hat Technologies"]


    template = random.choice(prompt_templates)
    code_language = random.choice(coding_languages)
    tech_topic = random.choice(tech_topics)
    tech_position = random.choice(tech_positions)
    tech_company = random.choice(tech_companies)

    prompt = template.format(tech_topic=tech_topic, code_language=code_language,
                            tech_position=tech_position, tech_company=tech_company)

    return prompt
