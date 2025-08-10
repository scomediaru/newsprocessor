import os
import subprocess

def create_newsprocessor_project():
    """Создает структуру проекта NewsProcessor"""
    
    # Основная структура
    dirs = [
        "backend/news_processor/settings",
        "backend/apps/authentication/migrations",
        "backend/apps/projects/migrations", 
        "backend/apps/sources/migrations",
        "backend/apps/processors/migrations",
        "backend/apps/publishers/migrations",
        "frontend/src/components/layout",
        "frontend/src/components/auth",
        "frontend/src/pages",
        "frontend/src/services",
        "frontend/src/hooks",
        "frontend/src/types",
        "frontend/public",
        "nginx",
        "scripts",
    ]
    
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        # Создаем пустой __init__.py в Python папках
        if 'backend' in dir_path and not 'migrations' in dir_path:
            with open(f"{dir_path}/__init__.py", "w") as f:
                pass
    
    print("✅ Структура проекта создана!")
    print("📝 Теперь копируй файлы из нашей беседы")

if __name__ == "__main__":
    create_newsprocessor_project()
