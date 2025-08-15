import { defineStore } from 'pinia'
import { login, logout, getUserInfo } from '@/api/auth'
import { ElMessage } from 'element-plus'
import router from '@/router'

export const useUserStore = defineStore('user', {
  state: () => ({
    token: localStorage.getItem('token') || '',
    user: null,
    permissions: []
  }),

  getters: {
    isLoggedIn: (state) => !!state.token,
    userRole: (state) => state.user?.role || '',
    isSuperAdmin: (state) => state.user?.role === 'super_admin',
    isSiteAdmin: (state) => state.user?.role === 'site_admin',
    isOrgAdmin: (state) => state.user?.role === 'org_admin'
  },

  actions: {
    async login(credentials) {
      try {
        const response = await login(credentials)
        this.token = response.data.access_token
        localStorage.setItem('token', this.token)
        await this.fetchUserInfo()
        ElMessage.success('登录成功')
        router.push('/')
        return true
      } catch (error) {
        ElMessage.error(error.response?.data?.detail || '登录失败')
        return false
      }
    },

    async fetchUserInfo() {
      try {
        const response = await getUserInfo()
        this.user = response.data
        return this.user
      } catch (error) {
        this.logout()
        return null
      }
    },

    logout() {
      this.token = ''
      this.user = null
      this.permissions = []
      localStorage.removeItem('token')
      router.push('/login')
      ElMessage.success('已退出登录')
    },

    setPermissions(permissions) {
      this.permissions = permissions
    },

    hasPermission(permission) {
      if (this.isSuperAdmin) return true
      return this.permissions.includes(permission)
    }
  }
})