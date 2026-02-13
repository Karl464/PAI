import os
import asyncio
from openai import OpenAI, AzureOpenAI
from dotenv import load_dotenv

# Load your .env file
load_dotenv()

def get_client_and_model(provider="local"):
    """
    Returns the appropriate client and model name based on your environment.
    """
    if provider == "azure":
        # Azure requires the specialized AzureOpenAI client
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_GPT4O_CHAT_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_GPT4O_CHAT_ENDPOINT"),
            api_version="2024-02-01" # Standard stable version
        )
        model = os.getenv("AZURE_OPENAI_GPT4O_CHAT_DEPLOYMENT")
        
    elif provider == "openai":
        # Standard OpenAI Cloud client
        client = OpenAI(
            api_key=os.getenv("OPENAI_CHAT_KEY")
        )
        model = os.getenv("OPENAI_CHAT_MODEL")

    elif provider == "local":
        # Local (LM Studio) uses the standard client with a local base_url
        client = OpenAI(
            # IMPORTANT: base_url must end in /v1 for LM Studio compatibility
            base_url="http://127.0.0.1:1234/v1",
            api_key="lm-studio" # Local models require a non-empty string
        )
        model = os.getenv("LOCAL_GPT35turbo_CHAT_MODEL")

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
    # Change "local" to "openai" or "azure" to switch targets
    selected_provider = "azure" 
    run_prompt_test(selected_provider)