<template>
    <div class="getfile">
        <title>Upload new File Test</title>
        <h1>Upload new File</h1>
            <input id=fileInput type=file name=file>
            <a href="#" v-on:click="submitForm">SUBMIT</a>
            
    </div>
</template>

<script>

import $ from 'jquery'

export default {
    name: 'GetFile',
    components: {},
    methods:{ 
        async submitForm(){
            var files = document.getElementById('fileInput').files
            if (files.length < 1) {
                alert("No file selected.")
                return
            }

            var file = files[0]
            if (file.name === '') {
                alert("Invalid file name.")
                return;
            }

            var requestContent = {
                ["fileName"] : file.name,
                ["fileContent"] : await file.text()
            }

            var json = JSON.stringify(requestContent)
            alert(json)
            $.post('http://127.0.0.1:5000/upload', json)

            $.ajax ({
                url: 'http://127.0.0.1:5000/upload',
                type: "POST",
                data: json,
                dataType: "json",
                contentType: "application/json; charset=utf-8",
                crossDomain: true
            });
        }
    }
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
</style>
