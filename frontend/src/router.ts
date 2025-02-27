import { createWebHistory, createRouter } from 'vue-router'

import HomeView from './views/HomeView.vue'
import PetsView from './views/PetsView.vue'
import ComponentesLuis from './views/ComponentesLuis.vue'
import ComponentesSergio from './views/ComponentesSergio.vue'
import TemplateScreen1 from './views/TemplateScreen1.vue'
import TemplateScreen2 from './views/TemplateScreen2.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/pets', component: PetsView},
  { path: '/componentesLuis', component: ComponentesLuis},
  { path: '/componentesSergio', component: ComponentesSergio},
  { path: '/templateScreen1', component: TemplateScreen1},
  { path: '/templateScreen2', component: TemplateScreen2}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
