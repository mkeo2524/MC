<template>
    <div class="getfile">
        <title>Upload new File Test</title>
        <h1>Upload new File</h1>
        <form method=post action="http://127.0.0.1:5000/upload" enctype=multipart/form-data>
            <input type=file name=file>
            <input type=submit value=Upload>
        </form>
    </div>
</template>

<script>
export default {
    name: 'GetFile'
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
