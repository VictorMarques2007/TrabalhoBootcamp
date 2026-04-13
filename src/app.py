import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

def add_task(task):
    if not task:
        raise ValueError("Tarefa não pode ser vazia")
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

def list_tasks():
    return load_tasks()

def remove_task(index):
    tasks = load_tasks()
    if index < 0 or index >= len(tasks):
        raise IndexError("Tarefa não existe")
    tasks.pop(index)
    save_tasks(tasks)

def menu():
    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("0 - Sair")

        choice = input("Escolha: ")

        if choice == "1":
            task = input("Digite a tarefa: ")
            add_task(task)

        elif choice == "2":
            for i, t in enumerate(list_tasks()):
                print(f"{i} - {t}")

        elif choice == "3":
            i = int(input("Índice da tarefa: "))
            remove_task(i)

        elif choice == "0":
            break

if __name__ == "__main__":
    menu()