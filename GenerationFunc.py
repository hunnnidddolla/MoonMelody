from transformers import AutoProcessor, MusicgenForConditionalGeneration
import time
import scipy.io.wavfile
from io import BytesIO
from db import supabase
async def generate_music(prompt: str, filename: str,
                         user_id: str,model_type:str,
                         duration:int):
    if model_type not in ["small", "medium", "large"]:
        model_type = "medium"
    processor = AutoProcessor.from_pretrained(f"facebook/musicgen-{model_type}")
    model = MusicgenForConditionalGeneration.from_pretrained(f"facebook/musicgen-{model_type}")
    inputs = processor(text=[f"{prompt}"],padding=True,return_tensors="pt")
    max_tokens = 256
    max_duration = max_tokens // 50
    if duration > max_duration:
        duration = max_duration
    start = time.time()
    audio_values = model.generate(**inputs, max_new_tokens=duration*50)
    sampling_rate = model.config.audio_encoder.sampling_rate
    with open(f"src/{filename}", 'wb') as f:
        scipy.io.wavfile.write(f, rate=sampling_rate, data=audio_values[0, 0].numpy())
    file_path = f"{user_id}/{filename}"
    if file_path not in supabase.storage.from_("User_generation").list():
        upload_response = supabase.storage.from_("User_generation").upload(file_path,f"src/{filename}")
    else:
        file_path = f"{user_id}/{filename}duplicat"
        upload_response = supabase.storage.from_("User_generation").upload(file_path, f"src/{filename}")
    print(time.time() - start)
    print('Success!')
