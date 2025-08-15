import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

NProgress.configure({ showSpinner: false })

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: () => import('@/views/Login.vue'),
    meta: { requiresAuth: false }
  },
  {
    path: '/',
    component: () => import('@/layouts/MainLayout.vue'),
    redirect: '/dashboard',
    meta: { requiresAuth: true },
    children: [
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: () => import('@/views/dashboard/index.vue'),
        meta: { title: '仪表板', icon: 'Monitor' }
      },
      {
        path: 'users',
        name: 'Users',
        component: () => import('@/views/users/index.vue'),
        meta: { title: '用户管理', icon: 'User', roles: ['super_admin', 'site_admin'] }
      },
      {
        path: 'organizations',
        name: 'Organizations',
        component: () => import('@/views/organizations/index.vue'),
        meta: { title: '机构管理', icon: 'OfficeBuilding', roles: ['super_admin', 'site_admin'] }
      },
      {
        path: 'sites',
        name: 'Sites',
        component: () => import('@/views/sites/index.vue'),
        meta: { title: '考点管理', icon: 'Location', roles: ['super_admin'] }
      },
      {
        path: 'exams',
        name: 'Exams',
        component: () => import('@/views/exams/index.vue'),
        meta: { title: '考试管理', icon: 'Document' }
      },
      {
        path: 'schedules',
        name: 'Schedules',
        component: () => import('@/views/schedules/index.vue'),
        meta: { title: '日程安排', icon: 'Calendar' }
      },
      {
        path: 'checkin',
        name: 'Checkin',
        component: () => import('@/views/checkin/index.vue'),
        meta: { title: '签到管理', icon: 'Checked' }
      },
      {
        path: 'reports',
        name: 'Reports',
        component: () => import('@/views/reports/index.vue'),
        meta: { title: '报表分析', icon: 'DataAnalysis' }
      }
    ]
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('@/views/404.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation guards
router.beforeEach(async (to, from, next) => {
  NProgress.start()
  
  const userStore = useUserStore()
  const token = localStorage.getItem('token')
  
  if (to.meta.requiresAuth && !token) {
    next('/login')
  } else if (to.path === '/login' && token) {
    next('/')
  } else {
    // Check role permissions
    if (to.meta.roles && !to.meta.roles.includes(userStore.user?.role)) {
      ElMessage.error('没有权限访问该页面')
      next(false)
    } else {
      next()
    }
  }
})

router.afterEach(() => {
  NProgress.done()
})

export default router