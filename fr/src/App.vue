<template>
    <div id="app">
        <h1>Hello how are you today</h1>
        <GetFile />
        <GetMarkers />
    </div>
</template>

<script>
import GetFile from './components/GetFile.vue'
import GetMarkers from './components/GetMarkers.vue'

export default {
    name: 'App',
    components: {
        GetFile,
        GetMarkers
    }
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
