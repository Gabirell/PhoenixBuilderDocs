import os

artifact_dir = "/Users/gabrielnetto/.gemini/antigravity/brain/87be6a90-b465-486e-8b2d-d7a68868d595"

print("Updating paths in local artifacts...")

for f in ["walkthrough.md", "implementation_plan.md"]:
    file_path = os.path.join(artifact_dir, f)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Perform replacements
        if "Phoenix/HowNotToDie" in content:
            content = content.replace("Phoenix/HowNotToDie", "PhoenixEcosystem/PhoenixGAMES/HowNotToDie")
        if "/Phoenix/" in content:
            content = content.replace("/Phoenix/", "/PhoenixEcosystem/")
        if "PhoenixBuilderDocs" in content:
            # Revert any accidental double replace in venv name if it happened
            content = content.replace("PhoenixEcosystemBuilderDocs", "PhoenixBuilderDocs")
            
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Updated artifact: {f}")

print("Artifact path update complete!")
