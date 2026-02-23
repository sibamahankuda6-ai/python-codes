marks={
    "siba":45,
    "hari":83
}
# print(marks.keys())
# print(marks.values())
# print(marks.items())
marks.update({"siba":444})
print(marks)
print(marks.get("siba2"))# none
print(marks["siba2"])#returns error