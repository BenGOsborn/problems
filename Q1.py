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

def find(elem, dep, seen, solved, out):
    seen[elem] = True

    if elem in dep:
        for item in dep[elem]:
            if item in solved and solved[item] == True:
                continue;
            elif item in seen and seen[item] == True:
                raise Exception("Loop exists")
            else:
                find(item, dep, seen, solved, out)

    solved[elem] = True
    
    out.append(elem)

def get_all_task_order(to_rerun, dep):
    out = []
    seen = {}
    solved = {}

    for elem in to_rerun:
        find(elem, dep, seen, solved, out)
    
    return out

def main():
    parsed = parse(tsk)
    to_rerun = find_changed(parsed, changed)

    dep = build_dependency_chain(parsed)

    print("Parsed", parsed)
    print("Out", to_rerun)

    print("Dep", dep)

    task_order = get_all_task_order(to_rerun, dep)

    print("Task order", task_order)

if __name__ == "__main__":
    main()