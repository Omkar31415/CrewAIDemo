# CrewAIDemo

```
conda create -p venv python==3.10 -y
```

```
conda activate venv\
```

```
pip install -r requirements.txt
```

Make sure to add your OPENAI_API_KEY and OPENAI_MODEL_NAME in .env file

```
python crew.py
```

- For PineCone Demo for Hybrid search
Make sure to add your HF_TOKEN and PINECONE_API_KEY in .env file
```
pip install -r Pinecone_demo\requirements.txt
```

- For Neo4j Demo for Graph search with cypher query 
Make sure to add your NEO4J_USERNAME, NEO4J_PASSWORD, GROQ_API_KEY and NEO4J_URI in .env file
create new env for this with python==3.12.0
```
pip install -r Neo4j_Demo\requirements.txt
```