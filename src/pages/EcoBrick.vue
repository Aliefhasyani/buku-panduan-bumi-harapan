<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits(['navigate'])

const activeStep = ref<number | null>(null)

const steps = [
  {
    num: '01',
    title: 'Persiapan Alat & Bahan',
    desc: 'Kumpulkan dan persiapkan seluruh kebutuhan material utama sebelum memulai proses.',
    details: [
      'Siapkan botol plastik bekas ukuran seragam (500ml atau 1.5L) dalam kondisi kering.',
      'Kumpulkan limbah plastik lunak seperti bungkus makanan, kantong kresek, atau kemasan saset.',
      'Sediakan tongkat kayu/bambu berujung tumpul sebagai penumbuk dan timbangan digital.'
    ],
    icon: '🛠️',
    tags: ['Botol Plastik', 'Tongkat', 'Timbangan'],
  },
  {
    num: '02',
    title: 'Pembersihan & Pemotongan',
    desc: 'Pastikan plastik dalam kondisi bersih dan terpotong untuk mencegah pertumbuhan bakteri dan memudahkan pemadatan.',
    details: [
      'Cuci plastik dengan sabun jika kotor atau berminyak, lalu jemur hingga benar-benar kering.',
      'Gunting plastik menjadi potongan kecil-kecil agar dapat mengisi celah botol secara maksimal.',
      'Pisahkan plastik berdasarkan warna jika ingin membuat pola desain pada botol.'
    ],
    icon: '✂️',
    tags: ['Cuci', 'Keringkan', 'Gunting'],
  },
  {
    num: '03',
    title: 'Pemadatan Plastik',
    desc: 'Isi dan padatkan plastik ke dalam botol untuk mencapai kepadatan dan kekuatan struktural.',
    details: [
      'Masukkan plastik lunak berwarna terlebih dahulu di bagian dasar botol.',
      'Tekan kuat plastik menggunakan tongkat penumbuk setiap kali memasukkan segenggam plastik.',
      'Pastikan tidak ada rongga udara. Target berat: botol 1.5L = 330g, botol 500ml = 150g.'
    ],
    icon: '⚖️',
    tags: ['Padat', 'Min. 330g', 'Rapat'],
  },
  {
    num: '04',
    title: 'Pemanfaatan & Assembly',
    desc: 'Rangkai botol-botol Eco-Brick yang telah memenuhi standar menjadi furnitur fungsional.',
    details: [
      'Gunakan lem silikon/kaca atau semen untuk merangkai botol secara permanen.',
      'Susun melingkar atau persegi menjadi tempat duduk, meja kecil, atau pot tanaman.',
      'Pastikan susunan seimbang agar konstruksi kuat menahan beban.'
    ],
    icon: '🪑',
    tags: ['Rangkai', 'Furnitur', 'Pembatas'],
  },
]

const strategiList = [
  {
    title: 'Bank Eco-Brick RT/RW',
    desc: 'Menjadikan Pos RT/RW setempat sebagai pusat pengumpulan dan penimbangan Eco-Brick warga secara terpusat.',
    icon: '🏛️',
  },
  {
    title: 'Integrasi Sekolah & PKK',
    desc: 'Memasukkan modul pembuatan Eco-Brick sebagai materi rutin pada kegiatan ekstrakurikuler sekolah dan program PKK ibu-ibu.',
    icon: '🏫',
  },
  {
    title: 'Lomba Kreativitas Daur Ulang',
    desc: 'Mengarahkan kompetisi berkala untuk kreasi daur ulang guna meningkatkan antusiasme dan partisipasi aktif warga.',
    icon: '🏆',
  },
]
</script>

<template>
  <div class="min-h-screen bg-white text-slate-800 font-sans selection:bg-emerald-100 selection:text-emerald-900">

    <!-- Hero -->
    <section class="relative pt-20 pb-28 px-6 overflow-hidden">
      <div class="absolute inset-0 -z-10">
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-emerald-50 rounded-full blur-3xl opacity-60"></div>
      </div>

      <div class="max-w-3xl mx-auto">
        <!-- Back button -->
        <button
          @click="emit('navigate', 'home')"
          class="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-emerald-600 transition-colors duration-200 mb-10 group"
        >
          <svg class="w-4 h-4 transition-transform duration-200 group-hover:-translate-x-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
          </svg>
          Kembali ke Beranda
        </button>

        <span class="inline-block text-xs font-semibold text-emerald-700 bg-emerald-50 border border-emerald-100 px-4 py-1.5 rounded-full mb-6 tracking-wide uppercase">
          Proker #04 · Lingkungan
        </span>

        <h1 class="text-5xl sm:text-6xl font-bold tracking-tight text-slate-900 leading-[1.1] mb-6">
          Upcycling Plastik <br>
          <span class="text-emerald-600">(Eco-Brick)</span>
        </h1>

        <p class="text-lg text-slate-500 max-w-xl leading-relaxed mb-10">
          Pelatihan pembuatan Eco-Brick dari limbah plastik tak terurai sebagai solusi mandiri pemanfaatan sampah dan pencegahan pencemaran lingkungan.
        </p>

        <!-- Quick info pills -->
        <div class="flex flex-wrap gap-3">
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full">
            <span>🎯</span> Zero Waste
          </div>
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full">
            <span>♻️</span> Daur Ulang Mandiri
          </div>
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full">
            <span>🌍</span> Cegah Pencemaran
          </div>
        </div>
      </div>
    </section>

    <!-- Panduan Pembuatan -->
    <section class="py-24 bg-slate-50/50">
      <div class="max-w-6xl mx-auto px-6">
        <div class="max-w-xl mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4">Panduan Pembuatan</h2>
          <p class="text-slate-500 leading-relaxed">Ikuti 4 tahapan teknis untuk menghasilkan Eco-Brick berkualitas tinggi dan berstandar.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div
            v-for="(item, i) in steps"
            :key="item.num"
            @mouseenter="activeStep = i"
            @mouseleave="activeStep = null"
            class="relative bg-white rounded-2xl p-8 border border-slate-100 cursor-default transition-all duration-300"
            :class="activeStep === i ? 'shadow-xl shadow-slate-200/50 -translate-y-1 border-emerald-100' : 'hover:shadow-lg hover:border-slate-200'"
          >
            <span class="absolute top-6 right-6 text-5xl font-bold text-slate-100 select-none">{{ item.num }}</span>
            <div class="relative">
              <div class="w-10 h-10 bg-emerald-50 text-emerald-600 rounded-xl flex items-center justify-center font-bold text-sm mb-5 border border-emerald-100">
                {{ item.num }}
              </div>
              <h3 class="text-lg font-bold text-slate-900 mb-3 flex items-center gap-2">
                <span>{{ item.icon }}</span>
                {{ item.title }}
              </h3>
              <p class="text-sm text-slate-500 leading-relaxed mb-3">{{ item.desc }}</p>
              <ul v-if="item.details" class="text-sm text-slate-500 leading-relaxed mb-5 list-disc pl-4 space-y-1">
                <li v-for="detail in item.details" :key="detail">{{ detail }}</li>
              </ul>
              <div class="flex flex-wrap gap-2">
                <span v-for="tag in item.tags" :key="tag" class="text-xs font-medium text-slate-500 bg-slate-100 px-2.5 py-1 rounded-md">
                  {{ tag }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Strategi Keberlanjutan -->
    <section class="py-24 px-6">
      <div class="max-w-6xl mx-auto">
        <div class="max-w-xl mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4">Strategi Keberlanjutan</h2>
          <p class="text-slate-500 leading-relaxed">Agar dampak pengelolaan sampah terus berjalan pasca-KKN, disusun 3 pilar keberlanjutan bersama masyarakat.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div
            v-for="(strat, idx) in strategiList"
            :key="idx"
            class="bg-white rounded-2xl p-8 border border-slate-100 hover:border-emerald-100 hover:shadow-xl hover:shadow-slate-200/50 hover:-translate-y-1 transition-all duration-300"
          >
            <div class="w-12 h-12 bg-emerald-50 rounded-xl flex items-center justify-center text-2xl mb-6 border border-emerald-100">
              {{ strat.icon }}
            </div>
            <h3 class="text-lg font-bold text-slate-900 mb-3">{{ strat.title }}</h3>
            <p class="text-sm text-slate-500 leading-relaxed">{{ strat.desc }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Back to Home -->
    <section class="pb-16 px-6">
      <div class="max-w-6xl mx-auto flex justify-center">
        <button
          @click="emit('navigate', 'home')"
          class="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-emerald-600 transition-colors duration-200 group"
        >
          <svg class="w-4 h-4 transition-transform duration-200 group-hover:-translate-x-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
          </svg>
          Kembali ke Beranda
        </button>
      </div>
    </section>
  </div>
</template>


