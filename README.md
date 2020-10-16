# PMD-Updater
Resolves warnings such as the following from PMD:
```
[WARNING] Use Rule name category/java/errorprone.xml/EmptyInitializer instead of the deprecated Rule name rulesets/java/empty.xml/EmptyInitializer. PMD 7.0.0 will remove support for this deprecated Rule name usage.
```

# Requirements
- Tested with Python 3.8. Others may work.

# Usage
1. Run `git clone https://github.com/ARMmaster17/pmd-updater`
2. Dump a copy of the compiler output with the deprecated rule warnings such as the one at the top of this README. Filename does not matter.
3. Place a copy of your ruleset.xml file in the cloned directory.
4. Run `pmd-updater ruleset.xml warnings.txt` replacing **warnings.txt** with the name of your compiler output dump.
5. Copy ruleset.xml back to your original project directory.
