<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits(['navigate'])
const activeStep = ref<number | null>(null)

const steps = [
  {
    num: '01', title: 'Perawatan Sarana',
    desc: 'Bersihkan atap UV dari debu, atur ventilasi insect net.',
    icon: '🧹', tags: ['Atap UV', 'Ventilasi', 'Insect Net'],
  },
  {
    num: '02', title: 'Penyiraman & Pupuk',
    desc: 'Siram 2x sehari (pagi/sore). Beri kasgot/kompos 2 minggu sekali.',
    icon: '🚿', tags: ['2x Sehari', 'Kasgot', '2 Minggu Sekali'],
  },
  {
    num: '03', title: 'Penggunaan',
    desc: 'Rebus Jahe/Temulawak (imun), Daun Sirih (antiseptik), Lidah Buaya (kulit).',
    icon: '🌿', tags: ['Jahe', 'Sirih', 'Lidah Buaya'],
  },
  {
    num: '04', title: 'Pembibitan',
    desc: 'Warga dapat mengambil bibit/stek untuk ditanam di rumah.',
    icon: '🌱', tags: ['Bibit', 'Stek', 'Rumah'],
  }
]

const strategiList = [
  { title: 'Penanggung Jawab', desc: 'Dikelola Ibu Khadijah & Kader Posyandu.', icon: '👩‍⚕️' },
  { title: 'Sistem Replikasi', desc: 'Warga yang mengambil wajib mengembalikan 1 pot bibit baru.', icon: '🔄' },
  { title: 'Pupuk Kasgot', desc: 'Pasokan pupuk dari program Maggot BSF.', icon: '💩' },
]
</script>

<template>
  <div class="min-h-screen bg-white text-slate-800 font-sans selection:bg-green-100 selection:text-green-900">
    <section class="relative pt-20 pb-28 px-6 overflow-hidden">
      <div class="absolute inset-0 -z-10">
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-green-50 rounded-full blur-3xl opacity-60"></div>
      </div>
      <div class="max-w-3xl mx-auto">
        <button @click="emit('navigate', 'home')" class="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-green-600 transition-colors duration-200 mb-10 group">
          <svg class="w-4 h-4 transition-transform duration-200 group-hover:-translate-x-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" /></svg>
          Kembali ke Beranda
        </button>
        <span class="inline-block text-xs font-semibold text-green-700 bg-green-50 border border-green-100 px-4 py-1.5 rounded-full mb-6 tracking-wide uppercase">Proker #05 · Kesehatan</span>
        <h1 class="text-5xl sm:text-6xl font-bold tracking-tight text-slate-900 leading-[1.1] mb-6">Green House <br><span class="text-green-600">TOGA Adaptif Iklim</span></h1>
        <p class="text-lg text-slate-500 max-w-xl leading-relaxed mb-6">
          Fasilitas Green House TOGA dibangun khusus sebagai sarana perlindungan fisik bagi berbagai jenis varietas Tanaman Obat Keluarga dari paparan cuaca ekstrem dan serangan hama. Berpusat di kawasan rumah tangga percontohan, program adaptif iklim ini ditujukan untuk menciptakan kemandirian penyediaan apotek hidup bagi masyarakat sekitar. Hal ini memungkinkan warga untuk mendapatkan akses pengobatan herbal darurat dan langkah pertolongan pertama secara cepat dan mandiri.
        </p>
        <p class="text-base text-slate-500 max-w-xl leading-relaxed mb-4"><strong class="text-slate-700">Tujuan & Sasaran:</strong> Kesehatam mandiri rumah tangga. Sasaran: Warga Bumi Harapan.</p>
        <p class="text-base text-slate-500 max-w-xl leading-relaxed mb-10"><strong class="text-slate-700">Manfaat:</strong> Obat herbal darurat (flu, batuk, demam) & konservasi hayati.</p>
        <div class="flex flex-wrap gap-3">
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full"><span>🌿</span> Obat Herbal</div>
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full"><span>🛡️</span> Pelindung Cuaca Ekstrem</div>
          <div class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full"><span>🩺</span> Kesehatan Mandiri</div>
        </div>
      </div>
    </section>
    <section class="py-24 bg-slate-50/50">
      <div class="max-w-6xl mx-auto px-6">
        <div class="max-w-xl mb-16">
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4">Panduan Operasional TOGA</h2>
          <p class="text-slate-500 leading-relaxed">Arahan pengelolaan dari perawatan sarana hingga tatacara pembibitan kembali.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div v-for="(item, i) in steps" :key="item.num" @mouseenter="activeStep = i" @mouseleave="activeStep = null"
            class="relative bg-white rounded-2xl p-8 border border-slate-100 cursor-default transition-all duration-300"
            :class="activeStep === i ? 'shadow-xl shadow-slate-200/50 -translate-y-1 border-green-100' : 'hover:shadow-lg hover:border-slate-200'">
            <span class="absolute top-6 right-6 text-5xl font-bold text-slate-100 select-none">{{ item.num }}</span>
            <div class="relative">
              <div class="w-10 h-10 bg-green-50 text-green-600 rounded-xl flex items-center justify-center font-bold text-sm mb-5 border border-green-100">{{ item.num }}</div>
              <h3 class="text-lg font-bold text-slate-900 mb-3 flex items-center gap-2"><span>{{ item.icon }}</span>{{ item.title }}</h3>
              <p class="text-sm text-slate-500 leading-relaxed mb-5">{{ item.desc }}</p>
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
          <p class="text-slate-500 leading-relaxed">Kerangka pengelolaan jangka panjang bersama warga untuk mempertahankan sarana TOGA.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="(strat, idx) in strategiList" :key="idx"
            class="bg-white rounded-2xl p-8 border border-slate-100 hover:border-green-100 hover:shadow-xl hover:shadow-slate-200/50 hover:-translate-y-1 transition-all duration-300">
            <div class="w-12 h-12 bg-green-50 rounded-xl flex items-center justify-center text-2xl mb-6 border border-green-100">{{ strat.icon }}</div>
            <h3 class="text-lg font-bold text-slate-900 mb-3">{{ strat.title }}</h3>
            <p class="text-sm text-slate-500 leading-relaxed">{{ strat.desc }}</p>
          </div>
        </div>
      </div>
    </section>
    <section class="pb-16 px-6">
      <div class="max-w-6xl mx-auto flex justify-center">
        <button @click="emit('navigate', 'home')" class="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-green-600 transition-colors duration-200 group">
          <svg class="w-4 h-4 transition-transform duration-200 group-hover:-translate-x-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7" /></svg>
          Kembali ke Beranda
        </button>
      </div>
    </section>
    <footer class="border-t border-slate-100 py-10 px-6">
      <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-2">
          <div class="w-6 h-6 bg-green-500 rounded-md flex items-center justify-center">
            <svg class="w-3 h-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="3"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25" /></svg>
          </div>
          <span class="text-sm font-semibold text-slate-700">LPPM KKN Guide</span>
        </div>
        <p class="text-xs text-slate-400">© 2026 Lembaga Penelitian dan Pengabdian kepada Masyarakat.</p>
      </div>
    </footer>
  </div>
</template>


