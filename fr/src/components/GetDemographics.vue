
<template>
    <div class="getmarkers">
    
        <h1>Patient Demographics</h1>
        <form id="frm1" action="/action_page.php">
    
            Patient ID: <input type="text" name="patient"><br><br> 
            Mass: <input type="number" name="mass"><br><br> 
            Height: <input type="number" name="height"><br><br> 
            Age: <input type="number" name="age"><br><br> 
            <input type="radio" id="male" name="gender" value="male">

            <label for="male">Male</label>
    
            <input type="radio" id="female" name="gender" value="female">
    
            <label for="female">Female</label>
    
            <input type="radio" id="other" name="gender" value="other">
    
            <label for="other">Other</label>
    
           
    
        </form>
    
    </div>
</template>

<script>
// import $ from 'jquery'

export default {

    components: {},
    methods: {
        async submitDemographics() {
            document.getElementById("frm1").submit();
        }
    }

}
</script>

<style>

</style>
