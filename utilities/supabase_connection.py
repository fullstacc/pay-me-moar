from utilities.load_variables import init_variables
from supabase import create_client, Client
import os

# Function to handle Supabase initialization and authentication
def init_supabase():
  try:
    url, key, email, password = init_variables()
    print('these are the environment variables currently:')
    print(f"url:{url}, key:{key}")
    print(f"email:{email},password:{password}")

    # Create Supabase client
    client = create_client(url, key)
    
    # Sign in with dedicated user credentials
    client.auth.sign_in_with_password({"email": email, "password": password})
    
    return client
  
  except Exception as e:
    print(f"Error initializing Supabase: {e}")
    raise SystemExit(1)