#!/usr/bin/env python3

import json

text = '''
{
    "app.log":3,
    "auth.log":4
}
'''

data = json.loads(text)

print(data)

print(type(data))
