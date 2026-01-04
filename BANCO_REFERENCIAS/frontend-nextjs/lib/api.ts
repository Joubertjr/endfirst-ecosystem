import axios from "axios"

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1"

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
})

// Interceptor para adicionar token do Clerk
api.interceptors.request.use(async (config) => {
  // Em Next.js, o token será adicionado pelo middleware do Clerk
  return config
})

export default api

