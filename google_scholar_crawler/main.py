from datetime import datetime
import json
import os

from scholarly import scholarly


author = scholarly.search_author_id(os.environ["GOOGLE_SCHOLAR_ID"])
scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
author["updated"] = str(datetime.now())
author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}

print(json.dumps(author, indent=2))
os.makedirs("results", exist_ok=True)

with open("results/gs_data.json", "w", encoding="utf-8") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}

with open("results/gs_data_shieldsio.json", "w", encoding="utf-8") as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
