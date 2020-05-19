<template>
    <div id="app">
        <div id="startingPage">
            <h1>Map Client</h1>
            <p>"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad <br>minim veniam, quis nostrud exercitation ullamco laboris nisi 
            ut aliquip ex ea commodo consequat. Duis aute irure <br>dolor in reprehenderit in voluptate velit esse cillum dolore eu 
            fugiat nulla pariatur.<br> Excepteur sint occaecat cupidatat
             non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>
             <br>
             <GetDemographics /><br><br>
            <GetFile />
           
        </div>
        <div id="body">
                <div id="essential">
                    <Essential />
                </div>
        </div>
    </div>
</template>

<script>
import GetFile from './components/GetFile.vue'
import Essential from './components/Essential.vue'
import GetDemographics from './components/GetDemographics.vue'


import $ from 'jquery'
export default {
    name: 'App',
    components: {
        GetFile,
        Essential,
        GetDemographics,
    },
    methods: {
        async goToNonEssential() {
            $("button").click(function() {
                $('html,body').animate({
                        scrollTop: $("#nonEssential").offset().top
                    },
                    'slow');
            });
        },

        async goToEssential() {
            $("button").click(function() {
                $('html,body').animate({
                        scrollTop: $("#essential").offset().top
                    },
                    'slow');
            });
        },

        async goToTracking() {
            $("button").click(function() {
                $('html,body').animate({
                        scrollTop: $("#tracking").offset().top
                    },
                    'slow');
            });
        },
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

#nonEssential {
    width: 100%;
    height: 700px;
    background: #E8E8E8;
}

#startingPage {
    height: 500px;
}




</style>
