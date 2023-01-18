from os import getenv

TOKEN = getenv("TOKEN", None)
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority")
