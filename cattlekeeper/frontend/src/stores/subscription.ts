import { defineStore } from 'pinia'
import api from '@/api/axios'

export const useSubscriptionStore = defineStore('subscription', {
  state: () => ({
    isActive: false,
    loading: false,
  }),
  actions: {
    async checkSubscription() {
      this.loading = true
      try {
        const res = await api.get('/api/subscription/status')
        this.isActive = res.data.active
      } catch (error) {
        console.error('Error al comprobar suscripción:', error)
        this.isActive = false
      } finally {
        this.loading = false
      }
    },
    setSubscriptionStatus(status:any) {
      this.isActive = status
    }
  }
})
