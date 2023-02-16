"""test."""

# Pip
from sistema_indicadores import DISTRIBUTION_METADATA

if __name__ == "__main__":
    print("hello world!")
    print("MetaData:")
    for key, val in DISTRIBUTION_METADATA.json.items():
        print(f"\t{key}\t= {val}")
