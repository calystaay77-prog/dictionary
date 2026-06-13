dictionary = {"CRINGE": "sesuatu yang aneh atau memalukan", "LOL": "Tanggapan umum terhadap sesuatu yang lucu", "ROFL": "tanggapan terhacap lelucon", "SHEESH": "sedikit ketidaksetujuan"}
word = input("kata yang ingin dicari? ")
if word in dictionary.keys():
    print (dictionary[word])
else:
    print("tidak di dalam kamus")
