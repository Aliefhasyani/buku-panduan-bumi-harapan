<script setup lang="ts">
import { ref } from 'vue'

// State untuk accordion FAQ
const openIndex = ref<number | null>(0)

const toggleFaq = (index: number) => {
  openIndex.value = openIndex.value === index ? null : index
}

// Daftar FAQ
const faqList = [
  {
    pertanyaan: 'Berapa lama KKN ini berlangsung?',
    jawaban: 'KKN ini berlangsung selama 45 hari penuh di lokasi penerjunan, mencakup tahap observasi, eksekusi program kerja individu dan kelompok, hingga penyusunan laporan akhir.'
  },
  {
    pertanyaan: 'Apa tematik dari KKN periode ini?',
    jawaban: 'Tematik KKN periode ini berfokus pada Perubahan Iklim (Climate Change). Seluruh program kerja yang disusun diharapkan berorientasi pada mitigasi, adaptasi lingkungan, serta edukasi keberlanjutan bagi masyarakat lokal.'
  },
  {
    pertanyaan: 'Bagaimana pembagian proporsi jam kerja program individu?',
    jawaban: 'Mahasiswa wajib memenuhi akumulasi jam kerja efektif sesuai regulasi LPPM yang terbagi dalam program kerja utama tematik perubahan iklim serta program pendukung.'
  },
  {
    pertanyaan: 'Kepada siapa proposal dan laporan individu diserahkan?',
    jawaban: 'Dokumen proposal dan laporan akhir individu wajib disetujui dan ditandatangani oleh Dosen Pembimbing Lapangan (DPL) serta Kepala Desa setempat sebelum diunggah ke portal LPPM.'
  }
]
</script>

<template>
  <div class="scroll-smooth">
    <!-- FAQ SECTION (Tanpa Navbar karena sudah dipanggil di App.vue) -->
    <section id="faq" class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <!-- Header -->
      <div class="text-center mb-12">
        <span class="bg-emerald-100 text-emerald-700 text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider">
          Informasi Umum
        </span>
        <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 mt-3 tracking-tight">
          Frequently Asked Questions (FAQ)
        </h1>
        <p class="mt-3 text-slate-600 max-w-xl mx-auto text-sm sm:text-base">
          Temukan jawaban atas pertanyaan umum seputar durasi, tematik, dan ketentuan pelaksanaan KKN.
        </p>
      </div>

      <!-- Accordion FAQ -->
      <div class="space-y-4">
        <div 
          v-for="(item, index) in faqList" 
          :key="index"
          class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden transition-all duration-200"
        >
          <button 
            @click="toggleFaq(index)"
            class="w-full text-left px-6 py-5 flex justify-between items-center space-x-4 focus:outline-none hover:bg-slate-50/80 transition"
          >
            <span class="font-semibold text-slate-900 text-base sm:text-lg">
              {{ item.pertanyaan }}
            </span>
            <span 
              class="flex-shrink-0 w-8 h-8 rounded-full bg-emerald-50 text-emerald-600 flex items-center justify-center font-bold text-lg transform transition-transform duration-200"
              :class="{ 'rotate-180 bg-emerald-600 text-white': openIndex === index }"
            >
              ↓
            </span>
          </button>

          <!-- Jawaban Expansion -->
          <div 
            v-show="openIndex === index" 
            class="px-6 pb-6 pt-1 text-slate-600 text-sm sm:text-base leading-relaxed border-t border-slate-100 bg-slate-50/50"
          >
            {{ item.jawaban }}
          </div>
        </div>
      </div>

      <!-- Callout Bantuan -->
      <div class="mt-12 bg-emerald-50 border border-emerald-200 rounded-2xl p-6 text-center">
        <h3 class="text-base font-bold text-emerald-900">Punya Pertanyaan Lain?</h3>
        <p class="text-xs sm:text-sm text-emerald-700 mt-1">
          Jika pertanyaan Anda belum terjawab, silakan berkonsultasi dengan Koordinator Desa atau DPL masing-masing.
        </p>
      </div>
    </section>

    <!-- FOOTER -->
    <footer class="bg-slate-900 text-slate-400 py-8 border-t border-slate-800 text-center text-sm mt-12">
      <div class="max-w-7xl mx-auto px-4">
        <p>© 2026 Lembaga Penelitian dan Pengabdian kepada Masyarakat (LPPM). All rights reserved.</p>
        <p class="mt-1 text-xs text-slate-500">KKN Tematik Perubahan Iklim — 45 Hari Pelaksanaan.</p>
      </div>
    </footer>
  </div>
</template>

