from fastapi import FastAPI
    from pydantic import BaseModel
    from fastapi.middleware.cors import CORSMiddleware

    app = FastAPI()

    # Ijinkan Website Hostinger mengakses Dapur ini
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], # Nanti ganti "*" dengan domain Hostinger Anda supaya aman
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    class VideoRequest(BaseModel):
        youtube_url: str

    @app.get("/")
    def home():
        return {"message": "Dapur ClipMaster Siap!"}

    @app.post("/process")
    def process_video(request: VideoRequest):
        # DI SINI LOGIKA AI NANTI DITARUH
        # Saat ini kita buat 'pura-pura' dulu untuk ngetes koneksi
        
        print(f"Menerima pesanan untuk URL: {request.youtube_url}")
        
        return {
            "status": "Berhasil Diterima",
            "original_url": request.youtube_url,
            "message": "Halo Bos! Server Python berhasil menerima link ini. Langkah selanjutnya adalah menghubungkan API AI.",
            "viral_score": 95
        }