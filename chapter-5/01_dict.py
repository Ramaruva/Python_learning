marks={
    "haryy":100,
    "shubam":56,
    "rohan":23
}
print(marks)
print(type(marks))
print(marks["haryy"])

# methods
print(marks.items())
print(marks.keys())
marks.update({"haryy":98})
print(marks)
print(marks.get("rohan"))
print(marks.get("heey"))