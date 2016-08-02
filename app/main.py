import webapp2
import os
import sys

# Add vendor directory to module search path
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)

vendor_dir = os.path.join(current_dir, 'lib')
sys.path.append(vendor_dir)

import routes

# When running on Google App Engine turn debugging off
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
    debug_setting = False
# When running locally set debug on
else:
    debug_setting = True

app = webapp2.WSGIApplication(routes.ROUTES, debug=debug_setting) # Load the app
