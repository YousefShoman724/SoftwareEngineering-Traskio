import os
import stat

files = ["users.json", "tasks.json"]

for file in files:
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    
    # لو الملف مش موجود، هننشئه
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("[]")
        print(f"✅ Created missing file: {file}")
    
    # إزالة الـ Read-only
    os.chmod(path, stat.S_IWRITE)
    print(f"🔓 File is now writable: {file}")
