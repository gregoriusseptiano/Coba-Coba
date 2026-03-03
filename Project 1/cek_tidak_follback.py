import json

# ===========================================
# 📂 NAMA FILE (pastikan di folder yang sama)
# ===========================================
followers_file = "followers_1.json"
following_file = "following.json"

# ===========================================
# 📥 BACA DATA FOLLOWERS
# ===========================================
with open(followers_file, "r", encoding="utf-8") as f:
    followers_data = json.load(f)

followers = set()
for item in followers_data:
    if "string_list_data" in item:
        followers.add(item["string_list_data"][0]["value"])

# ===========================================
# 📥 BACA DATA FOLLOWING
# ===========================================
with open(following_file, "r", encoding="utf-8") as f:
    following_data = json.load(f)

following = set()
for item in following_data:
    if "string_list_data" in item:
        following.add(item["string_list_data"][0]["value"])

# ===========================================
# 🔍 CARI YANG TIDAK FOLLOWBACK (AKUN YANG KAMU FOLLOW TAPI MEREKA TIDAK FOLLOW KAMU)
# ===========================================
tidak_follback = sorted(list(following - followers))

# ===========================================
# 💾 SIMPAN KE FILE HASIL
# ===========================================
hasil = {
    "total_followers": len(followers),
    "total_following": len(following),
    "tidak_follback_count": len(tidak_follback),
    "tidak_follback": tidak_follback
}

output_file = "akun_tidak_follback.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(hasil, f, indent=2, ensure_ascii=False)

# ===========================================
# 📊 TAMPILKAN HASIL DI TERMINAL
# ===========================================
print("✅ Proses selesai!")
print(f"📄 Hasil disimpan di: {output_file}")
print(f"👥 Total Followers : {len(followers)}")
print(f"👤 Total Following : {len(following)}")
print(f"🚫 Tidak Follback  : {len(tidak_follback)} akun")

if len(tidak_follback) > 0:
    print("\nContoh akun yang tidak follback kamu:")
    for akun in tidak_follback[:15]:
        print("-", akun)
else:
    print("\nSemua akun sudah follback kamu 😄")
