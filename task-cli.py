#!/usr/bin/env python3
import json
from datetime import datetime
import pytz
import os
import argparse

# Variables
TaskListFile = "tasksList.json"
taskID = 0
defaultStatus = "todo"


if os.path.exists(TaskListFile):
    with open(TaskListFile, "r", encoding="utf-8") as f:
        tasksList = json.load(f)
        print("Configuration file loaded successfully.")
else:
    tasksList = []
    with open(TaskListFile, "w", encoding="utf-8") as f:
        json.dump(tasksList, f, ensure_ascii=False, indent=4)
        print("Configuration file created successfully.")

def uniqueID():
    if tasksList:
        return max(task["id"] for task in tasksList) + 1
    else:
        return 0

def getTimestamp():
    dt = datetime.now(pytz.timezone("Europe/Warsaw"))
    timestamp = dt.strftime("%Y/%m/%d_%H:%M:%S")
    return timestamp

# Add // Update // Delete task functions

def saveTaskList():
    with open(TaskListFile, "w", encoding="utf-8") as f:
        json.dump(tasksList, f, ensure_ascii=False, indent=4)

def addTask(description):
    task = {
        "id": uniqueID(),
        "description": description,
        "status": defaultStatus,
        "createdAt": getTimestamp(),
        "updatedAt": getTimestamp()
    }
    tasksList.append(task)
    task_id = uniqueID() - 1
    print(f"Task added successfully (ID: {task_id})")   
    uniqueID()
    saveTaskList()

def updateTaskDescription(taskID, Newdescription):
    for task in tasksList:
        if task["id"] == taskID:
            task["description"] = Newdescription
            task["updatedAt"] = getTimestamp()
            saveTaskList()

def mark_in_progress(taskID):
    for task in tasksList:
        if task["id"] == taskID:
            task["status"] = "in-progress"
            task["updatedAt"] = getTimestamp()
            saveTaskList()

def mark_done(taskID):
    for task in tasksList:
        if task["id"] == taskID:
            task["status"] = "done"
            task["updatedAt"] = getTimestamp()
            saveTaskList()

def updateTaskStatus(taskID, taskStatus):
    for task in tasksList:
        if task["id"] == taskID:
            task["description"] = taskStatus
            task["updatedAt"] = getTimestamp()
            saveTaskList()

def deleteTask(taskID):
    global tasksList
    tasksList = [task for task in tasksList if task["id"] != taskID]
    with open(TaskListFile, "w", encoding="utf-8") as f:
        json.dump(tasksList, f, ensure_ascii=False, indent=4)
    print(f"Usunięto zadanie o ID {taskID}")
            

def listTasks(status=None):
    if status:
        for task in tasksList:
            if task["status"] == status:
                print(task)
        print(f"Listed tasks with status: {status}")
    else:
        for task in tasksList:
            print(task)
        print(f"Listed ALL tasks: {status}")


#  CLI Argument Parsing
parser = argparse.ArgumentParser(description="Task Management System", prog="task-cli")
subparsers = parser.add_subparsers(dest="command", required=True)

# Subparser for add command
parser_add = subparsers.add_parser("add")
parser_add.add_argument("description", type=str, help="Description of the task to add")

#subparser for update command
parser_update = subparsers.add_parser("update")
parser_update.add_argument("id", type=int, help="Taks ID")
parser_update.add_argument("description", type=str, help="Update descruption of the task to update by id")

#subparser for delete command
parser_delete = subparsers.add_parser("delete")
parser_delete.add_argument("id", type=int, help="Taks ID")

#subparser for mark-in-progress command
parser_markinprogress = subparsers.add_parser("mark-in-progress")
parser_markinprogress.add_argument("id", type=int, help="Unique Task ID")

#subparser for mark-done command
parser_markdone = subparsers.add_parser("mark-done")
parser_markdone.add_argument("id", type=int, help="Unique Task ID")

#subparser for list command
parser_list = subparsers.add_parser("list")
parser_list.add_argument("status", type=str, nargs="?", choices=["todo","in-progress","done"], help="Filtering by Status")

# Parsing args
args = parser.parse_args()

if args.command == "add":
    addTask(args.description)
elif args.command == "update":
    updateTaskDescription(args.id, args.description)
elif args.command == "delete":
    deleteTask(args.id)
elif args.command == "mark-in-progress":
    mark_in_progress(args.id)
elif args.command == "mark-done":
    mark_done(args.id)
elif args.command == "list":
    listTasks(args.status)




