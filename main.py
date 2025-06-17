from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# السماح لكل المصادر (تعديل لاحقًا للإنتاج)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    text: str

@app.post("/api/generate")
async def generate_video(req: GenerateRequest):
    # هنا يمكنك دمج نموذج الذكاء الاصطناعي أو أي منطق آخر
    text_input = req.text
    fake_video_url = f"https://example.com/videos/fake_video_based_on_{text_input[:10]}.mp4"
    return {"video_url": fake_video_url}