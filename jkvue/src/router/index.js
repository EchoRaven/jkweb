import Vue from 'vue'
import Router from 'vue-router'
/*引入页面*/
import login from '@/views/login/login.vue'
import register from '@/views/register/register.vue'
import home from '@/views/home/home.vue'
import write from '@/views/write/write.vue'
import webs from '@/views/webs/webs.vue'
import user from '@/views/user/user.vue'

Vue.use(Router)
const VueRouterPush = Router.prototype.push
Router.prototype.push = function push(to) {
  return VueRouterPush.call(this, to).catch(err => err)
}
/*配置路由*/
export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: login
    },
    {
      path: '/home/:uid',
      name: 'home',
      component: home
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/write/:uid',
      name: 'write',
      component: write
    },
    {
      path: '/webs/:id/:uid',
      name: 'webs',
      component: webs
    },
    {
      path: '/user/:uid',
      name: 'user',
      component: user
    },
  ]
})