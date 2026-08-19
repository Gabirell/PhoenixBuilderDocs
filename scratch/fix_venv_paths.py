import os

docs_root = "/Users/gabrielnetto/Documents/Programaciones/PhoenixEcosystem/PhoenixBuilderDocs"

print("Fixing paths in virtualenv and documentation...")

# Update .venv files
venv_bin_dir = os.path.join(docs_root, ".venv", "bin")
if os.path.exists(venv_bin_dir):
    for f in os.listdir(venv_bin_dir):
        file_path = os.path.join(venv_bin_dir, f)
        if os.path.isfile(file_path) and not os.path.islink(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                if "Programaciones/Phoenix/" in content:
                    content = content.replace("Programaciones/Phoenix/", "Programaciones/PhoenixEcosystem/")
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(content)
                    print(f"Updated venv bin: {f}")
            except Exception as e:
                # Skip binary files
                pass

# Update pyvenv.cfg
cfg_path = os.path.join(docs_root, ".venv", "pyvenv.cfg")
if os.path.exists(cfg_path):
    with open(cfg_path, "r", encoding="utf-8") as file:
        content = file.read()
    if "Programaciones/Phoenix/" in content:
        content = content.replace("Programaciones/Phoenix/", "Programaciones/PhoenixEcosystem/")
        with open(cfg_path, "w", encoding="utf-8") as file:
            file.write(content)
        print("Updated pyvenv.cfg")

# Update AGENTS.md
agents_path = os.path.join(docs_root, "AGENTS.md")
if os.path.exists(agents_path):
    with open(agents_path, "r", encoding="utf-8") as file:
        content = file.read()
    if "Programaciones/Phoenix/" in content:
        content = content.replace("Programaciones/Phoenix/", "Programaciones/PhoenixEcosystem/")
        with open(agents_path, "w", encoding="utf-8") as file:
            file.write(content)
        print("Updated AGENTS.md paths")

print("Venv and Docs paths correction complete!")
