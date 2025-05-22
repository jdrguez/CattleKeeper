import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    theme: localStorage.getItem('theme') || 'auto', 
  }),
  actions: {
    setTheme(value:any) {
      this.theme = value
      localStorage.setItem('theme', value)
      this.applyTheme()
    },
    applyTheme() {
      const html = document.documentElement
      const body = document.body
      const theme = this.theme
    
      html.removeAttribute('data-bs-theme')
      body.classList.remove('theme-light', 'theme-dark', 'theme-auto')
    
      if (theme === 'auto') {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
        html.setAttribute('data-bs-theme', prefersDark ? 'dark' : 'light')
        body.classList.add('theme-auto')
        body.classList.add(prefersDark ? 'theme-dark' : 'theme-light')
      } else {
        html.setAttribute('data-bs-theme', theme)
        body.classList.add(`theme-${theme}`)
      }
    }
    
  },
})
