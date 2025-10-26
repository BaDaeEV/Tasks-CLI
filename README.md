# Tasks-CLI
JSON-based task list with CLI

Usage on Linux:

Add a task:
    python3 <filename> add "<description>"

Update a task by ID:
    python3 <filename> update <taskID> "<new description>"

Delete a task by ID:
    python3 <filename> delete <taskID>

Mark a task as in-progress:
    python3 <filename> mark-in-progress <taskID>

Mark a task as done:
    python3 <filename> mark-done <taskID>

List tasks:
    python3 <filename> list                # lists all tasks
    python3 <filename> list <status>       # lists tasks filtered by status (todo, in-progress, done)

