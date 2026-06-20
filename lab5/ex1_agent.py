import json
import requests
from openai import OpenAI

# Conectarea la serverul local Ollama
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# --- DEFINIREA FUNCȚIILOR LOCALE (TOOLS) ---
def get_weather(city):
    """Returnează vremea folosind serviciul gratuit wttr.in"""
    try:
        response = requests.get(f"https://wttr.in/{city}?format=%C+%t")
        return response.text.strip()
    except Exception:
        return "Eroare la obținerea vremii."

def calculate(expression):
    """Evaluează o expresie matematică"""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Eroare de calcul: {e}"

# --- CONFIGURAREA SCHEMELOR PENTRU AI ---
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate an arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "The expression to evaluate, e.g. '2 + 3 * 4'"}
                },
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a specific city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "The name of the city, e.g. 'Paris', 'Bucharest'"}
                },
                "required": ["city"],
            },
        },
    }
]

# Prompt-ul de sistem obligă modelul să folosească funcțiile
messages = [
    {"role": "system", "content": "You are a helpful assistant. Use the provided tools when needed to answer exactly."}
]

print("🤖 Agentul este pregătit! Întreabă-mă despre vreme sau calcule (Scrie 'exit' pentru a ieși).")

# --- BUCLA INTERACTIVĂ ---
while True:
    user_input = input("\nTu: ")
    if user_input.lower() in ['exit', 'quit']:
        break
        
    messages.append({"role": "user", "content": user_input})
    
    # 1. Răspuns FĂRĂ tool calls (simplu)
    plain_response = client.chat.completions.create(
        model="mistral",
        messages=messages
    )
    print(f"\n🤖 AI (fără tool-uri): {plain_response.choices[0].message.content}")

    # 2. Răspuns CU tool calls
    response = client.chat.completions.create(
        model="mistral",
        messages=messages,
        tools=tools,
    )
    
    msg = response.choices[0].message
    
    # Verificăm dacă LLM-ul vrea să apeleze o funcție
    if msg.tool_calls:
        messages.append(msg)  # Salvăm decizia lui în istoric
        
        for tool_call in msg.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            
            print(f"   [⚙️ Rulăm local: {name} cu argumentele {args}]")
            
            # Executăm funcția reală în Python
            if name == "calculate":
                result = calculate(args["expression"])
            elif name == "get_weather":
                result = get_weather(args["city"])
            else:
                result = "Tool necunoscut."
                
            # Adăugăm rezultatul înapoi în conversație
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            })
            
        # Cerem LLM-ului să formuleze răspunsul final bazat pe rezultatele primite
        final_response = client.chat.completions.create(
            model="mistral",
            messages=messages,
            tools=tools,
        )
        reply = final_response.choices[0].message.content
        print(f"\n🤖 AI (cu tool-uri): {reply}")
        messages.append({"role": "assistant", "content": reply})
        
    else:
        # LLM-ul a putut răspunde direct, fără unelte
        print(f"\n🤖 AI (cu tool-uri): {msg.content}")
        messages.append({"role": "assistant", "content": msg.content})



      