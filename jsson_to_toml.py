import toml

output_file = "./ai_bot_app/.streamlit/secrets.toml"

with open(r"D:\Neeraj\streamlit\news-local-5414b-6683be5831b3.json") as json_file:
    json_text = json_file.read()

config = {"json_key_file": json_text}
toml_config = toml.dumps(config)

with open(output_file, "w") as target:
    target.write(toml_config)