import os

project_path = "/Users/gabrielnetto/Documents/Programaciones/PhoenixEcosystem/PhoenixGAMES/HowNotToDie/HowToNotDie/HowToNotDie.xcodeproj/project.pbxproj"

print("Updating relative path inside project.pbxproj...")
with open(project_path, "r", encoding="utf-8") as file:
    content = file.read()

# Replace relative path (ASCII plist format)
if "relativePath = ../PhoenixEngine;" in content:
    content = content.replace("relativePath = ../PhoenixEngine;", "relativePath = ../../../PhoenixEngine;")
    print("Updated project.pbxproj (ASCII form) successfully!")

# Replace relative path (XML plist format)
if "<string>../PhoenixEngine</string>" in content:
    content = content.replace("<string>../PhoenixEngine</string>", "<string>../../../PhoenixEngine</string>")
    print("Updated project.pbxproj (XML form) successfully!")

with open(project_path, "w", encoding="utf-8") as file:
    file.write(content)
