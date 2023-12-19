from dotenv import load_dotenv
import os

# Function to initialize and return environment variables
def init_variables():
    load_dotenv(".env")  # Load environment variables

    url = os.getenv('SUPABASE_SITE')
    key = os.getenv('SUPABASE_KEY')
    email = os.getenv('EMAIL')
    password = os.getenv('SUPABASE_PASS')



    return url, key, email, password

def init_stopwords():

    # stopwords for the word cloud
    stopwords = [
    "experience", "working", "work", "skills", "proficiency", "preferred",
    "excellent", "strong", "demonstrated", "extensive", "understand", "understanding",
    "proven", "track", "record", "fluent", "proficient", "knowledge", "industry",
    "such", "as", "e.g.", "with", "using", "used", "and", "or", "in", "on", "for",
    "of", "to", "a", "an", "the", "is", "plus", "including", "ability", "able",
    "environments", "environment", "systems", "system", "applications", "application",
    "tools", "tool", "technologies", "technology", "solutions", "solution", "methods",
    "method", "platforms", "platform", "services", "service", "designing", "design",
    "building", "build", "shipping", "ship", "contributing", "contribute",
    "development", "developing", "achieve", "maintain", "compliance", "security",
    "architecture", "architectures", "algorithms", "programming", "program",
    "managing", "manage", "leadership", "leader", "team", "teams", "projects",
    "project", "programs", "program", "product", "products", "developer", "develop",
    "engineering", "engineer", "infrastructure", "UI", "UX",
    "SOA", "databases", "frontend", "backend",
    "web", "mission-critical", "general-purpose", "deep", "learning",
    "natural", "language", "processing"
]
    return stopwords


