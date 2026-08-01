<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits(['navigate'])
const activeStep = ref<number | null>(null)

const steps = [
  {
    num: '01', title: 'Prinsip 3R Harian',
    desc: 'Terapkan gaya hidup minim sampah dengan mengutamakan pengurangan di sumbernya (rumah tangga).',
    details: [
      'Reduce: Biasakan membawa kantong belanja berbahan kain saat ke pasar untuk menekan penggunaan plastik.',
      'Reuse: Gunakan kembali wadah plastik atau kaca bekas selai/sirup untuk penyimpanan bumbu dapur.',
      'Recycle: Kumpulkan dan sumbangkan sampah kertas atau plastik botol ke pengepul atau bank sampah.'
    ],
    icon: '♻️', tags: ['Reduce', 'Reuse', 'Recycle'],
  },
  {
    num: '02', title: 'Kategori Tempat Sampah',
    desc: 'Biasakan membuang sampah sesuai dengan jenis dan warnanya untuk memudahkan proses daur ulang.',
    details: [
      'Warna Hijau (Organik): Khusus untuk sisa sayur, kulit buah, tulang ikan, nasi basi, dan dedaunan.',
      'Warna Kuning (Anorganik): Khusus untuk botol plastik minuman, kaleng susu, kertas, dan kardus.',
      'Warna Merah (B3/Residu): Khusus limbah berbahaya seperti popok bayi, baterai, dan wadah racun nyamuk.'
    ],
    icon: '🗑️', tags: ['Hijau', 'Kuning', 'Merah'],
  },
  {
    num: '03', title: 'Ember Komposter',
    desc: 'Ubah sampah organik dapur menjadi pupuk cair atau padat menggunakan ember komposter mandiri.',
    details: [
      'Siapkan ember bekas berventilasi; cacah sampah organik dapur menjadi ukuran lebih kecil.',
      'Semprotkan cairan bioaktivator (seperti EM4 yang dilarutkan air) untuk mempercepat pembusukan.',
      'Tutup ember rapat-rapat dan biarkan berfermentasi selama 3-4 minggu hingga menjadi kompos siap pakai.'
    ],
    icon: '🪣', tags: ['Cacah', 'EM4', '3-4 Minggu'],
  },
]

const strategiList = [
  { title: 'Bank Sampah', desc: 'Penjemputan terintegrasi DLH Parepare.', icon: '🏦' },
  { title: 'Edaran RT/RW', desc: 'Wajib tempat sampah pilah di Dasawisma.', icon: '📋' },
  { title: 'Monitoring', desc: 'Pengawasan saat Jumat Bersih.', icon: '👀' },
]
</script>

<template>
  <div class="min-h-screen bg-white text-slate-800 font-sans selection:bg-blue-100 selection:text-blue-900">
    <section class="relative pt-20 pb-28 px-6 overflow-hidden">
      <div class="absolute inset-0 -z-10">
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-blue-50 rounded-full blur-3xl opacity-60"></div>
      </div>
      <div class="max-w-3xl mx-auto">
        <button @click="emit('navigate', 'home')" class="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-blue-600 transition-colors duration-200 mb-10 group">
          <svg class="w-4 h-4 transition-transform duration-200 group-hover:-translate-x-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" /></svg>
          Kembali ke Beranda
        </button>
        <span class="inline-block text-xs font-semibold text-blue-700 bg-blue-50 border border-blue-100 px-4 py-1.5 rounded-full mb-6 tracking-wide uppercase">Proker #02 · Lingkungan</span>
        <h1 class="text-5xl sm:text-6xl font-bold tracking-tight text-slate-900 leading-[1.1] mb-6">Sosialisasi & <br><span class="text-blue-600">Pengelolaan Sampah</span></h1>
        <p class="text-lg text-slate-500 max-w-xl leading-relaxed mb-6">
          Program ini berfokus pada edukasi intensif dan praktik langsung pengelolaan sampah yang dimulai dari skala rumah tangga terkecil. Dengan menerapkan prinsip 3R (Reduce, Reuse, Recycle), masyarakat diajak untuk secara proaktif memilah sampah organik dan anorganik dari sumbernya. Selain menjaga kebersihan lingkungan, langkah preventif ini ditujukan untuk memutus rantai penumpukan sampah di tempat pembuangan akhir serta mencegah risiko banjir akibat penyumbatan saluran air di area permukiman.
        </p>
        <p class="text-base text-slate-500 max-w-xl leading-relaxed mb-4"><strong class="text-slate-700">Tujuan & Sasaran:</strong> Mencegah banjir, kurangi sampah TPA. Sasaran: Warga Bumi Harapan.</p>
        <p class="text-base text-slate-500 max-w-xl leading-relaxed mb-10"><strong class="text-slate-700">Manfaat:</strong> Lingkungan bersih, bebas genangan, bernilai ekonomi.</p>
        <div class="flex flex-wrap gap-3">
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full"><span>♻️</span> 3R</div>
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full"><span>🏘️</span> Skala Rumah Tangga</div>
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full"><span>🌍</span> Cegah Banjir</div>
        </div>
      </div>
    </section>
    <section class="py-24 bg-slate-50/50">
      <div class="max-w-6xl mx-auto px-6">
        <div class="max-w-xl mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4">Sistem Pemilahan & Pengomposan</h2>
          <p class="text-slate-500 leading-relaxed">Prinsip pemilahan 3R harian, kategori tempat sampah, dan cara pembuatan kompos mandiri.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(item, i) in steps" :key="item.num" @mouseenter="activeStep = i" @mouseleave="activeStep = null"
            class="relative bg-white rounded-2xl p-8 border border-slate-100 cursor-default transition-all duration-300"
            :class="activeStep === i ? 'shadow-xl shadow-slate-200/50 -translate-y-1 border-blue-100' : 'hover:shadow-lg hover:border-slate-200'">
            <span class="absolute top-6 right-6 text-5xl font-bold text-slate-100 select-none">{{ item.num }}</span>
            <div class="relative">
              <div class="w-10 h-10 bg-blue-50 text-blue-600 rounded-xl flex items-center justify-center font-bold text-sm mb-5 border border-blue-100">{{ item.num }}</div>
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
          <p class="text-slate-500 leading-relaxed">Mekanisme agar pengelolaan sampah terus berlangsung secara mandiri pasca-KKN.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(strat, idx) in strategiList" :key="idx"
            class="bg-white rounded-2xl p-8 border border-slate-100 hover:border-blue-100 hover:shadow-xl hover:shadow-slate-200/50 hover:-translate-y-1 transition-all duration-300">
            <div class="w-12 h-12 bg-blue-50 rounded-xl flex items-center justify-center text-2xl mb-6 border border-blue-100">{{ strat.icon }}</div>
            <h3 class="text-lg font-bold text-slate-900 mb-3">{{ strat.title }}</h3>
            <p class="text-sm text-slate-500 leading-relaxed">{{ strat.desc }}</p>
          </div>
        </div>
      </div>
    </section>
    <section class="pb-16 px-6">
      <div class="max-w-6xl mx-auto flex justify-center">
        <button @click="emit('navigate', 'home')" class="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-blue-600 transition-colors duration-200 group">
          <svg class="w-4 h-4 transition-transform duration-200 group-hover:-translate-x-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" /></svg>
          Kembali ke Beranda
        </button>
      </div>
    </section>
  </div>
</template>


