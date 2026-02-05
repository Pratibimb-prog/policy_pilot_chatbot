import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_huggingface import HuggingFacePipeline
from config.settings import MAX_NEW_TOKENS, TEMPERATURE, LLM_MODEL_ID

def get_llm():
    tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL_ID)

    model = AutoModelForCausalLM.from_pretrained(
        LLM_MODEL_ID,
        torch_dtype=torch.float16,
        device_map="auto",            
        load_in_4bit=True,             
        offload_folder="offload",      
        offload_state_dict=True
    )

    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=MAX_NEW_TOKENS,
        temperature=TEMPERATURE,
        do_sample=True,
        return_full_text=False
    )

    return HuggingFacePipeline(pipeline=pipe)
