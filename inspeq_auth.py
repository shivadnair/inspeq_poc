from inspeq.client import InspeqEval
import os
from dotenv import load_dotenv

#loading the environment variables
load_dotenv()

#creating an instance of the InspeqEval class
def inspeq_auth():
    inspeq_auth = InspeqEval(
        inspeq_api_key=os.getenv("INSPEQ_API_KEY"),
        inspeq_project_id=os.getenv("INSPEQ_PROJECT_ID"),
    )
    return inspeq_auth