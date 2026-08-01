<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits(['navigate'])
const activeStep = ref<number | null>(null)

const steps = [
  {
    num: '01', title: 'Cari Posisi',
    desc: 'Langkah pertama membaca peta adalah mengidentifikasi titik lokasi saat ini secara presisi.',
    details: [
      'Gunakan legenda atau indeks jalan untuk menemukan lokasi RT/RW tempat tinggal Anda.',
      'Jadikan landmark seperti masjid, sekolah, atau kantor kelurahan sebagai titik acuan (patokan).',
      'Pahami orientasi arah mata angin (Utara/Selatan) pada peta untuk memudahkan navigasi.'
    ],
    icon: '📍', tags: ['Lokasi', 'RT/RW', 'Landmark'],
  },
  {
    num: '02', title: 'Zona Risiko',
    desc: 'Pahami tingkatan bahaya pada lingkungan sekitar melalui kode warna yang tertera di peta.',
    details: [
      'Area berwarna Merah menunjukkan zona risiko tinggi yang rawan banjir atau longsor.',
      'Area berwarna Kuning menunjukkan zona waspada dengan risiko bencana tingkat sedang.',
      'Area berwarna Hijau menunjukkan zona aman yang direkomendasikan untuk evakuasi sementara.'
    ],
    icon: '🚦', tags: ['Merah', 'Kuning', 'Hijau'],
  },
  {
    num: '03', title: 'Fasilitas',
    desc: 'Kenali lokasi berbagai sarana prasarana yang mendukung ketahanan lingkungan dan kesehatan.',
    details: [
      'Cari ikon khusus untuk menemukan titik kumpul pengelolaan sampah organik dan anorganik.',
      'Identifikasi lokasi budidaya Maggot BSF, area Green House TOGA, dan sumur resapan.',
      'Ketahui lokasi Ruang Terbuka Hijau (RTH) yang dapat dimanfaatkan saat keadaan darurat.'
    ],
    icon: '🏢', tags: ['Sampah', 'BSF', 'TOGA', 'RTH'],
  },
  {
    num: '04', title: 'Evakuasi',
    desc: 'Pahami prosedur dan jalur keselamatan yang harus dilalui saat terjadi bencana.',
    details: [
      'Identifikasi rute jalur evakuasi tercepat yang ditandai dengan garis dan panah berwarna hijau.',
      'Ikuti arah panah menuju Titik Kumpul Aman terdekat atau Posko Darurat Bencana.',
      'Hindari melewati rute yang bersilangan dengan zona risiko tinggi (area berwarna merah).'
    ],
    icon: '🏃', tags: ['Panah Hijau', 'Titik Kumpul', 'Darurat'],
  }
]

const strategiList = [
  { title: 'Papan Akrilik Outdoor', desc: 'Dipasang permanen di Kelurahan & Pos RW.', icon: '🗺️' },
  { title: 'Integrasi BPBD', desc: 'Penyerahan data shapefile/PDF untuk simulasi.', icon: '🤝' },
  { title: 'Update Spasial', desc: 'File mentah GIS disimpan di platform digital.', icon: '💾' },
]
</script>

<template>
  <div class="min-h-screen bg-white text-slate-800 font-sans selection:bg-rose-100 selection:text-rose-900">
    <section class="relative pt-20 pb-28 px-6 overflow-hidden">
      <div class="absolute inset-0 -z-10">
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-rose-50 rounded-full blur-3xl opacity-60"></div>
      </div>
      <div class="max-w-3xl mx-auto">
        <button @click="emit('navigate', 'home')" class="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-rose-600 transition-colors duration-200 mb-10 group">
          <svg class="w-4 h-4 transition-transform duration-200 group-hover:-translate-x-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" /></svg>
          Kembali ke Beranda
        </button>
        <span class="inline-block text-xs font-semibold text-rose-700 bg-rose-50 border border-rose-100 px-4 py-1.5 rounded-full mb-6 tracking-wide uppercase">Proker #08 · Pemetaan Risiko</span>
        <h1 class="text-5xl sm:text-6xl font-bold tracking-tight text-slate-900 leading-[1.1] mb-6">Peta Spasial <br><span class="text-rose-600">Mitigasi Bencana (GIS)</span></h1>
        <p class="text-lg text-slate-500 max-w-xl leading-relaxed mb-6">
          Pemetaan spasial berbasis GIS (Geographic Information System) ini dirancang sebagai instrumen visual komprehensif untuk memetakan secara detail zona rawan bencana di kelurahan setempat. Peta tematik yang dihasilkan mencakup informasi penting terkait sarana fasilitas mitigasi, lokasi titik kumpul aman, serta rute jalur evakuasi tercepat. Dengan adanya alat bantu tata ruang spasial ini, masyarakat luas dan perangkat kelurahan diharapkan dapat merespon kondisi darurat secara tanggap demi meminimalisir dampak kerugian dan korban jiwa.
        </p>
        <p class="text-base text-slate-500 max-w-xl leading-relaxed mb-4"><strong class="text-slate-700">Tujuan & Sasaran:</strong> Kesiapsiagaan bencana & acuan tata ruang. Sasaran: Warga & Perangkat Kelurahan.</p>
        <p class="text-base text-slate-500 max-w-xl leading-relaxed mb-10"><strong class="text-slate-700">Manfaat:</strong> Evakuasi cepat, minimalisir korban jiwa, dasar kebijakan.</p>
        <div class="flex flex-wrap gap-3">
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full"><span>🗺️</span> Pemetaan Bencana</div>
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full"><span>🏃‍♂️</span> Jalur Evakuasi</div>
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full"><span>📍</span> Titik Kumpul Aman</div>
        </div>
      </div>
    </section>
    <section class="py-24 bg-slate-50/50">
      <div class="max-w-6xl mx-auto px-6">
        <div class="max-w-xl mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4">Panduan Pembacaan Peta</h2>
          <p class="text-slate-500 leading-relaxed">Cara memahami informasi di peta dari lokasi hingga jalur evakuasi.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div v-for="(item, i) in steps" :key="item.num" @mouseenter="activeStep = i" @mouseleave="activeStep = null"
            class="relative bg-white rounded-2xl p-8 border border-slate-100 cursor-default transition-all duration-300"
            :class="activeStep === i ? 'shadow-xl shadow-slate-200/50 -translate-y-1 border-rose-100' : 'hover:shadow-lg hover:border-slate-200'">
            <span class="absolute top-6 right-6 text-5xl font-bold text-slate-100 select-none">{{ item.num }}</span>
            <div class="relative">
              <div class="w-10 h-10 bg-rose-50 text-rose-600 rounded-xl flex items-center justify-center font-bold text-sm mb-5 border border-rose-100">{{ item.num }}</div>
              <h3 class="text-lg font-bold text-slate-900 mb-3 flex items-center gap-2"><span>{{ item.icon }}</span>{{ item.title }}</h3>
              <p class="text-sm text-slate-500 leading-relaxed mb-3">{{ item.desc }}</p>
              <ul v-if="item.details" class="text-sm text-slate-500 leading-relaxed mb-5 list-disc pl-4 space-y-1">
                <li v-for="detail in item.details" :key="detail">{{ detail }}</li>
              </ul>
              <div class="flex flex-wrap gap-2">
                <span v-for="tag in item.tags" :key="tag" class="text-xs font-medium text-slate-500 bg-slate-100 px-2.5 py-1 rounded-md">{{ tag }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="py-24 px-6">
      <div class="max-w-6xl mx-auto">
        <div class="max-w-xl mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4">Strategi Keberlanjutan</h2>
          <p class="text-slate-500 leading-relaxed">Penyediaan sarana dan tata kelola data untuk menjaga relevansi mitigasi bencana.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(strat, idx) in strategiList" :key="idx"
            class="bg-white rounded-2xl p-8 border border-slate-100 hover:border-rose-100 hover:shadow-xl hover:shadow-slate-200/50 hover:-translate-y-1 transition-all duration-300">
            <div class="w-12 h-12 bg-rose-50 rounded-xl flex items-center justify-center text-2xl mb-6 border border-rose-100">{{ strat.icon }}</div>
            <h3 class="text-lg font-bold text-slate-900 mb-3">{{ strat.title }}</h3>
            <p class="text-sm text-slate-500 leading-relaxed">{{ strat.desc }}</p>
          </div>
        </div>
      </div>
    </section>
    <section class="pb-16 px-6">
      <div class="max-w-6xl mx-auto flex justify-center">
        <button @click="emit('navigate', 'home')" class="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-rose-600 transition-colors duration-200 group">
          <svg class="w-4 h-4 transition-transform duration-200 group-hover:-translate-x-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" /></svg>
          Kembali ke Beranda
        </button>
      </div>
    </section>
  </div>
</template>


