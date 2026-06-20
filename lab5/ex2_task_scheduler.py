import json
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

# O listă simplă în memorie pentru a simula baza de date a TODO-urilor
tasks = []

def add_task(title, date):
    """Adaugă un task în sistem"""
    tasks.append({"title": title, "date": date})
    return f"Task-ul '{title}' a fost adăugat cu succes pentru data {date}."

def list_tasks():
    """Listează toate task-urile"""
    if not tasks:
        return "Nu ai niciun task planificat."
    result = "Task-urile tale sunt:\n"
    for i, t in enumerate(tasks):
        result += f"{i+1}. {t['title']} (Data: {t['date']})\n"
    return result

tools = [
    {
        "type": "function",
        "function": {
            "name": "add_task",
            "description": "Add a new task to the task scheduler.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {"type": "string", "description": "The title or description of the task"},
                    "date": {"type": "string", "description": "The due date of the task in DD-MM-YYYY format or similar"}
                },
                "required": ["title", "date"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_tasks",
            "description": "List all existing tasks from the scheduler.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    }
]

messages = [
    {"role": "system", "content": "You are a task management assistant. Use the provided tools to add or list tasks when requested."}
]

print("🤖 Agentul TODO este pregătit! (ex: 'Adaugă un task să plătesc taxele pe 25 mai 2026' sau 'exit' pentru a ieși)")

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
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            print(f"   [⚙️ Rulăm local: {name} cu argumentele {args}]")

            if name == "add_task":
                result = add_task(args["title"], args["date"])
            elif name == "list_tasks":
                result = list_tasks()
            else:
                result = "Tool necunoscut."

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            })

        final_response = client.chat.completions.create(
            model="mistral",
            messages=messages,
            tools=tools,
        )
        reply = final_response.choices[0].message.content
        print(f"\n🤖 AI: {reply}")
        messages.append({"role": "assistant", "content": reply})

    else:
        print(f"\n🤖 AI: {msg.content}")
        messages.append({"role": "assistant", "content": msg.content})
