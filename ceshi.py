from transformers import AutoModelForCausalLM, AutoTokenizer

model_dir = "/root/autodl-tmp/RoadSafety_Gpt"
# Note: The default behavior now has injection attack prevention off.
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)

model = AutoModelForCausalLM.from_pretrained(
    model_dir,
    device_map="auto",
    trust_remote_code=True
).eval()

response, history = model.chat(tokenizer, "你是谁", history=None)
print(response)
