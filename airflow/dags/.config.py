import json

manifest_data = {
    "fileLocations": [
        {
            "URIs": [
                "s3://BUCKET-NAME/Amazon-Bestseller-Dataset.csv"
            ]
        }
    ],
    "globalUploadSettings": {
        "format": "CSV",
        "delimiter": ",",
        "textqualifier": "\"",
        "containsHeader": "true"
    }
}

manifest_file_path = 'manifest.json'
with open(manifest_file_path, 'w') as f:
    json.dump(manifest_data, f, indent=4)

print(f"Manifest file created at {manifest_file_path}.")
