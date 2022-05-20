# **** So basically, we need to parse the initial file, and then we need to loop through the changed and see what task the file corresponds to


tsk = [
    'task: taskA', 'files: foo.txt', 'deps: taskB taskC', '',
    'task: taskB', 'files: foo.txt', 'deps: taskD', '',
    'task: taskC', 'files: foo.txt', 'deps: taskD', '',
    'task: taskD', 'files: foo.txt', 'deps:', ''
]

changed = [
    "foo.txt",
]

def parse_task(task):
    return task.split(" ")[1]

def parse_files(files):
    return files.split(" ")[1:]

def parse_deps(deps):
    return deps.split(" ")[1:]

def parse(raw):
    tups = []

    i = 0
    while i < len(raw):
        tups.append((parse_task(raw[i]), parse_files(raw[i + 1]), parse_deps(raw[i + 2]))); # Keep the dependencies as empty for now
        i += 4
    
    return tups

def find_changed(parsed, changed):
    tasks = []

    for tup in parsed:
        for change in changed:
            if change in tup[1]:
                tasks.append(tup[0])
    
    return tasks

def build_dependency_chain(tuple):
    dic = {}
    
    for tup in tuple:
        dic[tup[0]] = tup[2]
    
    return dic

def main():
    parsed = parse(tsk)
    out = find_changed(parsed, changed)

    # **** So currently, we have got all of the tasks that need to be performed for the update, and now we need to figure out any dependencies that need to be run
    # **** We will just get the build dependencies for each one, and not add it in if it has already been added
    # **** We should not add dependencies to the list that do not include any file changes ? (ok !)

    # **** So what I am thinking is build a dependency graph for all of them, concatenate them together, and then remove anything that is not needed ?

    print(parsed)
    print(out)
    print(build_dependency_chain(parsed))

if __name__ == "__main__":
    main()