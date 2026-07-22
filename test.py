import os

print("Current Working Directory:", os.getcwd())
from retriever import retrieve_context

results = retrieve_context(
    "VPN authentication failed"
)

for item in results:

    print("="*80)

    print(item["source"])

    print()

    print(item["text"])