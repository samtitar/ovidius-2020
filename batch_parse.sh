for file in data/unstructured/*
do
    python3 parse_documents.py --document $file
done