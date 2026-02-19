import os
import asyncio
from dotenv import load_dotenv
from dotenv import find_dotenv
from openai import OpenAI, AzureOpenAI

# Encuentra el archivo .env que se va a usar 
env_path = find_dotenv() 
print("📂 Archivo .env detectado:", env_path)

# Load your .env file
load_dotenv()


def get_client_and_model(provider="local"):

    """
    Returns the appropriate client and model name based on your environment.
    """
    if provider == "openai":
    # Standard OpenAI Cloud client
        client = OpenAI(
            api_key=os.getenv("PLATFORM_OPENAI_CHAT_API_KEY")
        )
        model = os.getenv("PLATFORM_OPENAI_CHAT_GPT4O_MODEL","gpt-4o")

    elif provider == "azure":
        # Azure requires the specialized AzureOpenAI client
        client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_GPT4O_ENDPOINT", ""),
            api_key=os.getenv("AZURE_OPENAI_GPT4O_KEY"),
            api_version="2024-02-01" # Standard stable version
        )
        model = os.getenv("AZURE_OPENAI_GPT4O_MODEL","")
        
        print("EndPoint: ",client._azure_endpoint)
        
    elif provider == "local":
    # Standard OpenAI Cloud client
        client = OpenAI(
            base_url=os.getenv("LOCAL_GPT35turbo_CHAT_ENDPOINT"),
            api_key=os.getenv("LOCAL_GPT35turbo_CHAT_KEY")
        )
        model = os.getenv("LOCAL_GPT35turbo_CHAT_MODEL","gpt-4o")
        
    else:
    # Standard OpenAI Cloud client
        client = OpenAI(
            api_key=os.getenv("OPENAI_CHAT_KEY")
        )
        model = os.getenv("OPENAI_CHAT_MODEL","gpt-4o")

        print("EndPoint: ",client._base_url)

    print("api_key: ",client.api_key)
    print("model: ",model)
    print("URL: ",client._base_url)

    return client, model

def run_prompt_test(provider):
    client, model = get_client_and_model(provider)
    
    # The specific prompt you requested
    prompt = "Write a short story about the Roman Empire."
    
    print(f"\n--- [Connecting to {provider.upper()}] ---")
    print(f"Target Model: {model}")
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
            temperature=0.7
        )
        print("\n--- [Model Response] ---")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error connecting to {provider}: {e}")


if __name__ == "__main__":
    selected_provider = "local" 
    run_prompt_test(selected_provider)
