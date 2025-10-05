import ollama

def generate_sql_from_question(question: str, db_schema: str):
    """
    Takes a user's question and a database schema, then uses a local LLM 
    to generate an SQL query.
    """
    prompt = f"""
    Based on the database schema below, write a single, executable SQL query 
    that answers the following user question.
    
    IMPORTANT: Respond with ONLY the SQL query and nothing else. Do not use markdown.

    ---
    Schema:
    {db_schema}
    ---
    Question: "{question}"
    """

    try:
        print("🤖 Contacting local LLM...")
        # The fix is on the next line: 'message' is now 'messages'
        response = ollama.chat(
            model='llama3',
            messages=[{'role': 'user', 'content': prompt}]
        )
        
        sql_query = response['message']['content'].strip()
        
        # Clean up potential markdown formatting from the LLM's response
        if sql_query.startswith("```sql"):
            sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
            
        return sql_query
    except Exception as e:
        print(f"❌ Error communicating with LLM: {e}")
        return None