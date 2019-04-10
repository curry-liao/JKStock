// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import BootstrapVue from 'bootstrap-vue'
import VueResource from 'vue-resource'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueResource)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  data () {
    var self = this;
    var resource = this.$resource('/stock/');

    resource.get().then(
    (response) => {
      self.$data.items = response.body
    }, (response) => {
      console.info('fail')
    });

    return { items: [] }
  }
// Use components
//  components: { App },
//  template: '<App/>',
})
