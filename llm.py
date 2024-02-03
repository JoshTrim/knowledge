from openai import OpenAI
import instructor

from model import KnowledgeGraph

from dotenv import load_dotenv

load_dotenv()


# Adds response_model to ChatCompletion
# Allows the return of Pydantic model rather than raw JSON
client = instructor.patch(OpenAI())

def generate_graph(input) -> KnowledgeGraph:
    return client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Help me understand the following by describing it as a detailed knowledge graph: {input}",
            }
        ],
        response_model=KnowledgeGraph,
    )  # type: ignore

