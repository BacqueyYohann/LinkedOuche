from linkedin_api import Linkedin

# Authenticate using any Linkedin user account credentials
#TROUVER LES CREDENTIALS QUAND ON UTILISE GOOGLE POUR SE CONNECTER
api = Linkedin('reedhoffman@linkedin.com', '*******')

# GET a profile
profile = api.get_profile('billy-g')

# GET a profiles contact info
contact_info = api.get_profile_contact_info('billy-g')

# GET 1st degree connections of a given profile
connections = api.get_profile_connections('1234asc12304')