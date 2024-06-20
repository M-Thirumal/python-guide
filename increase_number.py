import re

file_path = '/Users/thirumal/git/icms-api/src/main/java/com/enkindle/persistence/dao/ResolutionApplicantDetailDao.java'

with open(file_path, 'r') as file:
    lines = file.readlines()

incremented_lines = []
for line in lines:
    incremented_line = re.sub(r'\b(\d+)\b', lambda x: str(int(x.group()) + 1), line)
    incremented_lines.append(incremented_line)

with open(file_path, 'w') as file:
    file.writelines(incremented_lines)