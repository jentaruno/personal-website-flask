from airtable import airtable

AIRTABLE_API_TOKEN = "patT4pvQjSWrkylsU.86fb9cdce6a8e52fef170526b700c56db931fee32b4640f7dae58fddc648baf3"
AIRTABLE_BASE_ID = "apphTUZp6LxUaKgR2"
AIRTABLE_TABLE_NAMES = ["Digital", "Design", "Traditional"]
ENDPOINT = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/Digital?maxRecords=3&view=Grid%20view"

at = airtable.Airtable(AIRTABLE_BASE_ID, AIRTABLE_API_TOKEN)
