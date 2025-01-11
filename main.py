from linkedin_api import Linkedin
from dotenv import load_dotenv # type: ignore
import os



# Load environment variables from .env file
load_dotenv()



email = os.getenv('LINKEDIN_EMAIL')

profile_name = os.getenv('LINKEDIN_PROFILE_NAME')

password = os.getenv('LINKEDIN_PASSWORD')

# Authenticate using any Linkedin user account credentials
#TROUVER LES CREDENTIALS QUAND ON UTILISE GOOGLE POUR SE CONNECTER
api = Linkedin(email, password)

# GET a profile
try:
    profile = api.get_profile(profile_name)
    print("Auth success")

except Exception as e:
    print("Auth failed")
    print("e")

# GET a profiles contact info
contact_info = api.get_profile_contact_info(profile_name)

print(f"contact : {contact_info}")

# GET 1st degree connections of a given profile
#connections = api.get_profile_connections('1234asc12304')