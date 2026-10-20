"""Generate five deterministic, no-API content drafts for @editbyhs6.

These are structured starter drafts, not live research or verified religious rulings.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

TOPICS = [
    {
        "pillar": "Refleksi kehidupan dan nilai Islami",
        "topic": "Saat doa terasa belum dijawab",
        "audience": "Dewasa muda yang sedang menunggu kepastian",
        "angle": "Menemani proses tanpa menjanjikan hasil tertentu",
        "hook": "Pernah merasa doamu belum menemukan jawaban?",
        "message": "Tidak semua hal harus selesai hari ini. Kamu boleh terus berusaha, berdoa, dan memberi ruang bagi dirimu untuk menjalani proses dengan sabar.",
        "visual": "Karakter virtual perempuan berhijab di dekat jendela saat hujan, cahaya sinematik lembut, ekspresi tenang, tanpa teks dalam gambar.",
        "religious_claim": False,
    },
    {
        "pillar": "Refleksi kehidupan dan nilai Islami",
        "topic": "Berhenti membandingkan perjalanan",
        "audience": "Penonton yang merasa tertinggal dari teman sebaya",
        "angle": "Mengubah perbandingan menjadi fokus pada langkah kecil",
        "hook": "Kamu tidak terlambat hanya karena orang lain lebih dulu sampai.",
        "message": "Setiap orang punya keadaan dan tanggung jawab yang berbeda. Alih-alih mengukur hidup dari pencapaian orang lain, pilih satu langkah baik yang bisa kamu lakukan hari ini.",
        "visual": "Karakter virtual perempuan berhijab berjalan pelan di trotoar saat golden hour, cinematic wide shot, suasana reflektif.",
        "religious_claim": False,
    },
    {
        "pillar": "Storytelling sinematik",
        "topic": "Pesan untuk diri yang kelelahan",
        "audience": "Orang yang sedang kewalahan dengan rutinitas",
        "angle": "Validasi emosi dan ajakan beristirahat dengan sehat",
        "hook": "Untuk kamu yang terlihat kuat, tapi diam-diam lelah.",
        "message": "Kamu tidak harus membuktikan kekuatanmu setiap saat. Ambil jeda, tarik napas, dan lanjutkan satu hal kecil ketika kamu sudah siap. Istirahat bukan berarti menyerah.",
        "visual": "Karakter virtual perempuan berhijab duduk di bangku taman menjelang senja, close-up tangan dan wajah, tone hangat.",
        "religious_claim": False,
    },
    {
        "pillar": "Refleksi kehidupan dan nilai Islami",
        "topic": "Memulai lagi setelah melakukan kesalahan",
        "audience": "Penonton yang merasa kecewa pada dirinya sendiri",
        "angle": "Tanggung jawab tanpa mengunci diri dalam rasa bersalah",
        "hook": "Satu kesalahan tidak harus menjadi akhir ceritamu.",
        "message": "Akui apa yang perlu diperbaiki, minta maaf bila ada yang terluka, lalu pilih tindakan yang lebih baik. Kamu tidak bisa mengubah kemarin, tetapi kamu bisa menentukan langkah berikutnya.",
        "visual": "Karakter virtual perempuan berhijab menulis jurnal di meja dekat cahaya pagi, cinematic close-up, natural light.",
        "religious_claim": False,
    },
    {
        "pillar": "Storytelling sinematik",
        "topic": "Kebaikan kecil yang tidak terlihat",
        "audience": "Penonton yang merasa usahanya tidak dihargai",
        "angle": "Menghargai tindakan baik tanpa mengejar pengakuan",
        "hook": "Tidak semua kebaikan harus disaksikan banyak orang.",
        "message": "Ada hal baik yang tetap berarti meski tidak mendapat tepuk tangan. Lakukan kebaikan dengan niat yang jernih, tetap jaga batas diri, dan jangan jadikan pengakuan sebagai satu-satunya ukuran.",
        "visual": "Karakter virtual perempuan berhijab membantu merapikan buku di ruang komunitas, candid cinematic shot, soft daylight.",
        "religious_claim": False,
    },
    {
        "pillar": "Doa, ayat, dan edukasi spiritual",
        "topic": "Membuat ruang tenang untuk berdoa",
        "audience": "Penonton yang ingin membangun rutinitas spiritual sederhana",
        "angle": "Kebiasaan personal yang realistis, tanpa klaim dalil",
        "hook": "Kalau pikiranmu ramai, mulai dari satu menit yang tenang.",
        "message": "Sisihkan waktu sejenak, jauhkan distraksi, dan sampaikan doamu dengan jujur. Ini adalah ajakan membangun kebiasaan personal—bukan janji bahwa semua masalah akan langsung selesai.",
        "visual": "Karakter virtual perempuan berhijab di sudut ruangan sederhana sebelum matahari terbit, suasana hening dan sinematik.",
        "religious_claim": False,
    },
    {
        "pillar": "Refleksi kehidupan dan nilai Islami",
        "topic": "Menjaga hati saat menerima kritik",
        "audience": "Dewasa muda yang sedang menghadapi komentar negatif",
        "angle": "Memilah masukan yang berguna dari komentar yang merendahkan",
        "hook": "Tidak semua komentar harus kamu bawa pulang ke hati.",
        "message": "Dengarkan masukan yang spesifik dan bisa membantumu bertumbuh. Untuk kata-kata yang hanya merendahkan, kamu boleh menjaga jarak. Evaluasi diri tanpa kehilangan harga diri.",
        "visual": "Karakter virtual perempuan berhijab menatap pantulan di jendela kereta, city lights bokeh, cinematic.",
        "religious_claim": False,
    },
    {
        "pillar": "Storytelling sinematik",
        "topic": "Satu langkah kecil hari ini",
        "audience": "Penonton yang kesulitan memulai tujuan besar",
        "angle": "Memecah target menjadi tindakan kecil",
        "hook": "Kalau semuanya terasa berat, kecilkan langkahnya—bukan harapanmu.",
        "message": "Pilih satu hal yang realistis untuk diselesaikan hari ini. Tidak harus sempurna dan tidak harus besar. Kemajuan sering dimulai saat kita berhenti menunggu suasana ideal.",
        "visual": "Karakter virtual perempuan berhijab membuka tirai kamar saat pagi, cahaya masuk perlahan, hopeful cinematic look.",
        "religious_claim": False,
    },
    {
        "pillar": "Refleksi kehidupan dan nilai Islami",
        "topic": "Belajar memaafkan tanpa mengabaikan batas",
        "audience": "Penonton yang sedang memulihkan diri dari konflik",
        "angle": "Membedakan memaafkan dengan membiarkan perlakuan buruk berulang",
        "hook": "Memaafkan tidak selalu berarti kembali seperti dulu.",
        "message": "Kamu bisa memilih melepaskan dendam sambil tetap menetapkan batas yang sehat. Pemulihan punya waktunya sendiri, dan keselamatan serta ketenanganmu tetap penting.",
        "visual": "Karakter virtual perempuan berhijab berjalan menjauh dari lorong menuju taman terbuka, soft backlight, cinematic.",
        "religious_claim": False,
    },
    {
        "pillar": "Doa, ayat, dan edukasi spiritual",
        "topic": "Syukur yang sederhana",
        "audience": "Penonton yang ingin lebih sadar pada hal kecil sehari-hari",
        "angle": "Latihan refleksi personal tanpa mengutip teks agama",
        "hook": "Sebelum hari ini selesai, sebutkan satu hal yang masih kamu syukuri.",
        "message": "Mungkin hari ini tidak berjalan sempurna. Coba ingat satu hal kecil yang membantumu bertahan—waktu istirahat, percakapan baik, atau kesempatan untuk mencoba lagi. Refleksi ini tidak meniadakan kesulitan yang kamu alami.",
        "visual": "Karakter virtual perempuan berhijab memegang secangkir teh dekat jendela pagi, detail tangan, warm cinematic light.",
        "religious_claim": False,
    },
]

def build_content(topic: dict, number: int, date_label: str) -> dict:
    content_id = f"HS6-{date_label}-{number:02d}"
    voiceover = (
        f"{topic['hook']}\n\n{topic['message']}\n\n"
        "Simpan video ini jika kamu ingin mengingatnya lagi, dan bagikan kepada seseorang yang mungkin membutuhkannya."
    )
    return {
        "content_id": content_id,
        "status": "DRAF — perlu review editorial manusia",
        "purpose": "Membangun kedekatan emosional dan mendorong refleksi yang sehat",
        "pillar": topic["pillar"],
        "audience": topic["audience"],
        "angle": topic["angle"],
        "hook": topic["hook"],
        "voiceover": voiceover,
        "estimated_duration": "30–45 detik (sesuaikan tempo VO)",
        "storyboard": [
            {"time": "0–3 dtk", "visual": topic["visual"], "on_screen_text": topic["hook"]},
            {"time": "3–15 dtk", "visual": "Medium shot karakter, gerakan kamera perlahan, beri ruang untuk subtitle.", "on_screen_text": topic["message"][:90]},
            {"time": "15–35 dtk", "visual": "Cutaway suasana pendukung; pertahankan identitas karakter dan palet warna.", "on_screen_text": "Jalani satu langkah kecil hari ini."},
            {"time": "35–45 dtk", "visual": "Close-up tenang, fade out perlahan.", "on_screen_text": "Simpan • Renungkan • Bagikan"},
        ],
        "visual_prompt": topic["visual"] + " Konsisten dengan karakter virtual perempuan berhijab milik brand; tidak menyerupai figur nyata; tanpa logo pihak ketiga.",
        "subtitle": voiceover,
        "title": topic["topic"] + " | Refleksi Singkat",
        "caption": topic["message"] + "\n\nApa satu hal yang ingin kamu ingat hari ini?",
        "keywords": ["refleksi diri", "Islamic cinematic reflection", "self reminder", topic["topic"].lower()],
        "hashtags": ["#EditByHS6", "#RefleksiDiri", "#PengingatDiri", "#IslamicReflection", "#ReelsIndonesia"],
        "cta": "Simpan untuk pengingat, lalu bagikan dengan orang yang kamu pedulikan.",
        "platform_adaptation": {
            "TikTok": "Hook langsung di 1–2 detik pertama; subtitle besar dan pacing dinamis.",
            "Facebook Reels": "Narasi emosional jelas; caption kontekstual dan mudah dibagikan.",
            "Instagram Reels": "Visual konsisten, cover dengan 3–5 kata, caption reflektif.",
            "YouTube Shorts": "Judul spesifik, pembuka langsung ke inti, payoff sebelum akhir.",
        },
        "editorial_checks": {
            "religious_accuracy": "Tidak ada ayat/hadis yang dikutip. Jika ditambahkan saat revisi, wajib verifikasi sumber dan konteks.",
            "originality": "Draf dibuat dari template internal; periksa kemiripan sebelum publikasi.",
            "asset_rights": "Gunakan aset buatan sendiri atau berlisensi; cek lisensi musik, font, dan visual.",
            "monetization": "Hindari klaim absolut, konten repetitif massal, dan aset yang tidak memiliki hak penggunaan.",
            "editorial_review": "Wajib cek alur, bahasa, konsistensi karakter, dan akurasi sebelum dipublikasikan.",
        },
        "performance_hypothesis": "Hipotesis: hook yang relevan dan subtitle terbaca dapat membantu retensi; belum ada data performa yang membuktikan hipotesis ini.",
        "metrics": ["retensi 3 detik", "rata-rata durasi tonton", "persentase selesai", "simpan", "bagikan", "komentar berkualitas"],
        "research_note": "Generator tanpa API tidak melakukan riset tren/web langsung. Jangan menyebut topik ini sedang tren.",
    }

def main() -> None:
    today = datetime.now(timezone.utc).astimezone().date()
    date_label = today.strftime("%Y%m%d")
    # Rotate through the topic bank by day to avoid the same five topics each day.
    day_index = today.toordinal()
    start = (day_index * 5) % len(TOPICS)
    chosen = [TOPICS[(start + offset) % len(TOPICS)] for offset in range(5)]
    output_dir = Path("output/daily")
    output_dir.mkdir(parents=True, exist_ok=True)
    package = {
        "brand": "@editbyhs6",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "generation_mode": "deterministic_no_api_template",
        "editorial_status": "DRAFTS_FOR_HUMAN_REVIEW",
        "note": "Bukan hasil riset langsung dan bukan persetujuan editorial. Verifikasi semua klaim agama sebelum publikasi.",
        "contents": [build_content(topic, i + 1, date_label) for i, topic in enumerate(chosen)],
    }
    json_path = output_dir / f"{date_label}-five-content-pack.json"
    md_path = output_dir / f"{date_label}-five-content-pack.md"
    json_path.write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    sections = [
        f"# Paket 5 Konten Harian — @editbyhs6 ({date_label})",
        "",
        "> Status: DRAF. Generator ini tidak memakai API dan tidak melakukan riset tren langsung. Review manusia wajib sebelum publikasi.",
        "",
    ]
    for item in package["contents"]:
        sections.extend([
            f"## {item['content_id']} — {item['title']}",
            f"**Status:** {item['status']}",
            f"**Pilar:** {item['pillar']}  ",
            f"**Audiens:** {item['audience']}  ",
            f"**Angle:** {item['angle']}",
            "",
            f"### Hook\n{item['hook']}",
            f"### Voice-over\n{item['voiceover']}",
            f"### Storyboard\n" + "\n".join(
                f"- **{scene['time']}** — {scene['visual']}\n  - Teks layar: {scene['on_screen_text']}"
                for scene in item["storyboard"]
            ),
            f"### Prompt visual\n{item['visual_prompt']}",
            f"### Caption\n{item['caption']}",
            f"**Judul:** {item['title']}  ",
            f"**Kata kunci:** {', '.join(item['keywords'])}  ",
            f"**Hashtag:** {' '.join(item['hashtags'])}  ",
            f"**CTA:** {item['cta']}",
            "### Adaptasi platform",
            *[f"- **{platform}:** {notes}" for platform, notes in item["platform_adaptation"].items()],
            "### Editorial & evaluasi",
            *[f"- **{key}:** {value}" for key, value in item["editorial_checks"].items()],
            f"- **Hipotesis performa:** {item['performance_hypothesis']}",
            f"- **Metrik:** {', '.join(item['metrics'])}",
            f"- **Catatan riset:** {item['research_note']}",
            "",
        ])
    md_path.write_text("\n".join(sections) + "\n", encoding="utf-8")
    print(f"Generated {len(package['contents'])} draft contents: {md_path} and {json_path}")

if __name__ == "__main__":
    main()
