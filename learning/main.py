# Import FastAPI framework
from fastapi import FastAPI

# Create FastAPI app instance
app=FastAPI()

# Route for root URL - returns a simple message
@app.get("/")
def read_root():
    return {"message":"Hello World!"}

# Route with path parameter and query parameter
# Example: /item/5?q=test
@app.get("/item/{item_id}")
def read_item(item_id:int, q:str | None):
    # item_id comes from URL path, q is optional query parameter
    return {"item_id":item_id,"q":q}

# Run with: uvicorn main:app --reload


# What I learned:
# - FastAPI creates REST APIs easily
# - @app.get() decorator defines routes
# - Path parameters {item_id} capture values from URL
# - Query parameters (q:str=None) are optional
# - Type hints enable automatic validation
# - FastAPI converts dict to JSON automatically