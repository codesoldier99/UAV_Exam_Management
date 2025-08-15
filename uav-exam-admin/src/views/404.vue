<template>
  <div class="not-found">
    <div class="content">
      <h1>404</h1>
      <p>页面未找到</p>
      <el-button type="primary" @click="goHome">返回首页</el-button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goHome = () => {
  router.push('/')
}
</script>

<style lang="scss" scoped>
.not-found {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  
  .content {
    text-align: center;
    color: white;
    
    h1 {
      font-size: 120px;
      margin: 0;
    }
    
    p {
      font-size: 24px;
      margin: 20px 0 40px;
    }
  }
}
</style>