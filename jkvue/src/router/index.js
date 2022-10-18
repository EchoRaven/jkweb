import Vue from 'vue'
import Router from 'vue-router'
/*引入页面*/
import login from '@/views/login/login.vue'
import register from '@/views/register/register.vue'
import home from '@/views/home/home.vue'

Vue.use(Router)

/*配置路由*/
export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/register',
      name: 'register',
      component: register
    }
  ]
})