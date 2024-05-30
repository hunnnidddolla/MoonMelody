from supabase import create_client, Client

url: str = "https://ttyyxkkcaupshgurulco.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR0eXl4a2tjYXVwc2hndXJ1bGNvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTY0ODQ3ODIsImV4cCI6MjAzMjA2MDc4Mn0.J4pcTTQCgja7zBcSL-4mpwfTG1nT6iMQgqrX9Q1EU8w"

supabase: Client = create_client(url, key)
