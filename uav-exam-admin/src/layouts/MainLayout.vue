<template>
  <el-container class="main-layout">
    <el-aside :width="isCollapse ? '64px' : '220px'">
      <div class="logo-container">
        <img src="/logo.png" alt="Logo" class="logo" />
        <span v-if="!isCollapse" class="logo-title">UAV考点管理</span>
      </div>
      
      <el-menu
        :default-active="activeMenu"
        :collapse="isCollapse"
        background-color="#304156"
        text-color="#bfcbd9"
        active-text-color="#409eff"
        :router="true"
      >
        <template v-for="route in menuRoutes" :key="route.path">
          <el-menu-item
            v-if="!route.children"
            :index="route.path"
          >
            <el-icon><component :is="route.meta.icon" /></el-icon>
            <template #title>{{ route.meta.title }}</template>
          </el-menu-item>
          
          <el-sub-menu
            v-else
            :index="route.path"
          >
            <template #title>
              <el-icon><component :is="route.meta.icon" /></el-icon>
              <span>{{ route.meta.title }}</span>
            </template>
            <el-menu-item
              v-for="child in route.children"
              :key="child.path"
              :index="`${route.path}/${child.path}`"
            >
              {{ child.meta.title }}
            </el-menu-item>
          </el-sub-menu>
        </template>
      </el-menu>
    </el-aside>
    
    <el-container>
      <el-header>
        <div class="header-left">
          <el-icon
            class="collapse-btn"
            @click="isCollapse = !isCollapse"
          >
            <component :is="isCollapse ? 'Expand' : 'Fold'" />
          </el-icon>
          
          <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item v-for="item in breadcrumbs" :key="item.path">
              {{ item.meta.title }}
            </el-breadcrumb-item>
          </el-breadcrumb>
        </div>
        
        <div class="header-right">
          <el-dropdown>
            <div class="user-info">
              <el-avatar :size="32" :src="userStore.user?.avatar_url">
                {{ userStore.user?.full_name?.[0] || 'U' }}
              </el-avatar>
              <span class="user-name">{{ userStore.user?.full_name || '用户' }}</span>
              <el-icon><ArrowDown /></el-icon>
            </div>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="showProfile">
                  <el-icon><User /></el-icon>
                  个人中心
                </el-dropdown-item>
                <el-dropdown-item @click="showSettings">
                  <el-icon><Setting /></el-icon>
                  系统设置
                </el-dropdown-item>
                <el-dropdown-item divided @click="handleLogout">
                  <el-icon><SwitchButton /></el-icon>
                  退出登录
                </el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </el-header>
      
      <el-main>
        <router-view v-slot="{ Component }">
          <transition name="fade" mode="out-in">
            <component :is="Component" />
          </transition>
        </router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { ElMessageBox } from 'element-plus'

const route = useRoute()
const router = useRouter()
const userStore = useUserStore()

const isCollapse = ref(false)

const activeMenu = computed(() => route.path)

const menuRoutes = computed(() => {
  const routes = router.options.routes.find(r => r.path === '/')?.children || []
  return routes.filter(r => {
    if (r.meta?.hidden) return false
    if (r.meta?.roles) {
      return r.meta.roles.includes(userStore.userRole) || userStore.isSuperAdmin
    }
    return true
  })
})

const breadcrumbs = computed(() => {
  const matched = route.matched.filter(r => r.meta?.title)
  return matched.slice(1) // Remove the first item (MainLayout)
})

const showProfile = () => {
  router.push('/profile')
}

const showSettings = () => {
  router.push('/settings')
}

const handleLogout = async () => {
  try {
    await ElMessageBox.confirm(
      '确定要退出登录吗？',
      '提示',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }
    )
    userStore.logout()
  } catch {
    // User cancelled
  }
}
</script>

<style lang="scss" scoped>
.main-layout {
  height: 100vh;
  
  .el-aside {
    background-color: #304156;
    transition: width 0.3s;
    
    .logo-container {
      height: 60px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #2b3548;
      
      .logo {
        width: 32px;
        height: 32px;
      }
      
      .logo-title {
        margin-left: 12px;
        color: #fff;
        font-size: 16px;
        font-weight: 600;
      }
    }
    
    .el-menu {
      border-right: none;
      height: calc(100% - 60px);
      overflow-y: auto;
    }
  }
  
  .el-header {
    background-color: #fff;
    box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    
    .header-left {
      display: flex;
      align-items: center;
      
      .collapse-btn {
        font-size: 20px;
        cursor: pointer;
        margin-right: 20px;
        
        &:hover {
          color: #409eff;
        }
      }
    }
    
    .header-right {
      .user-info {
        display: flex;
        align-items: center;
        cursor: pointer;
        
        .user-name {
          margin: 0 8px;
          color: #606266;
        }
      }
    }
  }
  
  .el-main {
    background-color: #f5f7fa;
    padding: 20px;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>