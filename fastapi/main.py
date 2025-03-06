from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from diffusers import DiffusionPipeline
import torch
from io import BytesIO
from PIL import Image
import base64

app = FastAPI()

try:
    pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
    pipe = pipe.to("mps")
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    raise HTTPException(status_code=500, detail=f"Error loading model: {e}")

class TextRequest(BaseModel):
    prompt: str

@app.post("/generate_image/")
async def generate_image(request: TextRequest):
    try:
        prompt = request.prompt
        images = pipe(prompt=prompt).images[0]

        buffered = BytesIO()
        images.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")

        img_html = f'<img src="data:image/png;base64,{img_base64}" alt="Generated Image">'
        
        return {"image_html": img_html}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

