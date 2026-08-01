<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits(['navigate'])

const activeStep = ref<number | null>(null)

const steps = [
  {
    num: '01',
    title: 'Penempatan',
    desc: 'Pilih lokasi yang aman dan ideal untuk meletakkan Rocket Stove sebelum dinyalakan.',
    details: [
      'Tempatkan tungku di dapur dengan ventilasi udara yang baik atau di area terbuka.',
      'Gunakan alas yang keras, datar, dan tahan api (seperti plesteran semen atau bata merah).',
      'Bebaskan area sekitar tungku (radius minimal 50 cm) dari benda yang mudah terbakar.'
    ],
    icon: '📍',
    tags: ['Ventilasi', 'Alas Keras', 'Radius 50cm'],
  },
  {
    num: '02',
    title: 'Bahan Bakar',
    desc: 'Siapkan biomassa yang ukurannya pas agar proses pembakaran di dalam ruang bakar efisien.',
    details: [
      'Gunakan ranting pohon kering, potongan papan sisa, atau tempurung kelapa.',
      'Potong kayu bakar menjadi ukuran kecil (diameter sekitar 1-3 cm) agar mudah dimasukkan.',
      'Pastikan seluruh kayu dalam kondisi kering sempurna untuk menghindari asap tebal.'
    ],
    icon: '🪵',
    tags: ['Ranting', 'Papan', 'Tempurung'],
  },
  {
    num: '03',
    title: 'Penyulutan Api',
    desc: 'Mulai proses pembakaran dengan memanfaatkan aliran udara vertikal (efek cerobong/draft).',
    details: [
      'Masukkan bahan pemantik seperti daun kering, kertas bekas, atau sabut ke dasar tungku.',
      'Susun beberapa kayu kecil secara menyilang di atas pemantik agar api mudah merambat.',
      'Nyalakan api dari saluran udara bawah; biarkan prinsip draft menyedot api kuat ke atas.'
    ],
    icon: '🔥',
    tags: ['Pemantik', 'Draft Vertikal', 'Saluran Bawah'],
  },
  {
    num: '04',
    title: 'Pengontrolan',
    desc: 'Lakukan pemeliharaan nyala api selama proses memasak agar suhu tetap konstan.',
    details: [
      'Dorong ujung kayu bakar secara perlahan ke dalam ruang bakar saat mulai memendek.',
      'Jaga agar saluran udara bagian bawah tidak tertutup rapat oleh tumpukan abu tebal.',
      'Segera tambahkan potongan kayu kecil baru jika nyala api mulai terlihat mengecil.'
    ],
    icon: '🎛️',
    tags: ['Dorong Kayu', 'Saluran Udara', 'Kontrol'],
  },
  {
    num: '05',
    title: 'Memasak',
    desc: 'Letakkan peralatan masak dengan benar agar panas api tersalurkan dengan maksimal.',
    details: [
      'Tempatkan panci atau wajan tepat di atas dudukan cerobong (skirt) tungku.',
      'Pastikan masih terdapat celah di sekitar panci agar asap hasil pembakaran bisa keluar.',
      'Gunakan tutup panci selama memasak untuk mempercepat proses pematangan.'
    ],
    icon: '🍳',
    tags: ['Dudukan', 'Cerobong', 'Celah Asap'],
  },
  {
    num: '06',
    title: 'Pemadaman & Perawatan',
    desc: 'Matikan api dengan aman dan bersihkan tungku untuk menjaga keawetan strukturnya.',
    details: [
      'Tarik sisa kayu yang belum habis terbakar keluar, lalu celupkan ujungnya ke dalam air.',
      'Biarkan badan tungku mendingin secara alami di udara terbuka (jangan disiram air).',
      'Buang sisa abu di bagian bawah lorong secara berkala agar sirkulasi udara selalu lancar.'
    ],
    icon: '🧹',
    tags: ['Celup Air', 'Dingin Alami', 'Buang Abu'],
  },
]

const strategiList = [
  {
    title: 'Kader Dapur Hijau',
    desc: 'Pembentukan penanggung jawab Dasawisma.',
    icon: '👩‍🍳',
  },
  {
    title: 'Suplai Mandiri',
    desc: 'Memanfaatkan limbah ranting warga & pertukangan.',
    icon: '🌿',
  },
  {
    title: 'Pemeliharaan',
    desc: 'Pembersihan abu rutin paska-pakai.',
    icon: '🔧',
  },
]
</script>

<template>
  <div class="min-h-screen bg-white text-slate-800 font-sans selection:bg-orange-100 selection:text-orange-900">

    <!-- Hero -->
    <section class="relative pt-20 pb-28 px-6 overflow-hidden">
      <div class="absolute inset-0 -z-10">
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-orange-50 rounded-full blur-3xl opacity-60"></div>
      </div>

      <div class="max-w-3xl mx-auto">
        <!-- Back button -->
        <button
          @click="emit('navigate', 'home')"
          class="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-orange-600 transition-colors duration-200 mb-10 group"
        >
          <svg class="w-4 h-4 transition-transform duration-200 group-hover:-translate-x-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" />
          </svg>
          Kembali ke Beranda
        </button>

        <span class="inline-block text-xs font-semibold text-orange-700 bg-orange-50 border border-orange-100 px-4 py-1.5 rounded-full mb-6 tracking-wide uppercase">
          Proker #01 · Energi Terbarukan
        </span>

        <h1 class="text-5xl sm:text-6xl font-bold tracking-tight text-slate-900 leading-[1.1] mb-6">
          Rocket Stove <br>
          <span class="text-orange-600">(Tungku Biomassa)</span>
        </h1>

        <p class="text-lg text-slate-500 max-w-xl leading-relaxed mb-6">
          Program kerja Rocket Stove atau Tungku Biomassa ini merupakan inovasi teknologi tepat guna yang dirancang khusus untuk menciptakan efisiensi pembakaran tingkat tinggi. Dengan memanfaatkan sistem aliran udara vertikal (draft), tungku ini secara efektif meminimalisir produksi asap yang mengganggu sekaligus menekan konsumsi penggunaan kayu bakar harian. Ini menjadikannya solusi memasak yang sangat ideal bagi rumah tangga karena tidak hanya ramah lingkungan, namun juga lebih hemat dan menyehatkan.
        </p>
        <p class="text-base text-slate-500 max-w-xl leading-relaxed mb-4">
          <strong class="text-slate-700">Tujuan:</strong> Alternatif energi memasak ramah lingkungan & hemat biomassa.
        </p>
        <p class="text-base text-slate-500 max-w-xl leading-relaxed mb-10">
          <strong class="text-slate-700">Manfaat:</strong> Bebas asap berlebih, hemat kayu 50%, dan memasak lebih cepat.
        </p>

        <!-- Quick info pills -->
        <div class="flex flex-wrap gap-3">
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full">
            <span>🔥</span> Efisiensi Tinggi
          </div>
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full">
            <span>💨</span> Bebas Asap
          </div>
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full">
            <span>🌿</span> Hemat Kayu 50%
          </div>
        </div>
      </div>
    </section>

    <!-- Panduan Operasional -->
    <section class="py-24 bg-slate-50/50">
      <div class="max-w-6xl mx-auto px-6">
        <div class="max-w-xl mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4">Panduan Operasional & Penggunaan</h2>
          <p class="text-slate-500 leading-relaxed">Ikuti 6 tahapan dari penempatan tungku hingga pemadaman dan perawatan berkala.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="(item, i) in steps"
            :key="item.num"
            @mouseenter="activeStep = i"
            @mouseleave="activeStep = null"
            class="relative bg-white rounded-2xl p-8 border border-slate-100 cursor-default transition-all duration-300"
            :class="activeStep === i ? 'shadow-xl shadow-slate-200/50 -translate-y-1 border-orange-100' : 'hover:shadow-lg hover:border-slate-200'"
          >
            <span class="absolute top-6 right-6 text-5xl font-bold text-slate-100 select-none">{{ item.num }}</span>
            <div class="relative">
              <div class="w-10 h-10 bg-orange-50 text-orange-600 rounded-xl flex items-center justify-center font-bold text-sm mb-5 border border-orange-100">
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
          <p class="text-slate-500 leading-relaxed">Langkah memastikan penggunaan Rocket Stove tetap berlanjut pasca-KKN.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div
            v-for="(strat, idx) in strategiList"
            :key="idx"
            class="bg-white rounded-2xl p-8 border border-slate-100 hover:border-orange-100 hover:shadow-xl hover:shadow-slate-200/50 hover:-translate-y-1 transition-all duration-300"
          >
            <div class="w-12 h-12 bg-orange-50 rounded-xl flex items-center justify-center text-2xl mb-6 border border-orange-100">
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
          class="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-orange-600 transition-colors duration-200 group"
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


