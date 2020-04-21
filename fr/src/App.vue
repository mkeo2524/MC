<template>
    <div id="app">
        <div id="startingPage">
            <h1>Hello how are you today</h1>
            <GetFile />
            <button style="margin-top: 20px;" type="button" id="button" @click="goToEssential()">Next</button>
        </div>
        <div id="essential">
            <Essential />
        </div>
        <button style="margin-top: 20px;" type="button" id="button" @click="goToNonEssential()">Next</button>
        <div id="nonEssential">
            <GetMarkers />
        </div>
    </div>
</template>

<script>
import GetFile from './components/GetFile.vue'
import Essential from './components/Essential.vue'
import GetMarkers from './components/GetMarkers.vue'
import $ from 'jquery'
export default {
    name: 'App',
    components: {
        GetFile,
        Essential,
        GetMarkers,
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
    height: 1000px;
    background: #E8E8E8;
}

#startingPage {
    height: 500px;
}
</style>
