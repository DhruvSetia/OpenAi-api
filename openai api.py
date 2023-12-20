from openai import OpenAI

# Set your OpenAI API key
OpenAI.api_key = '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'

# Create an instance of the OpenAI client
client = OpenAI()

# Rest of your code
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": "Given the following SQL tables, your job is to write queries given a user’s request...\n[truncated for brevity]"
        },
        {
            "role": "user",
            "content": "Write a SQL query which computes the average total order value for all orders on 2023-04-01."
        }
    ],
    temperature=0.7,
    max_tokens=64,
    top_p=1
)
