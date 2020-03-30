import json
from collections import OrderedDict


def build_command(json_file):
    return json.dumps(clean(json.loads(json_file, object_pairs_hook=OrderedDict)))


def clean(x):
    if type(x) is int or type(x) is float:
        return 0
    elif type(x) is str:
        return ""
    elif type(x) is list:
        return []
    elif type(x) is OrderedDict:
        res = OrderedDict()
        for k, v in x.items():
            res[k] = clean(v)
        return res


print(build_command("""
{
    "version": "0.1.0",
    "command": "c:python",
    "args": ["app.py"],
    "problemMatcher": {
        "fileLocation": ["relative", "${workspaceRoot}"],
        "pattern": {
            "regexp": "^(.*)+s$",
            "message": 1
        }
    }
}
"""))
