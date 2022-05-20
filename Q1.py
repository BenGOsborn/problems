# **** So basically, we need to parse the initial file, and then we need to loop through the changed and see what task the file corresponds to

tsk = [
  "task: taskA",
  "files: lib/foo.txt lib/bar.txt",
  "deps:",
  "",
  "task: taskB",
  "files: src/baz.txt",
  "deps:",
  "",
  "task: taskC",
  "files: README.md",
  "deps:",
  ""
]

changed = [
    "lib/foo.txt",
    "README.md" 
]

def parse_task(task):
    return task.split(" ")[1]

def parse_files(files):
    return files.split(" ")[1:]

def parse(raw):
    tups = []

    i = 0
    while i < len(raw):
        tups.append((parse_task(raw[i]), parse_files(raw[i + 1]), [])); # Keep the dependencies as empty for now
        i += 4
    
    return tups

def find_changed(parsed, changed):
    tasks = []

    for tup in parsed:
        for change in changed:
            if change in tup[1]:
                tasks.append(tup[0])
    
    return tasks

def main():
    parsed = parse(tsk)
    out = find_changed(parsed, changed)

    print(out)

if __name__ == "__main__":
    main()