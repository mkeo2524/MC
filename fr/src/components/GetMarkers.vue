<template>
    <div class="getmarkers">
    
        <h1>Marker Set Get API Test</h1>
    
        <button @click="handleClick()">Click me!</button>
        <br><br><br><br>
    
        <div>
            <div id="table" style="float:left; overflow:scroll">
                <table id='MarkerTable' border-collapse='collapse'>
                </table>
            </div>
            <div id="landmark" style="float:right; margin-right:25%">
                <Landmarks />
            </div>
        </div>
    </div>
</template>

<script>
import Landmarks from './Landmarks.vue'
export default {
    name: 'GetMarkers',
    components: {
        Landmarks
    },
    methods: {
        async handleClick() {
            const url = 'http://127.0.0.1:5000/get';
            const response = await fetch(url);
            const data = await response.json();
            const table = document.getElementById('MarkerTable');
            data.markers.forEach((e) => {
                const rowContent = `<tr ><td>${e}</td></tr>`;
                const row = document.createElement('tr');
                row.innerHTML = rowContent;
                table.append(row);
            });
        },
    },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
    margin: 40px 0 0;
}

ul {
    list-style-type: none;
    padding: 0;
}

li {
    display: inline-block;
    margin: 0 10px;
}

a {
    color: #42b983;
}

#table {
    display: block;
    margin-left: 35%;
    width: 5%;
    padding-top: 40px;
    height: 500px;
}
</style>
