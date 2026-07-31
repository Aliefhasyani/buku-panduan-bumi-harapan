<script setup lang="ts">
// KKN Guide - Modern Clean Redesign
import { ref } from 'vue'

const emit = defineEmits(['navigate'])

const listProker = [
  {
    nama: 'Rocket Stove',
    slug: 'rocket-stove',
    icon: '🔥',
    desc: 'Tungku biomassa hemat energi dengan efisiensi pembakaran tinggi.',
    color: 'orange',
  },
  {
    nama: 'Pengelolaan Sampah',
    slug: 'sosialisasi-sampah',
    icon: '♻️',
    desc: 'Sosialisasi dan workshop pengelolaan sampah rumah tangga.',
    color: 'teal',
  },
  {
    nama: 'Budidaya Maggot BSF',
    slug: 'maggot-bsf',
    icon: '🐛',
    desc: 'Biokonversi sampah organik menjadi pakan ternak melalui larva BSF.',
    color: 'lime',
  },
  {
    nama: 'Eco-Brick',
    slug: 'ecobrick',
    icon: '🧱',
    desc: 'Mengolah sampah plastik menjadi material bangunan ramah lingkungan.',
    color: 'sky',
  },
  {
    nama: 'Green House TOGA',
    slug: 'green-house-toga',
    icon: '🌿',
    desc: 'Budidaya tanaman obat keluarga dalam rumah kaca mini.',
    color: 'emerald',
  },
  {
    nama: 'Platform Digital',
    slug: 'platform-digital',
    icon: '💻',
    desc: 'Digitalisasi informasi desa melalui platform web interaktif.',
    color: 'violet',
  },
  {
    nama: 'Biopori',
    slug: 'biopori',
    icon: '🕳️',
    desc: 'Lubang resapan biopori untuk pengelolaan air dan kompos alami.',
    color: 'amber',
  },
  {
    nama: 'Peta Spasial (GIS)',
    slug: 'peta-gis',
    icon: '🗺️',
    desc: 'Pemetaan mitigasi bencana berbasis Geographic Information System.',
    color: 'rose',
  },
]

const colorMap: Record<string, { bg: string; border: string; text: string; hoverBorder: string; hoverShadow: string; iconBg: string; iconBorder: string; tag: string }> = {
  orange:  { bg: 'bg-orange-50/50',  border: 'border-orange-100/60',  text: 'text-orange-700',  hoverBorder: 'hover:border-orange-200',  hoverShadow: 'hover:shadow-orange-100/50',  iconBg: 'bg-orange-100',  iconBorder: 'border-orange-200', tag: 'bg-orange-100 text-orange-700' },
  teal:    { bg: 'bg-teal-50/50',    border: 'border-teal-100/60',    text: 'text-teal-700',    hoverBorder: 'hover:border-teal-200',    hoverShadow: 'hover:shadow-teal-100/50',    iconBg: 'bg-teal-100',    iconBorder: 'border-teal-200',   tag: 'bg-teal-100 text-teal-700'   },
  lime:    { bg: 'bg-lime-50/50',    border: 'border-lime-100/60',    text: 'text-lime-700',    hoverBorder: 'hover:border-lime-200',    hoverShadow: 'hover:shadow-lime-100/50',    iconBg: 'bg-lime-100',    iconBorder: 'border-lime-200',   tag: 'bg-lime-100 text-lime-700'   },
  sky:     { bg: 'bg-sky-50/50',     border: 'border-sky-100/60',     text: 'text-sky-700',     hoverBorder: 'hover:border-sky-200',     hoverShadow: 'hover:shadow-sky-100/50',     iconBg: 'bg-sky-100',     iconBorder: 'border-sky-200',    tag: 'bg-sky-100 text-sky-700'    },
  emerald: { bg: 'bg-emerald-50/50', border: 'border-emerald-100/60', text: 'text-emerald-700', hoverBorder: 'hover:border-emerald-200', hoverShadow: 'hover:shadow-emerald-100/50', iconBg: 'bg-emerald-100', iconBorder: 'border-emerald-200',tag: 'bg-emerald-100 text-emerald-700'},
  violet:  { bg: 'bg-violet-50/50',  border: 'border-violet-100/60',  text: 'text-violet-700',  hoverBorder: 'hover:border-violet-200',  hoverShadow: 'hover:shadow-violet-100/50',  iconBg: 'bg-violet-100',  iconBorder: 'border-violet-200', tag: 'bg-violet-100 text-violet-700'},
  amber:   { bg: 'bg-amber-50/50',   border: 'border-amber-100/60',   text: 'text-amber-700',   hoverBorder: 'hover:border-amber-200',   hoverShadow: 'hover:shadow-amber-100/50',   iconBg: 'bg-amber-100',   iconBorder: 'border-amber-200',  tag: 'bg-amber-100 text-amber-700'  },
  rose:    { bg: 'bg-rose-50/50',    border: 'border-rose-100/60',    text: 'text-rose-700',    hoverBorder: 'hover:border-rose-200',    hoverShadow: 'hover:shadow-rose-100/50',    iconBg: 'bg-rose-100',    iconBorder: 'border-rose-200',   tag: 'bg-rose-100 text-rose-700'   },
}

const stats = [
  { value: '288', unit: 'Jam', label: 'Durasi Proker Minimal', desc: 'Total jam kerja efektif yang wajib dipenuhi selama masa KKN.' },
  { value: '3', unit: 'Bab', label: 'Struktur Laporan', desc: 'Sistematika baku LPPM: Analisis, Rencana, dan Evaluasi.' },
  { value: '1×', unit: 'Hari', label: 'Pengisian Logbook', desc: 'Wajib diisi setiap akhir kegiatan untuk validasi harian.' },
]

const stages = [
  {
    num: '01',
    title: 'Observasi & Proposal',
    desc: 'Identifikasi masalah lokasi, susun matriks rencana kerja, dan ajukan persetujuan DPL serta Kepala Desa.',
    tags: ['Survei', 'Matriks', 'Persetujuan'],
  },
  {
    num: '02',
    title: 'Pelaksanaan & Logbook',
    desc: 'Eksekusi program sesuai target jam kerja, dokumentasikan kegiatan, dan isi logbook secara berkala.',
    tags: ['Eksekusi', 'Dokumentasi', 'Presensi'],
  },
  {
    num: '03',
    title: 'Penyusunan Laporan',
    desc: 'Susun laporan akhir dengan analisis hasil, evaluasi kendala, dan lampiran bukti fisik luaran.',
    tags: ['Analisis', 'Evaluasi', 'Lampiran'],
  },
]

const chapters = [
  {
    title: 'Bagian Awal',
    items: ['Halaman Judul', 'Halaman Pengesahan (DPL & Kades)', 'Kata Pengantar', 'Daftar Isi'],
  },
  {
    title: 'Bagian Inti',
    items: ['Bab I — Analisis Situasi & Masalah', 'Bab II — Rencana & Realisasi Proker', 'Bab III — Pembahasan & Evaluasi'],
  },
  {
    title: 'Bagian Penutup & Lampiran',
    items: ['Kesimpulan & Saran', 'Logbook Fisik', 'Foto Kegiatan (Before/After)', 'Daftar Presensi'],
  },
]

const formatSpec = [
  { label: 'Font', value: 'Times New Roman, 12 pt' },
  { label: 'Judul Bab', value: '14 pt Bold' },
  { label: 'Spasi', value: '1.5 Lines' },
  { label: 'Margin Kiri', value: '4 cm' },
  { label: 'Margin Lainnya', value: '3 cm' },
  { label: 'Kertas', value: 'A4 (210 × 297 mm)' },
]

const activeStage = ref<number | null>(null)
</script>

<template>
  <div class="min-h-screen bg-white text-slate-800 font-sans selection:bg-emerald-100 selection:text-emerald-900">

    <!-- Navbar -->


    <!-- Hero -->
    <section id="beranda" class="relative pt-20 pb-28 px-6 overflow-hidden">
      <div class="absolute inset-0 -z-10">
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-emerald-50 rounded-full blur-3xl opacity-60"></div>
      </div>

      <div class="max-w-3xl mx-auto text-center">
        <span class="inline-block text-xs font-semibold text-emerald-700 bg-emerald-50 border border-emerald-100 px-4 py-1.5 rounded-full mb-6 tracking-wide uppercase">
          Bumi Harapan · 2026
        </span>
        <h1 class="text-5xl sm:text-6xl font-bold tracking-tight text-slate-900 leading-[1.1] mb-6">
          Panduan Program Kerja <br>
          <span class="text-emerald-600">Individu Mahasiswa KKN</span>
        </h1>
        <p class="text-lg text-slate-500 max-w-xl mx-auto leading-relaxed mb-12">
          Regulasi, sistematika laporan, manajemen logbook, dan template berkas resmi untuk kelancaran pilar program individu Anda.
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 max-w-2xl mx-auto">
          <div v-for="(s, i) in stats" :key="i" class="group bg-white border border-slate-100 rounded-2xl p-5 text-left hover:border-emerald-200 hover:shadow-lg hover:shadow-emerald-50 transition-all duration-300">
            <div class="flex items-baseline gap-1 mb-2">
              <span class="text-3xl font-bold text-slate-900">{{ s.value }}</span>
              <span class="text-sm font-semibold text-emerald-600">{{ s.unit }}</span>
            </div>
            <div class="text-sm font-semibold text-slate-700 mb-1">{{ s.label }}</div>
            <div class="text-xs text-slate-400 leading-relaxed">{{ s.desc }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Pilih Program Kerja -->
    <section id="pilih-proker" class="py-24 px-6 bg-gradient-to-b from-white via-emerald-50/30 to-white">
      <div class="max-w-6xl mx-auto">
        <div class="text-center mb-16">
          <span class="inline-block text-xs font-semibold text-emerald-700 bg-emerald-50 border border-emerald-100 px-4 py-1.5 rounded-full mb-5 tracking-wide uppercase">
            8 Program Individu
          </span>
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4">Pilih Program Kerja Anda</h2>
          <p class="text-slate-500 leading-relaxed max-w-xl mx-auto">Klik salah satu program di bawah untuk langsung membaca panduan lengkapnya.</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          <button
            v-for="(proker, idx) in listProker"
            :key="proker.slug"
            @click="emit('navigate', proker.slug)"
            class="group relative bg-white rounded-2xl p-6 border text-left cursor-pointer transition-all duration-300 hover:shadow-xl hover:-translate-y-1"
            :class="[colorMap[proker.color].border, colorMap[proker.color].hoverBorder, colorMap[proker.color].hoverShadow]"
          >
            <!-- Number badge -->
            <span class="absolute top-4 right-4 text-4xl font-bold text-slate-100/80 select-none transition-colors duration-300 group-hover:text-slate-200/60">
              {{ String(idx + 1).padStart(2, '0') }}
            </span>

            <!-- Icon -->
            <div
              class="w-12 h-12 rounded-xl flex items-center justify-center text-2xl mb-5 border transition-transform duration-300 group-hover:scale-110"
              :class="[colorMap[proker.color].iconBg, colorMap[proker.color].iconBorder]"
            >
              {{ proker.icon }}
            </div>

            <!-- Title -->
            <h3 class="text-base font-bold text-slate-900 mb-2 group-hover:text-slate-800 transition-colors duration-200">
              {{ proker.nama }}
            </h3>

            <!-- Description -->
            <p class="text-sm text-slate-400 leading-relaxed mb-4">
              {{ proker.desc }}
            </p>

            <!-- Arrow indicator -->
            <div
              class="inline-flex items-center gap-1.5 text-xs font-semibold transition-all duration-200 opacity-0 translate-x-0 group-hover:opacity-100 group-hover:translate-x-1"
              :class="colorMap[proker.color].text"
            >
              Baca Panduan
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </div>
          </button>
        </div>
      </div>
    </section>

    <!-- Tahapan -->
    <section id="tahapan" class="py-24 bg-slate-50/50">
      <div class="max-w-6xl mx-auto px-6">
        <div class="max-w-xl mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4">Tahapan Utama</h2>
          <p class="text-slate-500 leading-relaxed">Alur kerja wajib dari awal penerjunan hingga penarikan. Klik setiap tahap untuk melihat detail.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div 
            v-for="(stage, i) in stages" 
            :key="i"
            @mouseenter="activeStage = i"
            @mouseleave="activeStage = null"
            class="relative bg-white rounded-2xl p-8 border border-slate-100 cursor-default transition-all duration-300"
            :class="activeStage === i ? 'shadow-xl shadow-slate-200/50 -translate-y-1 border-emerald-100' : 'hover:shadow-lg hover:border-slate-200'"
          >
            <span class="absolute top-6 right-6 text-5xl font-bold text-slate-100 select-none">{{ stage.num }}</span>
            <div class="relative">
              <div class="w-10 h-10 bg-emerald-50 text-emerald-600 rounded-xl flex items-center justify-center font-bold text-sm mb-5 border border-emerald-100">
                {{ stage.num }}
              </div>
              <h3 class="text-lg font-bold text-slate-900 mb-3">{{ stage.title }}</h3>
              <p class="text-sm text-slate-500 leading-relaxed mb-5">{{ stage.desc }}</p>
              <div class="flex flex-wrap gap-2">
                <span v-for="tag in stage.tags" :key="tag" class="text-xs font-medium text-slate-500 bg-slate-100 px-2.5 py-1 rounded-md">
                  {{ tag }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Sistematika -->
    <section id="sistematika" class="py-24 px-6">
      <div class="max-w-6xl mx-auto">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">

          <!-- Left: Chapters -->
          <div>
            <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4">Sistematika Laporan</h2>
            <p class="text-slate-500 leading-relaxed mb-10">Struktur baku LPPM untuk memastikan proses validasi nilai berjalan lancar.</p>

            <div class="space-y-6">
              <div v-for="(ch, i) in chapters" :key="i" class="flex gap-4">
                <div class="flex-shrink-0 w-8 h-8 bg-emerald-100 text-emerald-700 rounded-full flex items-center justify-center text-xs font-bold mt-0.5">
                  {{ i + 1 }}
                </div>
                <div>
                  <h4 class="font-semibold text-slate-900 mb-2">{{ ch.title }}</h4>
                  <ul class="space-y-1.5">
                    <li v-for="item in ch.items" :key="item" class="text-sm text-slate-500 flex items-start gap-2">
                      <span class="w-1 h-1 bg-emerald-400 rounded-full mt-2 flex-shrink-0"></span>
                      {{ item }}
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- Right: Format Card -->
          <div class="lg:sticky lg:top-24">
            <div class="bg-white border border-slate-100 rounded-2xl overflow-hidden shadow-sm">
              <div class="bg-slate-900 text-white px-6 py-4 flex items-center justify-between">
                <span class="text-sm font-semibold tracking-wide">Format Standar</span>
                <span class="text-xs bg-white/10 px-2 py-1 rounded text-slate-300">A4</span>
              </div>
              <div class="p-6">
                <div class="space-y-0">
                  <div v-for="(spec, i) in formatSpec" :key="i" class="flex items-center justify-between py-3.5 border-b border-slate-50 last:border-0">
                    <span class="text-sm text-slate-500">{{ spec.label }}</span>
                    <span class="text-sm font-semibold text-slate-800 text-right">{{ spec.value }}</span>
                  </div>
                </div>
              </div>
              <div class="bg-slate-50 px-6 py-4 border-t border-slate-100">
                <p class="text-xs text-slate-400 leading-relaxed">
                  Pastikan seluruh berkas menggunakan format di atas. Penyimpangan dapat menyebabkan penolakan validasi.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>


    <!-- Footer -->
    <footer class="border-t border-slate-100 py-10 px-6">
      <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-2">
          <div class="w-6 h-6 bg-emerald-500 rounded-md flex items-center justify-center">
            <svg class="w-3 h-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25" />
            </svg>
          </div>
          <span class="text-sm font-semibold text-slate-700">KKN Guide</span>
        </div>
        <p class="text-xs text-slate-400">© 2026 KKNT </p>
      </div>
    </footer>
  </div>
</template>

