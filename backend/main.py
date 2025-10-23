from fastapi import FastAPI, Body
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "HuggingFaceTB/SmolLM2-135M-Instruct"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

app = FastAPI(title="Local Text Generator API")

@app.post("/generate")
def generate_text(
    prompt: str = Body(..., embed=True),
    max_new_tokens: int = 50,
    temperature: float = 0.7,
):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
    )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    generated = text[len(prompt):]

    return {"prompt": prompt, "generated": generated.strip()}
