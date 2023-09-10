from flask import Flask, jsonify
from utils import at, AIRTABLE_TABLE_NAMES

app = Flask(__name__)

def page(table):
    # TODO: load 5 by 5 otherwise airtable mad
    json_data = at.get(table)
    records = json_data.get("records", [])

    result = []

    for record in records:
        fields = record.get("fields", {})
        title = fields.get("Title", "")
        subtitle = fields.get("Subtitle", "")
        description = fields.get("Description", "")
        image_url = fields.get("Image", [{}])[0].get("thumbnails", {}).get("full", {}).get("url", "")

        item = {
            "title": title,
            "image": image_url,
            "subtitle": subtitle,
            "desc": description
        }

        result.append(item)

    return jsonify(result)


@app.route("/" + AIRTABLE_TABLE_NAMES[0])
def page0():
    return page(AIRTABLE_TABLE_NAMES[0])


@app.route("/" + AIRTABLE_TABLE_NAMES[1])
def page1():
    return page(AIRTABLE_TABLE_NAMES[1])


@app.route("/" + AIRTABLE_TABLE_NAMES[2])
def page2():
    return page(AIRTABLE_TABLE_NAMES[2])

if __name__ == "__main__":
    app.run(debug=True)