import json
import subprocess
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# Funcția periculoasă pe care vrem să o protejăm
def run_command(command):
    # AICI ESTE BARIERA DE SIGURANȚĂ CERUTĂ ÎN LABORATOR
    print(f"\n⚠️  ATENȚIE! AI-ul dorește să ruleze următoarea comandă în terminalul tău:")
    print(f"   > {command}")
    
    confirm = input("Permiți rularea acestei comenzi? (y/n): ")
    if confirm.lower() != 'y':
        return "Execuția a fost respinsă de către utilizator."
        
    try:
        # Executăm comanda în bash și returnăm output-ul
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout if result.stdout else "Comanda a rulat cu succes, fără output."
    except subprocess.CalledProcessError as e:
        return f"Eroare la rularea comenzii: {e.stderr}"

tools = [
    {
        "type": "function",
        "function": {
            "name": "run_command",
            "description": "Run a shell command on the user's Linux machine.",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {"type": "string", "description": "The exact bash command to execute, e.g. 'ls -l' or 'echo hello'"}
                },
                "required": ["command"],
            },
        },
    }
]

messages = [{"role": "system", "content": "You are a coding assistant. You can run bash commands to inspect the system or create files."}]

print("🤖 Coding Agent pregătit! (ex: 'Arată-mi ce fișiere sunt în folderul curent' sau 'exit' pentru a ieși)")

while True:
    user_input = input("\nTu: ")
    if user_input.lower() in ['exit', 'quit']:
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="mistral",
        messages=messages,
        tools=tools,
    )

    msg = response.choices[0].message

    if msg.tool_calls:
        messages.append(msg)
        for tool_call in msg.tool_calls:
            args = json.loads(tool_call.function.arguments)
            if tool_call.function.name == "run_command":
                # Apelăm funcția protejată
                result = run_command(args["command"])
            else:
                result = "Tool necunoscut."
                
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            })
            
        final_response = client.chat.completions.create(model="mistral", messages=messages, tools=tools)
        reply = final_response.choices[0].message.content
        print(f"\n🤖 AI: {reply}")
        messages.append({"role": "assistant", "content": reply})
    else:
        print(f"\n🤖 AI: {msg.content}")
        messages.append({"role": "assistant", "content": msg.content})