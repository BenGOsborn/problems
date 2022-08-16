def add_to_list(string, clicks, clicks_map):
    string_split = string.split(".")

    for i in range(len(string_split)):
        slc = string_split[i:len(string_split) + 1]
        curr = ".".join(slc)

        if curr in clicks_map:
            clicks_map[curr] += clicks
        else:
            clicks_map[curr] = clicks

def main():
    clicks_map = {}

    counts = [
        "900,google.com",
        "300,yahoo.com"
    ]

    for count in counts:
        split = count.split(",")
        clicks = int(split[0])
        domain = split[1]

        add_to_list(domain, clicks, clicks_map)

    print(clicks_map)

if __name__ == "__main__":
    main()