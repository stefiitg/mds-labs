import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def next_id(tasks):
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


def cmd_add(tasks, args):
    desc = " ".join(args).strip()
    if not desc:
        print("Error: description cannot be empty")
        return
    tasks.append({"id": next_id(tasks), "description": desc, "done": False})
    print(f"Added task: {desc}")


def cmd_list(tasks, args):
    active = [t for t in tasks if not t["done"]]
    if not active:
        print("No tasks")
        return
    for t in active:
        print(f"[{t['id']}] {t['description']}")


def cmd_done(tasks, args):
    if not args:
        print("Error: missing task ID")
        return
    try:
        tid = int(args[0])
    except ValueError:
        print("Error: invalid ID")
        return
    for t in tasks:
        if t["id"] == tid:
            if t["done"]:
                print(f"Task [{tid}] is already done")
                return
            t["done"] = True
            print(f"Task [{tid}] marked as done")
            return
    print(f"Error: no task with ID {tid}")


def cmd_delete(tasks, args):
    if not args:
        print("Error: missing task ID")
        return
    try:
        tid = int(args[0])
    except ValueError:
        print("Error: invalid ID")
        return
    for i, t in enumerate(tasks):
        if t["id"] == tid:
            del tasks[i]
            print(f"Task [{tid}] deleted")
            return
    print(f"Error: no task with ID {tid}")


def cmd_help(tasks, args):
    print("Commands:")
    print("  add <description>  - Add a new task")
    print("  list               - List active tasks")
    print("  done <ID>          - Mark a task as done")
    print("  delete <ID>        - Delete a task")
    print("  help               - Show this help")
    print("  exit / quit        - Save and exit")


COMMANDS = {
    "add": cmd_add,
    "list": cmd_list,
    "done": cmd_done,
    "delete": cmd_delete,
    "help": cmd_help,
}


def main():
    tasks = load_tasks()
    print("TODO: type 'help' for commands, 'exit' to quit")
    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            break
        if not line:
            continue
        parts = line.split()
        cmd = parts[0].lower()
        args = parts[1:]
        if cmd in ("exit", "quit"):
            break
        handler = COMMANDS.get(cmd)
        if handler:
            handler(tasks, args)
        else:
            print(f"Unknown command: {cmd}")
    save_tasks(tasks)
    print("Tasks saved. Goodbye!")


if __name__ == "__main__":
    main()
