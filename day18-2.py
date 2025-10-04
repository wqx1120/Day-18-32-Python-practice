content = f"""hello world
this is a test file
hello python logging
"""
with open("sample.txt", "w", encoding = "utf-8") as f:
    f.write(content)