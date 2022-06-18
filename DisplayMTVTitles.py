import json
from pathlib import Path, PureWindowsPath


MTVPath = Path(
    "C:/Users/Brice/source/repos/LearningPy/LearningPy/utils/vvpop/MTVTitles.json"
)
# Convert path to Windows format
winpath = PureWindowsPath(MTVPath)

print(winpath)
# prints "source_data\text_files\raw_data.txt"

my_str = open(winpath).read()
val1 = json.loads(my_str)


for key in val1:
    print("--------------------\n" + key + "\n--------------------")
    for k in val1[key]:  # f'{s1}{s2:>10}'
        print(f'{k["Title"]:<40}{k["DiscType"]:<10}{k["DigitalCopy"]:<15}')
jjjj: int = 123456789
print(
    f"{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}",
    end="",
)
print(
    f"{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}",
    end="",
)
# print(f"{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}{jjjj}")

#        for j in k:
#            print(j)
