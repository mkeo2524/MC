<template>
    <div class="landmarks">
        <form action="http://127.0.0.1:5000/meta">
            <label for="RASI">right anterior superior iliac spine:</label>
            <input type="text" id="RASI" name="RASI"><br><br>
            <label for="LASI">left anterior superior iliac spine:</label>
            <input type="text" id="LASI" name="LASI"><br><br>
            <label for="RTHI">right thigh:</label>
            <input type="text" id="RTHI" name="RTHI"><br><br>
            <label for="LTHI">left thigh:</label>
            <input type="text" id="LTHI" name="LTHI"><br><br>
            <label for="RKNE">right knee:</label>
            <input type="text" id="RKNE" name="RKNE"><br><br>
            <label for="LKNE">left knee:</label>
            <input type="text" id="LKNE" name="LKNE"><br><br>
            <label for="RTIB">right tibia:</label>
            <input type="text" id="RTIB" name="RTIB"><br><br>
            <label for="LTIB">left tibia:</label>
            <input type="text" id="LTIB" name="LTIB"><br><br>
            <label for="RANK">right ankle:</label>
            <input type="text" id="RANK" name="RANK"><br><br>
            <label for="LANK">left ankle:</label>
            <input type="text" id="LANK" name="LANK"><br><br>
            <label for="RTOE">right toe:</label>
            <input type="text" id="RTOE" name="RTOE"><br><br>
            <label for="LTOE">left toe:</label>
            <input type="text" id="LTOE" name="LTOE"><br><br>
            <label for="RHEE">right heel:</label>
            <input type="text" id="RHEE" name="RHEE"><br><br>
            <label for="LHEE">left heel:</label>
            <input type="text" id="LHEE" name="LHEE"><br><br>
            <input type="submit" value="Submit">
        </form>
    </div>
</template>

<script>
export default {
    name: 'Landmarks',
    methods: {

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

#MarkerTable {
    display: block;
    margin-left: auto;
    margin-right: auto;
    width: 25%;
    padding-top: 40px;
}
</style>
