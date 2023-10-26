def konversi(minggu=0, hari=0, jam=0, menit=0):
    total_menit = (minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit
    return total_menit

data = ["0 minggu 1 hari 0 jam 0 menit", 
        "1 minggu 0 hari 0 jam 0 menit", 
        "0 minggu 0 hari 1 jam 0 menit"]

outputData = []
filteredData = []

for waktu in data:
    waktu_split = list(filter(str.isdigit, waktu.split()))
    filteredData.append(waktu_split)
    
    minggu = int(waktu_split[0])
    hari = int(waktu_split[1])
    jam = int(waktu_split[2])
    menit = int(waktu_split[3])
    
    outputData.append(konversi(minggu, hari, jam, menit))

print("Output Data =", outputData)
print("Filtered Data =", filteredData)