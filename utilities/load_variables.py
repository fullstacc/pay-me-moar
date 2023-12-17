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
