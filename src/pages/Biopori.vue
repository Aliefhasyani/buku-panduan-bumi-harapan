<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits(['navigate'])

const activeStep = ref<number | null>(null)

const steps = [
  {
    num: '01',
    title: 'Pembuatan Lubang Tanah',
    desc: 'Buat lubang silindris tegak lurus (vertikal) ke dalam tanah berdiameter 10 cm dengan kedalaman 80–100 cm.',
    details: [
      'Gunakan bor tanah manual atau mesin untuk mempermudah pengerjaan.',
      'Pilih lokasi di area resapan air, sekitar pepohonan, atau jalur air hujan.',
      'Jaga jarak antar lubang minimal 50-100 cm agar struktur tanah tetap kuat.'
    ],
    icon: '🕳️',
    tags: ['Bor Tanah', 'Ø 10 cm', '80–100 cm'],
  },
  {
    num: '02',
    title: 'Pemasangan Pipa PVC',
    desc: 'Masukkan pipa PVC berlubang sebagai penahan agar dinding tanah tidak longsor.',
    details: [
      'Gunakan pipa PVC ukuran 10 cm yang telah dilubangi kecil-kecil di sekelilingnya.',
      'Pasang penutup dop yang juga berlubang di bagian atas pipa.',
      'Pastikan posisi penutup rata dengan permukaan tanah untuk menghindari tersandung.'
    ],
    icon: '🛠️',
    tags: ['PVC Ø 10', 'Dop Berlubang', 'Struktur'],
  },
  {
    num: '03',
    title: 'Pengisian Sampah Organik',
    desc: 'Isi lubang dengan sampah organik rumah tangga atau sisa tanaman secara bertahap.',
    details: [
      'Masukkan sisa makanan, kulit buah, atau sayuran yang belum dimasak.',
      'Tambahkan daun kering atau ranting kecil untuk menjaga sirkulasi udara.',
      'Hindari memasukkan sampah plastik, kaca, atau bahan anorganik lainnya.'
    ],
    icon: '🍂',
    tags: ['Sisa Makanan', 'Kulit Buah', 'Daun Kering'],
  },
  {
    num: '04',
    title: 'Panen Kompos & Perawatan',
    desc: 'Lakukan perawatan rutin dan panen kompos setelah proses pembusukan selesai.',
    details: [
      'Tunggu sekitar 2–3 bulan hingga sampah organik terurai sepenuhnya.',
      'Angkat kompos menggunakan alat pengait atau bor tanah, lalu gunakan untuk tanaman.',
      'Isi kembali lubang yang sudah kosong dengan sampah organik baru.'
    ],
    icon: '♻️',
    tags: ['2–3 Bulan', 'Kompos', 'Isi Ulang'],
  },
]

const strategiList = [
  {
    title: 'Gerakan 1 Rumah 2 Biopori',
    desc: 'Mendorong dan memfasilitasi setiap kepala keluarga untuk membuat minimal 2 lubang resapan biopori di area pekarangan rumah masing-masing.',
    icon: '🏡',
  },
  {
    title: 'Pengisian Organik Rutin',
    desc: 'Mengedukasi masyarakat secara aktif untuk memilah sampah dapur harian dan mengisikannya secara berkala ke lubang biopori mandiri.',
    icon: '🗑️',
  },
  {
    title: 'Gotong Royong & Pemantauan',
    desc: 'Pembersihan dan pemeliharaan rutin saluran resapan serta lubang biopori warga melalui agenda kerja bakti / Jumat Bersih berkala.',
    icon: '🧹',
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
          Proker #07 · Konservasi Air
        </span>

        <h1 class="text-5xl sm:text-6xl font-bold tracking-tight text-slate-900 leading-[1.1] mb-6">
          Lubang Resapan <br>
          <span class="text-emerald-600">Biopori (LRB)</span>
        </h1>

        <p class="text-lg text-slate-500 max-w-xl leading-relaxed mb-10">
          Lubang silindris vertikal ke dalam tanah yang diisi sampah organik untuk meningkatkan daya resap air hujan serta memproduksi kompos organik di tempat.
        </p>

        <!-- Quick info pills -->
        <div class="flex flex-wrap gap-3">
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full">
            <span>💧</span> Resapan Air
          </div>
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full">
            <span>🌱</span> Kompos Organik
          </div>
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full">
            <span>🌍</span> Cegah Banjir
          </div>
        </div>
      </div>
    </section>

    <!-- Panduan Pembuatan -->
    <section class="py-24 bg-slate-50/50">
      <div class="max-w-6xl mx-auto px-6">
        <div class="max-w-xl mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4">Panduan Pembuatan</h2>
          <p class="text-slate-500 leading-relaxed">Tata cara pembuatan lubang biopori, pemasangan pipa pelindung, pengisian sampah, hingga panen kompos.</p>
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
          <p class="text-slate-500 leading-relaxed">Langkah jangka panjang berbasis partisipasi warga untuk memastikan manfaat lubang biopori terus terjaga.</p>
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


