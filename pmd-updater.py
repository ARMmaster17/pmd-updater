import sys
import re

rulesetFile = None
warningFile = None

def getRulesetFileHandle(path):
    return open(path, 'r')

def getWarningFileHandle(path):
    wFile = open(path, 'r')
    return wFile.readlines()

def parseArguments():
    if len(sys.argv) < 1:
        raise ValueError('Missing argument rulesetFilePath.')
    rulesetFile = getRulesetFileHandle(sys.argv[1])
    if len(sys.argv) >= 2:
        warningFile = getWarningFileHandle(sys.argv[2])
    else:
        warningFile = getWarningFileHandle('warnings.txt')

def performRulePathChange(line):
    if (re.search("*Use Rule name * instead of the deprecated Rule name *\. PMD * will remove support for this deprecated Rule name usage\.", line) == None):
        return
    matchObj = re.search("Use Rule name (.*) instead of the deprecated Rule name (.*)\.", line)
    oldRule = matchObj.group(2)
    newRule = matchObj.group(1)

def main():
    parseArguments()
    for line in warningFile:
        performRulePathChange(line)

if __name__ == "__main__":
    main()