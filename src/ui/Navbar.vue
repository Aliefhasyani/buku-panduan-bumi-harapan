<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const emit = defineEmits(['navigate'])

const isMenuOpen = ref(false)
const isDropdownOpen = ref(false)
const isScrolled = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
  if (isMenuOpen.value) isDropdownOpen.value = false
}

const toggleDropdown = () => {
  isDropdownOpen.value = !isDropdownOpen.value
}

const closeAll = () => {
  isMenuOpen.value = false
  isDropdownOpen.value = false
}

const goTo = (page: string) => {
  emit('navigate', page)
  closeAll()
}

// Close dropdown when clicking outside
const handleClickOutside = (e: MouseEvent) => {
  const target = e.target as HTMLElement
  if (!target.closest('[data-dropdown]')) {
    isDropdownOpen.value = false
  }
}

const handleScroll = () => {
  isScrolled.value = window.scrollY > 8
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
  window.addEventListener('scroll', handleScroll, { passive: true })
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
  window.removeEventListener('scroll', handleScroll)
})

const listProker = [
  { nama: '1. Rocket Stove', slug: 'rocket-stove' },
  { nama: '2. Sosialisasi dan Workshop Pengelolaan Sampah', slug: 'sosialisasi-sampah' },
  { nama: '3. Budidaya Maggot BSF', slug: 'maggot-bsf' },
  { nama: '4. Sosialisasi dan Workshop Eco-Brick', slug: 'ecobrick' },
  { nama: '5. Green House', slug: 'green-house-toga' },
  { nama: '6. Platform Digital', slug: 'platform-digital' },
  { nama: '7. Green Garden', slug: 'biopori' },
  { nama: '8. Peta Spasial (GIS)', slug: 'peta-gis' },
]
</script>

<template>
  <nav
    class="w-full sticky top-0 z-50 transition-all duration-300"
    :class="isScrolled
      ? 'bg-white/90 backdrop-blur-xl shadow-sm border-b border-gray-100'
      : 'bg-white border-b border-gray-50'"
  >
    <div class="max-w-5xl mx-auto px-5 sm:px-6">
      <div class="flex items-center justify-between h-16">

        <!-- Logo -->
        <div
          class="flex items-center gap-3 cursor-pointer group"
          @click="goTo('home')"
        >
          <img
            src="@/assets/images/logo-kkn.png"
            alt="Logo KKN"
            class="h-9 w-auto object-contain"
          >
          <div class="hidden sm:block">
            <span class="font-semibold text-sm text-gray-900 block leading-tight group-hover:text-green-600 transition-colors duration-200">
              Buku Panduan Proker
            </span>
            <span class="text-[11px] text-gray-400 block">Individu KKN</span>
          </div>
        </div>

        <!-- Desktop Menu -->
        <div class="hidden md:flex items-center gap-1">
          <button
            @click="goTo('home')"
            class="px-3.5 py-2 text-sm text-gray-500 hover:text-green-600 hover:bg-green-50/60 rounded-lg transition-all duration-200 font-medium"
          >
            Beranda
          </button>

          <a
            href="#tahapan"
            class="px-3.5 py-2 text-sm text-gray-500 hover:text-green-600 hover:bg-green-50/60 rounded-lg transition-all duration-200 font-medium"
          >
            Tentang KKN
          </a>

          <!-- Dropdown Daftar Proker -->
          <div class="relative" data-dropdown>
            <button
              @click="toggleDropdown"
              class="flex items-center gap-1 px-3.5 py-2 text-sm text-gray-500 hover:text-green-600 hover:bg-green-50/60 rounded-lg transition-all duration-200 font-medium focus:outline-none"
            >
              <span>Daftar Proker</span>
              <svg
                class="w-3.5 h-3.5 transition-transform duration-200"
                :class="{ 'rotate-180': isDropdownOpen }"
                fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
              </svg>
            </button>

            <!-- Dropdown Panel -->
            <Transition
              enter-active-class="transition duration-150 ease-out"
              enter-from-class="opacity-0 -translate-y-1 scale-95"
              enter-to-class="opacity-100 translate-y-0 scale-100"
              leave-active-class="transition duration-100 ease-in"
              leave-from-class="opacity-100 translate-y-0 scale-100"
              leave-to-class="opacity-0 -translate-y-1 scale-95"
            >
              <div
                v-show="isDropdownOpen"
                class="absolute right-0 mt-2 w-60 bg-white rounded-xl shadow-lg ring-1 ring-gray-100 py-1.5 z-50 origin-top-right"
              >
                <button
                  v-for="proker in listProker"
                  :key="proker.slug"
                  @click="goTo(proker.slug)"
                  class="block w-full text-left px-4 py-2.5 text-sm text-gray-600 hover:bg-green-50/70 hover:text-green-700 transition-colors duration-150"
                >
                  {{ proker.nama }}
                </button>
              </div>
            </Transition>
          </div>

          <a
            href="#sistematika"
            class="px-3.5 py-2 text-sm text-gray-500 hover:text-green-600 hover:bg-green-50/60 rounded-lg transition-all duration-200 font-medium"
          >
            Laporan
          </a>

          <button
            @click="goTo('faq')"
            class="px-3.5 py-2 text-sm text-gray-500 hover:text-green-600 hover:bg-green-50/60 rounded-lg transition-all duration-200 font-medium"
          >
            FAQ
          </button>

          <div class="w-px h-5 bg-gray-200 mx-1.5"></div>

          <a
            href="/path-to-your-pdf.pdf"
            download
            class="ml-1 inline-flex items-center gap-1.5 bg-green-500 hover:bg-green-600 text-white text-sm font-medium px-4 py-2 rounded-lg transition-colors duration-200"
          >
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v12m0 0l-4-4m4 4l4-4M4 17v2a1 1 0 001 1h14a1 1 0 001-1v-2" />
            </svg>
            <span>PDF</span>
          </a>
        </div>

        <!-- Mobile Hamburger -->
        <button
          @click="toggleMenu"
          class="md:hidden w-9 h-9 flex items-center justify-center rounded-lg text-gray-400 hover:text-green-600 hover:bg-green-50/60 transition-all duration-200 focus:outline-none"
        >
          <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path
              v-if="!isMenuOpen"
              stroke-linecap="round" stroke-linejoin="round"
              d="M4 6h16M4 12h16M4 18h16"
            />
            <path
              v-else
              stroke-linecap="round" stroke-linejoin="round"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>

      </div>
    </div>

    <!-- Mobile Menu -->
    <Transition
      enter-active-class="transition duration-200 ease-out"
      enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition duration-150 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-2"
    >
      <div
        v-show="isMenuOpen"
        class="md:hidden border-t border-gray-100 bg-white/95 backdrop-blur-xl"
      >
        <div class="px-4 py-3 space-y-0.5">
          <button
            @click="goTo('home')"
            class="block w-full text-left text-gray-600 hover:text-green-600 hover:bg-green-50/60 px-3 py-2.5 rounded-lg text-sm font-medium transition-all duration-200"
          >
            Beranda
          </button>

          <!-- Mobile Proker List -->
          <div class="border-t border-gray-50 my-1.5"></div>
          <p class="px-3 pt-1 pb-0.5 text-[11px] font-semibold text-gray-300 uppercase tracking-wider">Program Kerja</p>
          <button
            v-for="proker in listProker"
            :key="'m-' + proker.slug"
            @click="goTo(proker.slug)"
            class="block w-full text-left text-gray-500 hover:text-green-600 hover:bg-green-50/60 px-3 py-2 rounded-lg text-sm transition-all duration-200"
          >
            {{ proker.nama }}
          </button>

          <div class="border-t border-gray-50 my-1.5"></div>

          <button
            @click="goTo('faq')"
            class="block w-full text-left text-gray-600 hover:text-green-600 hover:bg-green-50/60 px-3 py-2.5 rounded-lg text-sm font-medium transition-all duration-200"
          >
            FAQ
          </button>

          <div class="pt-2 pb-1">
            <a
              href="/path-to-your-pdf.pdf"
              download
              class="flex items-center justify-center gap-2 bg-green-500 hover:bg-green-600 text-white text-sm font-medium px-4 py-2.5 rounded-lg transition-colors duration-200"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v12m0 0l-4-4m4 4l4-4M4 17v2a1 1 0 001 1h14a1 1 0 001-1v-2" />
              </svg>
              Download PDF
            </a>
          </div>
        </div>
      </div>
    </Transition>
  </nav>
</template>