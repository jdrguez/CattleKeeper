import axios from 'axios'
import router from '@/router'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
})


api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)


api.interceptors.response.use(
  (response) => response, // 
  (error) => {
    if (error.response) {
      if (error.response.status === 402) {
        router.push('/plans')
      }
      if (error.respose.status == 404){
        router.push('NotFound')
      }
    }
    return Promise.reject(error)
  }
)



export default api
