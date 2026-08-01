<script setup lang="ts">
import { ref } from 'vue'
import Navbar from './ui/Navbar.vue'
import Home from './pages/Home.vue'
import Faq from './pages/Faq.vue'
import RocketStove from './pages/RocketStove.vue'
import SosialisasiSampah from './pages/SosialisasiSampah.vue'
import MaggotBSF from './pages/MaggotBSF.vue'
import EcoBrick from './pages/EcoBrick.vue'
import GreenHouseToga from './pages/GreenHouseToga.vue'
import PlatformDigital from './pages/PlatformDigital.vue'
import Biopori from './pages/Biopori.vue'
import PetaGis from './pages/PetaGis.vue'
import Footer from './ui/Footer.vue'

const currentPage = ref('home')

const handleNavigate = (page: string) => {
  currentPage.value = page
  window.scrollTo(0, 0)
}
</script>

<template>
  <div class="min-h-screen bg-slate-50 text-slate-800 font-sans scroll-smooth">
    <Navbar @navigate="handleNavigate" />
    
    <Home v-if="currentPage === 'home'" @navigate="handleNavigate" />
    <Faq v-else-if="currentPage === 'faq'" />
    <RocketStove v-else-if="currentPage === 'rocket-stove'" @navigate="handleNavigate" />
    <SosialisasiSampah v-else-if="currentPage === 'sosialisasi-sampah'" @navigate="handleNavigate" />
    <MaggotBSF v-else-if="currentPage === 'maggot-bsf'" @navigate="handleNavigate" />
    <EcoBrick v-else-if="currentPage === 'ecobrick' || currentPage === 'proker-ecobrick'" @navigate="handleNavigate" />
    <GreenHouseToga v-else-if="currentPage === 'green-house-toga'" @navigate="handleNavigate" />
    <PlatformDigital v-else-if="currentPage === 'platform-digital'" @navigate="handleNavigate" />
    <Biopori v-else-if="currentPage === 'biopori' || currentPage === 'proker-biopori'" @navigate="handleNavigate" />
    <PetaGis v-else-if="currentPage === 'peta-gis'" @navigate="handleNavigate" />
    
    <Footer />
  </div>
</template>
