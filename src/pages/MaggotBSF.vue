<script setup lang="ts">
import { ref } from "vue";

const emit = defineEmits(["navigate"]);
const activeStep = ref<number | null>(null);

const steps = [
  {
    num: "01",
    title: "Persiapan Biopond",
    desc: "Siapkan kandang lalat BSF dan biopond sebagai tempat pembesaran larva (maggot).",
    details: [
      "Gunakan wadah plastik atau bak kayu berlapis terpal berukuran minimal 1x1 meter.",
      "Tempatkan biopond di area yang teduh, terhindar dari hujan dan sinar matahari langsung.",
      "Sediakan penutup jaring kelambu untuk mencegah lalat liar bertelur di dalam wadah.",
    ],
    icon: "📦",
    tags: ["Wadah", "Terlindung", "Teduh"],
  },
  {
    num: "02",
    title: "Pemberian Pakan",
    desc: "Berikan sampah organik sebagai sumber makanan utama bagi pertumbuhan maggot.",
    details: [
      "Cacah atau potong sampah sisa makanan rumah tangga agar lebih mudah diurai maggot.",
      "Beri pakan sebanyak 1-2 kali sehari, sesuaikan takaran dengan kepadatan larva di biopond.",
      "Pastikan ketebalan pakan tidak lebih dari 5 cm agar larva di bagian bawah tetap bisa bernapas.",
    ],
    icon: "🥬",
    tags: ["Sampah Organik", "1-2x Sehari", "Dipotong"],
  },
  {
    num: "03",
    title: "Kontrol Kelembapan",
    desc: "Jaga kondisi biopond agar tetap stabil untuk mencegah kematian larva dan timbulnya bau.",
    details: [
      "Pertahankan tingkat kelembapan media pada kisaran 60-70% (tekstur seperti kompos lembap).",
      "Taburkan serbuk gergaji, dedak, atau sekam kering jika media terlalu basah atau berair.",
      "Semprotkan air secukupnya menggunakan semprotan halus jika media terlihat terlalu kering.",
    ],
    icon: "💧",
    tags: ["60-70%", "Dedak/Sekam", "Kontrol"],
  },
  {
    num: "04",
    title: "Panen",
    desc: "Lakukan panen maggot untuk pakan ternak dan panen kasgot sebagai pupuk organik.",
    details: [
      "Panen maggot segar (Fresh Maggot) pada usia 14-21 hari saat larva berukuran maksimal.",
      "Saring sisa pakan yang telah menghitam dan menjadi remah-remah, ini disebut pupuk kasgot.",
      "Sisakan sebagian larva prepupa untuk dibiarkan menjadi lalat BSF agar siklus terus berlanjut.",
    ],
    icon: "🪱",
    tags: ["14-21 Hari", "Maggot", "Kasgot"],
  },
];

const strategiList = [
  {
    title: "Kelompok Pengelola (KPM)",
    desc: "Diserahkan ke peternak/warga lokal.",
    icon: "👥",
  },
  {
    title: "Pasokan Organik",
    desc: "Pasokan rutin dari warung makan & pasar.",
    icon: "🍱",
  },
  {
    title: "Sirkular Ekonomi",
    desc: "Penjualan hasil maggot & kasgot untuk operasional.",
    icon: "💰",
  },
];
</script>

<template>
  <div
    class="min-h-screen bg-white text-slate-800 font-sans selection:bg-teal-100 selection:text-teal-900"
  >
    <section class="relative pt-20 pb-28 px-6 overflow-hidden">
      <div class="absolute inset-0 -z-10">
        <div
          class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-teal-50 rounded-full blur-3xl opacity-60"
        ></div>
      </div>
      <div class="max-w-3xl mx-auto">
        <button
          @click="emit('navigate', 'home')"
          class="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-teal-600 transition-colors duration-200 mb-10 group"
        >
          <svg
            class="w-4 h-4 transition-transform duration-200 group-hover:-translate-x-0.5"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M15 19l-7-7 7-7"
            />
          </svg>
          Kembali ke Beranda
        </button>
        <span
          class="inline-block text-xs font-semibold text-teal-700 bg-teal-50 border border-teal-100 px-4 py-1.5 rounded-full mb-6 tracking-wide uppercase"
          >Proker #03 · Ketahanan Lingkungan</span
        >
        <h1
          class="text-5xl sm:text-6xl font-bold tracking-tight text-slate-900 leading-[1.1] mb-6"
        >
          Budidaya Maggot BSF <br /><span class="text-teal-600"
            >Cerdas Iklim</span
          >
        </h1>
        <p class="text-lg text-slate-500 max-w-xl leading-relaxed mb-6">
          Budidaya Maggot Black Soldier Fly (BSF) merupakan sebuah inisiatif
          biokonversi cerdas yang terbukti sangat ampuh dalam mengurai limbah
          sisa makanan atau sampah organik basah secara instan. Proses
          penguraian alami oleh larva ini sangat ramah lingkungan karena tidak
          menghasilkan emisi gas metana yang berkontribusi pada efek gas rumah
          kaca. Di samping itu, hasil panen maggot menjadi alternatif pakan
          ternak berkualitas berprotein tinggi yang bernilai ekonomis bagi warga
          setempat.
        </p>
        <p class="text-base text-slate-500 max-w-xl leading-relaxed mb-4">
          <strong class="text-slate-700">Tujuan:</strong> Kurangi gas rumah kaca
          & hasilkan pakan ternak protein tinggi.
        </p>
        <p class="text-base text-slate-500 max-w-xl leading-relaxed mb-6">
          <strong class="text-slate-700">Manfaat:</strong> Kurangi sampah 80%,
          pakan murah, pupuk kasgot subur.
        </p>
        <div class="flex flex-wrap gap-4 mb-10">
          <a
            href="/maggot.pdf"
            download="buku-hirisasi-maggot.pdf"
            class="inline-flex items-center gap-2 bg-teal-600 hover:bg-teal-700 text-white font-semibold px-5 py-3 rounded-full shadow-sm transition-all duration-200"
          >
            <svg
              class="w-5 h-5"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 3v12m0 0l-4-4m4 4l4-4M4 16v2a2 2 0 002 2h12a2 2 0 002-2v-2"
              />
            </svg>
            Unduh Buku Hilirisasi Maggot (PDF)
          </a>
          <a
            href="/buku_panduan_saku_kkn_v5.pdf"
            download="buku-panduan-maggot.pdf"
            class="inline-flex items-center gap-2 bg-white hover:bg-slate-50 text-slate-700 font-semibold px-5 py-3 rounded-full border border-slate-200 shadow-sm transition-all duration-200"
          >
            <svg
              class="w-5 h-5 text-slate-500"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 3v12m0 0l-4-4m4 4l4-4M4 16v2a2 2 0 002 2h12a2 2 0 002-2v-2"
              />
            </svg>
            Unduh Buku Panduan (PDF)
          </a>
        </div>
        <div class="flex flex-wrap gap-3">
          <div
            class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full"
          >
            <span>🐛</span> Biokonversi Cepat
          </div>
          <div
            class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full"
          >
            <span>📉</span> Kurangi Metana
          </div>
          <div
            class="flex items-center gap-2 bg-white border border-slate-100 text-slate-600 text-sm font-medium px-4 py-2 rounded-full"
          >
            <span>🐔</span> Pakan Protein Tinggi
          </div>
        </div>
      </div>
    </section>
    <section class="py-24 bg-slate-50/50">
      <div class="max-w-6xl mx-auto px-6">
        <div class="max-w-xl mb-16">
          <h2
            class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4"
          >
            Panduan Pengelolaan Maggot BSF
          </h2>
          <p class="text-slate-500 leading-relaxed">
            Tata cara pengelolaan dari persiapan biopond, pemberian pakan hingga
            panen.
          </p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div
            v-for="(item, i) in steps"
            :key="item.num"
            @mouseenter="activeStep = i"
            @mouseleave="activeStep = null"
            class="relative bg-white rounded-2xl p-8 border border-slate-100 cursor-default transition-all duration-300"
            :class="
              activeStep === i
                ? 'shadow-xl shadow-slate-200/50 -translate-y-1 border-teal-100'
                : 'hover:shadow-lg hover:border-slate-200'
            "
          >
            <span
              class="absolute top-6 right-6 text-5xl font-bold text-slate-100 select-none"
              >{{ item.num }}</span
            >
            <div class="relative">
              <div
                class="w-10 h-10 bg-teal-50 text-teal-600 rounded-xl flex items-center justify-center font-bold text-sm mb-5 border border-teal-100"
              >
                {{ item.num }}
              </div>
              <h3
                class="text-lg font-bold text-slate-900 mb-3 flex items-center gap-2"
              >
                <span>{{ item.icon }}</span
                >{{ item.title }}
              </h3>
              <p class="text-sm text-slate-500 leading-relaxed mb-3">
                {{ item.desc }}
              </p>
              <ul
                v-if="item.details"
                class="text-sm text-slate-500 leading-relaxed mb-5 list-disc pl-4 space-y-1"
              >
                <li v-for="detail in item.details" :key="detail">
                  {{ detail }}
                </li>
              </ul>
              <div class="flex flex-wrap gap-2">
                <span
                  v-for="tag in item.tags"
                  :key="tag"
                  class="text-xs font-medium text-slate-500 bg-slate-100 px-2.5 py-1 rounded-md"
                  >{{ tag }}</span
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section class="py-24 px-6">
      <div class="max-w-6xl mx-auto">
        <div class="max-w-xl mb-16">
          <h2
            class="text-3xl sm:text-4xl font-bold text-slate-900 tracking-tight mb-4"
          >
            Strategi Keberlanjutan
          </h2>
          <p class="text-slate-500 leading-relaxed">
            Pilar-pilar penting agar budidaya Maggot BSF terus berjalan mandiri
            pasca-KKN.
          </p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div
            v-for="(strat, idx) in strategiList"
            :key="idx"
            class="bg-white rounded-2xl p-8 border border-slate-100 hover:border-teal-100 hover:shadow-xl hover:shadow-slate-200/50 hover:-translate-y-1 transition-all duration-300"
          >
            <div
              class="w-12 h-12 bg-teal-50 rounded-xl flex items-center justify-center text-2xl mb-6 border border-teal-100"
            >
              {{ strat.icon }}
            </div>
            <h3 class="text-lg font-bold text-slate-900 mb-3">
              {{ strat.title }}
            </h3>
            <p class="text-sm text-slate-500 leading-relaxed">
              {{ strat.desc }}
            </p>
          </div>
        </div>
      </div>
    </section>
    <section class="pb-16 px-6">
      <div class="max-w-6xl mx-auto flex justify-center">
        <button
          @click="emit('navigate', 'home')"
          class="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-teal-600 transition-colors duration-200 group"
        >
          <svg
            class="w-4 h-4 transition-transform duration-200 group-hover:-translate-x-0.5"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M15 19l-7-7 7-7"
            />
          </svg>
          Kembali ke Beranda
        </button>
      </div>
    </section>
  </div>
</template>
