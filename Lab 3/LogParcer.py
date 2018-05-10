import re
import time


if __name__ == "__main__":

    pattern = r"\S+\s-\s-\s\[01/Jul/1995:(?:00:\d{2}:\d{2}|01:00:00)\s\S+\]\s\"GET\s(?:/\S+)*/movies(?:/\S+)+\.mpg\s\S+\"\s200\s\d+"
    number_of_matched_requests = 0
    read_lines = 0
    start_time = time.time()

    with open("log_file") as file:
        for line in file:
            read_lines += 1
            if re.match(pattern, line):
                number_of_matched_requests += 1
                print(re.findall(pattern, line))

    print("\nTHE END\nNumber of all read lines: %d" % read_lines)
    print("Number of all matched requests: %d" % number_of_matched_requests)
    print("Program finished in %s seconds" % (time.time() - start_time))
