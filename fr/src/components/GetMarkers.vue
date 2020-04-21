
<template>
    <div class="getmarkers">
    
        <h1>Marker Set Get API Test</h1>
    
        <button id='dataLoad' @click="handleLoadDataClick()">Load Data</button>
        <br><br><br><br>
        <div id='container' style='margin-bottom: 500px;'>
            <div id="essentialMarker" class="split left" style="overflow:auto; height:400px; width:10%; padding-left:400px; float:left">
                <table id='MarkerTable' class="markerClass" style="width:100%">
                </table>
            </div>
            <div id="diagram" class="split right" style="width: 50%; float:right ">
                <img src="..\assets\landmarks.jpg" alt="failed" style="height: 400px;">
            </div>
        </div>
        <div id='nonEssentialMarker' style="position: relative;">
            <button @click="onMoveToExtraLandmarks()">Upload</button>
        </div>
    </div>
</template>

<script>
import $ from 'jquery'

export default {
    name: 'GetMarkers',
    components: {},
    methods: {
        async handleLoadDataClick() {
            const url = 'http://127.0.0.1:5000/get';
            const response = await fetch(url);
            const data = await response.json();
            const table = document.getElementById('MarkerTable');
            data.markers.forEach((e) => {
                const rowContent = `<tr><td>${e}</td></tr>`;
                const row = document.createElement('tr');
                row.innerHTML = rowContent;
                table.append(row);
            });
            $(document).ready(function() {
                $('#MarkerTable tr').click(function() {
                    if ($(this).hasClass('selected')) {
                        $(this).removeClass('selected')
                    } else {
                        $(this).addClass('selected');
                    }
                });
            });
        },

        async clickOnce() {
            $('#dataLoad').one('submit', function() {
                $(this).find('input[type="submit"]').attr('disabled', 'disabled');
            });
        },

        async onMoveToExtraLandmarks() {
            var rows = $('#MarkerTable .selected');
            console.log(rows);
            const markers = rows.toArray()
                .flatMap(row => row.cells.toArray())
                .map(cell => cell.innerHTML);
            console.log(markers);
        }

    }
}
</script>

<style>
.split-left {
    margin: 0 auto;
}

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

.selected {
    background-color: blue;
    color: #FF0000;
}

table#MarkerTable {
    border-collapse: separate;
    border-spacing: 4px;
}

#MarkerTable tr {
    background-color: #eee;
    border-top: 1px solid #fff;
}

#MarkerTable tr:hover {
    background-color: #ccc;
}

#MarkerTable th {
    background-color: #fff;
}

#MarkerTable th,
#MarkerTable td {
    padding: 3px 5px;
}

#MarkerTable td:hover {
    cursor: pointer;
}
</style>
