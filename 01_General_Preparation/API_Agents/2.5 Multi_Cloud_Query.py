import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI, AzureOpenAI
from anthropic import Anthropic
from google import genai
from google.genai import types

# Encuentra el archivo .env que se va a usar 
env_path = find_dotenv() 
print("📂 Archivo .env detectado:", env_path)

load_dotenv()


def get_client_and_model(provider="local"):
    """
    Returns the appropriate client and model name based on your environment.
    """
    if provider == "openai":
        client = OpenAI(api_key=os.getenv("PLATFORM_OPENAI_CHAT_API_KEY"))
        model  = os.getenv("PLATFORM_OPENAI_CHAT_GPT4O_MODEL", "gpt-4o")

    elif provider == "azure":
        client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_GPT4O_ENDPOINT", ""),
            api_key=os.getenv("AZURE_OPENAI_GPT4O_KEY"),
            api_version="2024-02-01"
        )
        model = os.getenv("AZURE_OPENAI_GPT4O_MODEL", "")
        print("EndPoint:", client._azure_endpoint)

    elif provider == "local":
        client = OpenAI(
            base_url=os.getenv("LOCAL_GPT35turbo_CHAT_ENDPOINT"),
            api_key=os.getenv("LOCAL_GPT35turbo_CHAT_KEY")
        )
        model = os.getenv("LOCAL_GPT35turbo_CHAT_MODEL", "gpt-4o")

    elif provider == "claude":
        client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        model  = os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-6")
        print("EndPoint:", client._base_url)

    # ── New providers ─────────────────────────────────────────────────────────

    elif provider == "gemini":
        # Uses google-genai SDK — returned as a plain dict so run_prompt_test
        # can detect it and call the right API.
        client = {"sdk": genai.Client(api_key=os.getenv("GEMINI_API_KEY"))}
        model  = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        print("EndPoint: https://generativelanguage.googleapis.com")

    elif provider == "grok":
        # OpenAI-compatible — just swap base_url + api_key
        client = OpenAI(
            api_key=os.getenv("XAI_API_KEY"),
            base_url=os.getenv("XAI_BASE_URL", "https://api.x.ai/v1")
        )
        model = os.getenv("XAI_MODEL", "grok-4-1-fast")

    elif provider == "deepseek":
        # OpenAI-compatible — just swap base_url + api_key
        client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
        )
        model = os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash")

    elif provider == "mistral":
        # OpenAI-compatible — just swap base_url + api_key
        client = OpenAI(
            api_key=os.getenv("MISTRAL_API_KEY"),
            base_url="https://api.mistral.ai/v1"
        )
        model = os.getenv("MISTRAL_MODEL", "mistral-large-latest")

    else:
        client = OpenAI(api_key=os.getenv("OPENAI_CHAT_KEY"))
        model  = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o")

    # Gemini client is a dict — skip generic prints for it
    if not isinstance(client, dict):
        print("api_key:", client.api_key)
        print("model:  ", model)
        print("URL:    ", client.base_url)

    return client, model


def run_prompt_test(provider):
    client, model = get_client_and_model(provider)

    prompt = "Write a short story about the Roman Empire."

    print(f"\n--- [Connecting to {provider.upper()}] ---")
    print(f"Target Model: {model}")

    try:
        if provider == "claude":
            response = client.messages.create(
                model=model,
                max_tokens=200,
                messages=[{"role": "user", "content": prompt}]
            )
            print("\n--- [Model Response] ---")
            print(response.content[0].text)

        elif provider == "gemini":
            response = client["sdk"].models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(max_output_tokens=200, temperature=0.7)
            )
            print("\n--- [Model Response] ---")
            print(response.text)

        else:
            # OpenAI-compatible: openai, azure, local, grok, deepseek, mistral
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
    selected_provider = "claude"   # openai | azure | local | claude | gemini | grok | deepseek | mistral
    run_prompt_test(selected_provider)
