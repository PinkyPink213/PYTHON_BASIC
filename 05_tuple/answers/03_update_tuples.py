"""เฉลยบทที่ 3: Update Tuples"""

tools = ("hammer", "rope", "map")

tool_list = list(tools)
tool_list[1] = "torch"
tools = tuple(tool_list)
print(tools)

tool_list = list(tools)
tool_list.append("key")
tools = tuple(tool_list)
print(tools)

tool_list = list(tools)
tool_list.remove("map")
tools = tuple(tool_list)
print(tools)

