import os 
import click
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

api_key=os.getenv("OPEN_API_KEY")





client = InferenceClient(
    provider="novita",
    api_key=api_key,
)
@click.command()
@click.argument('prompt')
def chat( prompt):
    completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
        )
    
    click.echo(completion.choices[0].content)
    


chat()


