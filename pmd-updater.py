import sys
import re


def get_change_rule(line):
    match_obj = re.search("Use Rule name (.+) instead of the deprecated Rule name (.+)\\. PMD", line)
    old_rule = match_obj.group(2)
    new_rule = match_obj.group(1)
    return old_rule, new_rule


def is_deprecate_warning(line):
    return re.search(
        "Use Rule name",
        line) is not None

def main():
    if len(sys.argv) != 3:
        raise ValueError('Script requires two arguments.')
    ruleset_file = open(sys.argv[1], 'r').readlines()
    warning_file = open(sys.argv[2], 'r')
    for line in warning_file:
        print(".", end="")
        if is_deprecate_warning(line):
            print("+", end="")
            old_string, new_string = get_change_rule(line)
            print(f"{old_string}|{new_string}")
            for line_number in range(len(ruleset_file)):
                ruleset_file[line_number] = ruleset_file[line_number].replace(old_string, new_string)

    for line in ruleset_file:
        print(line)


if __name__ == "__main__":
    main()
