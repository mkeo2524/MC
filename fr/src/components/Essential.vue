<template>
    <div class="page1">
    
        <h1>Choose your essential landmarks</h1>
    
        <GetMarkers />
    

    
    
        
    
    </div>
</template>

<script>
import GetMarkers from './GetMarkers.vue'

export default {
    name: 'Essential',
    components: {
        GetMarkers,
    },
    methods: {

    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/* The Modal (background) */

.page1 {
    margin-top: 200px;
    top: 50%;
    left: 50%;
    border: solid black 2px;
    overflow-wrap: break-word;
    padding-bottom: 20px;
}
</style>
