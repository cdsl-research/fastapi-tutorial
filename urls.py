from controllers import *

# FastAPI routing function
app.add_api_route('/', index_test)
app.add_api_route('/admin', admin)