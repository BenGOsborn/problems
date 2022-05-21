# **** So basically, we need to parse the initial file, and then we need to loop through the changed and see what task the file corresponds to


tsk = [
    "task: distributeImages",
    "files: images/dogs/*.jpg images/*/*.png",
    "deps: compressJpegs compressPngs",
    "",
    "task: compressJpegs",
    "files: images/dogs/*.jpg",
    "deps:",
    "",
    "task: compressPngs",
    "files: images/*/*.png",
    "deps:",
    ""
]


changed = [
    "images/dogs/dalmatian.jpg",
    "images/dogs/retriever.jpg"
]

def match_glob(glob, file):
    if glob == "" and file == "": return True
    if glob == "" and file != "": return False
    if glob != "" and file == "":
        if glob == "*": return True
        return False

    if glob[0] == "*":
        glob_sliced = glob[1:]
        if match_glob(glob_sliced, file): return True
        if file[0] == "": return False

        file_sliced = file[1:]
        if match_glob(glob, file_sliced): return True
        
        return False


    if glob[0] == file[0]:
        glob_sliced = glob[1:]
        file_sliced = file[1:]

        return match_glob(glob_sliced, file_sliced)
    
    return False

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
            # **** This is the line that we need to change
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

def get_all_tasks(to_rerun, dep):
    out = []
    seen = {}
    solved = {}

    for elem in to_rerun:
        find(elem, dep, seen, solved, out)

    already_in = {}
    real_output = []
    for elem in out:
        if elem not in already_in:
            already_in[elem] = True
            real_output.append(elem)
    
    return real_output

# **** It seems that the dependencies will stay the same, but we just need to modify the find changed function

def get_ordered_tasks(to_rerun, dep):
    bloated = get_all_tasks(to_rerun, dep)

    out = []

    for elem in bloated:
        if elem in to_rerun:
            out.append(elem)

    return out

def main():
    print(match_glob("images/dogs/*.jpg", "images/dogs/dalmatian.jpg"))

    # parsed = parse(tsk)
    # to_rerun = find_changed(parsed, changed)

    # dep = build_dependency_chain(parsed)

    # print("Parsed", parsed)
    # print("Out", to_rerun)

    # print("Dep", dep)

    # print("OUT", get_ordered_tasks(to_rerun, dep))
    

if __name__ == "__main__":
    main()