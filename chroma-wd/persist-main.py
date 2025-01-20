import chromadb
chroma_client = chromadb.PersistentClient()


collection = chroma_client.get_or_create_collection(name="my_collection")

# one-time op
collection.upsert(
    documents=[
        "this is a mango fruit",
        "this is an apple fruit",
    ],
    ids=["id1", "id2"],
)

results = collection.query(
    query_texts=["kashmir apple"],
    n_results=2,
)

print(results)

