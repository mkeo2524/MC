<template>
    <div id="app">
        <div id="startingPage">
            <h1>Map Client</h1>
            <GetFile />
            <button style="margin-top: 20px;" type="button" id="button" @click="goToEssential()">Next</button>
        </div>
        <div id="essential">
            <Essential />
        </div>
        <button style="margin-top: 20px;" type="button" id="button" @click="goToNonEssential()">Next</button>
        <div id="nonEssential">
            <NonEssential />
        </div>
        <button style="margin-top: 20px;" type="button" id="button" @click="goToTracking()">Next</button>
        <div id="tracking">
            <Tracking />
        </div>
    </div>
</template>

<script>

import GetFile from './components/GetFile.vue'
import Essential from './components/Essential.vue'
import NonEssential from './components/NonEssential.vue'
import Tracking from './components/Tracking.vue'

import $ from 'jquery'
export default {
    name: 'App',
    components: {
        GetFile,
        Essential,
        NonEssential,
        Tracking,
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
