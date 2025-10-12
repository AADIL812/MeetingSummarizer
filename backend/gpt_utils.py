from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def analyze_meeting(transcript):
   
    
    prompt = f"""
    Analyze the following meeting transcript and perform these tasks:
    1. Summarize the key points.
    2. List all action items, assigning each to a person if mentioned.
    3. Identify all decisions that were made.
    4. Generate a concise follow-up email to all participants.

    Transcript:
    "{transcript}"

    Output:
    """

    
    inputs = tokenizer(prompt, return_tensors="pt", max_length=2048, truncation=True)

   
    output_sequences = model.generate(
        input_ids=inputs["input_ids"],
        max_length=1024,  
        num_beams=4,
        early_stopping=True
    )
    response_text = tokenizer.decode(output_sequences[0], skip_special_tokens=True)

    return response_text