"""__init__.py

Application starting point
"""

import importlib.metadata

_DISTRIBUTION_METADATA = importlib.metadata.metadata('sistema-indicadores')

print("hello world!")
print("Data:")
for key, val in _DISTRIBUTION_METADATA.items():
    print(f"\t{key}\t= {val}")
