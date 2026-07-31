import re
import os

replacements = {
    'RocketStove.vue': 'Program kerja Rocket Stove atau Tungku Biomassa ini merupakan inovasi teknologi tepat guna yang dirancang khusus untuk menciptakan efisiensi pembakaran tingkat tinggi. Dengan memanfaatkan sistem aliran udara vertikal (draft), tungku ini secara efektif meminimalisir produksi asap yang mengganggu sekaligus menekan konsumsi penggunaan kayu bakar harian. Ini menjadikannya solusi memasak yang sangat ideal bagi rumah tangga karena tidak hanya ramah lingkungan, namun juga lebih hemat dan menyehatkan.',
    'SosialisasiSampah.vue': 'Program ini berfokus pada edukasi intensif dan praktik langsung pengelolaan sampah yang dimulai dari skala rumah tangga terkecil. Dengan menerapkan prinsip 3R (Reduce, Reuse, Recycle), masyarakat diajak untuk secara proaktif memilah sampah organik dan anorganik dari sumbernya. Selain menjaga kebersihan lingkungan, langkah preventif ini ditujukan untuk memutus rantai penumpukan sampah di tempat pembuangan akhir serta mencegah risiko banjir akibat penyumbatan saluran air di area permukiman.',
    'MaggotBSF.vue': 'Budidaya Maggot Black Soldier Fly (BSF) merupakan sebuah inisiatif biokonversi cerdas yang terbukti sangat ampuh dalam mengurai limbah sisa makanan atau sampah organik basah secara instan. Proses penguraian alami oleh larva ini sangat ramah lingkungan karena tidak menghasilkan emisi gas metana yang berkontribusi pada efek gas rumah kaca. Di samping itu, hasil panen maggot menjadi alternatif pakan ternak berkualitas berprotein tinggi yang bernilai ekonomis bagi warga setempat.',
    'EcoBrick.vue': 'Eco-Brick merupakan program upcycling solutif untuk mengatasi permasalahan limbah plastik sekali pakai yang sulit terurai secara alami oleh tanah. Melalui pelatihan komprehensif, masyarakat diajarkan cara memadatkan potongan sampah plastik murni ke dalam botol bekas hingga menjadi balok bata ramah lingkungan yang kokoh. Hasil akhir dari proses ini kemudian dapat dirangkai dan dimanfaatkan kembali sebagai material furnitur fungsional maupun struktur pembatas taman pekarangan.',
    'GreenHouseToga.vue': 'Fasilitas Green House TOGA dibangun khusus sebagai sarana perlindungan fisik bagi berbagai jenis varietas Tanaman Obat Keluarga dari paparan cuaca ekstrem dan serangan hama. Berpusat di kawasan rumah tangga percontohan, program adaptif iklim ini ditujukan untuk menciptakan kemandirian penyediaan apotek hidup bagi masyarakat sekitar. Hal ini memungkinkan warga untuk mendapatkan akses pengobatan herbal darurat dan langkah pertolongan pertama secara cepat dan mandiri.',
    'PlatformDigital.vue': 'Platform Panduan Digital Integrasi adalah sebuah situs repositori modern dan interaktif yang secara khusus menyimpan seluruh modul teknis, dokumentasi, dan panduan pelaksanaan program kerja KKN. Sistem berbasis web ini didesain agar mudah diakses dari perangkat apapun dan kapan saja, memastikan terjadinya transparansi informasi secara penuh. Tujuan utamanya adalah sebagai fondasi digital agar setiap perangkat kelurahan maupun warga setempat dapat mereplikasi program-program yang telah berjalan secara berkelanjutan.',
    'Biopori.vue': 'Lubang Resapan Biopori (LRB) merupakan sebuah upaya konservasi tanah dan air yang sangat efektif dan mudah diaplikasikan di pekarangan rumah warga. Dengan metode pembuatan lubang silindris secara vertikal dan mengisinya menggunakan sampah organik dapur, tanah di sekitarnya akan mengalami peningkatan daya resap air hujan yang signifikan. Proses alami ini tidak hanya mencegah terjadinya genangan air dan risiko banjir lokal, tetapi sekaligus menghasilkan kompos organik berkualitas untuk menyuburkan tanaman.',
    'PetaGis.vue': 'Pemetaan spasial berbasis GIS (Geographic Information System) ini dirancang sebagai instrumen visual komprehensif untuk memetakan secara detail zona rawan bencana di kelurahan setempat. Peta tematik yang dihasilkan mencakup informasi penting terkait sarana fasilitas mitigasi, lokasi titik kumpul aman, serta rute jalur evakuasi tercepat. Dengan adanya alat bantu tata ruang spasial ini, masyarakat luas dan perangkat kelurahan diharapkan dapat merespon kondisi darurat secara tanggap demi meminimalisir dampak kerugian dan korban jiwa.'
}

for filename, new_text in replacements.items():
    filepath = os.path.join('src', 'pages', filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        pattern = r'<p class="text-base text-slate-500 max-w-xl leading-relaxed mb-4">\s*<strong class="text-slate-700">Penjelasan Proker:</strong>.*?</p>'
        new_tag = f'<p class="text-lg text-slate-500 max-w-xl leading-relaxed mb-6">\n          {new_text}\n        </p>'
        content = re.sub(pattern, new_tag, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
print('Done')
