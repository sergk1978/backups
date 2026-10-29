from pathlib import Path

class Size:
    def __init__(self, path):
        self.path = path

    def get_dir_size(self, path):
        total_size = 0
        for file_path in Path(path).rglob('*'):
            if file_path.is_file():
                total_size += file_path.stat().st_size
        return total_size

    def format_size(self):
        size_in_bytes = self.get_dir_size(self.path)
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_in_bytes < 1024:
                return f"{size_in_bytes:.2f} {unit}"
            size_in_bytes /= 1024
    


