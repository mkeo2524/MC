import Vue from 'vue'
import App from './App.vue'


Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  data:{
    data: {
      items: [
          {landmark: 'femur-GT-l'},
          {landmark: 'femur-GT-r'},
          {landmark: 'femur-HC-l'},
          {landmark: 'femur-HC-r'},
          {landmark: 'femur-LEC-l'},
          {landmark: 'femur-LEC-r'},
          {landmark: 'femur-MEC-l'},
          {landmark: 'femur-MEC-r'},
          {landmark: 'femur-kneecentre-l'},
          {landmark: 'femur-kneecentre-r'},
          {landmark: 'pelvis-LASIS'},
          {landmark: 'pelvis-LHJC'},
          {landmark: 'pelvis-LIS'},
          {landmark: 'pelvis-LIT'},
          {landmark: 'pelvis-LPS'},
          {landmark: 'pelvis-LPSIS'},
          {landmark: 'pelvis-RASIS'},
          {landmark: 'pelvis-RHJC'},
          {landmark: 'pelvis-RIS'},
          {landmark: 'pelvis-RIT'},
          {landmark: 'pelvis-RPS'},
          {landmark: 'pelvis-RPSIS'},
          {landmark: 'pelvis-Sacral'},
          {landmark: 'tibiafibula-LC-l'},
          {landmark: 'tibiafibula-LC-r'},
          {landmark: 'tibiafibula-LM-l'},
          {landmark: 'tibiafibula-LM-r'},
          {landmark: 'tibiafibula-MC-l'},
          {landmark: 'tibiafibula-MC-r'},
          {landmark: 'tibiafibula-MM-l'},
          {landmark: 'tibiafibula-MM-r'},
          {landmark: 'tibiafibula-TT-l'},
          {landmark: 'tibiafibula-TT-r'},
      ]
  },
  }
}).$mount('#app')
