import os

from pathlib import Path
path = Path(os.path.abspath(__file__)).parent.parent
print(path)




os.path.join(BASE_DIR, 'templates')