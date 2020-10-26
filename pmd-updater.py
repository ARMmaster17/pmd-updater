import sys
import re
import os


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
        raise ValueError('Script requires two arguments. Ex: "./pmd-updater.py [ruleset file path] [pmd console output dump]"')
    os.rename(sys.argv[1], f"{sys.argv[1]}.old")
    ruleset_file = open(f"{sys.argv[1]}.old", 'r').readlines()
    warning_file = open(sys.argv[2], 'r')
    for line in warning_file:
        if is_deprecate_warning(line):
            old_string, new_string = get_change_rule(line)
            for line_number in range(len(ruleset_file)):
                ruleset_file[line_number] = ruleset_file[line_number].replace(old_string, new_string)
    open(sys.argv[1], 'w').writelines(ruleset_file)


if __name__ == "__main__":
    main()
