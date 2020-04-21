
<template>
    <div class="getmarkers">
    
    
    
        <h1>Tracking Marker Set</h1>
    
    
    
        <button id='trackingDataLoad' @click="handleLoadDataClick()">Load Data</button>
    
        <br><br><br><br>

        <div id='container' style='margin-bottom: 500px;'>
    
            <div id="trackingMarker" class="split left" style="overflow:auto; height:400px; width:10%; padding-left:400px; float:left">
    
                <table id='TrackingTable' class="trackingClass" style="width:100%">
    
                </table>
    
            </div>
    
            <div id="Explanation" class="split right" style="width: 50%; float:right ">
    
                <h3>Lorem Ipsum</h3>
    
                <p>"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor<br> incididunt ut labore et dolore magna aliqua.
               
    
                </p>
    
            </div>
    
        </div>
    
        <div id='trackingMarker' style="position: relative;">
    
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
            const table = document.getElementById('TrackingTable');
            data.markers.forEach((e) => {
                const rowContent = `<tr><td>${e}</td></tr>`;
                const row = document.createElement('tr');
                row.innerHTML = rowContent;
                table.append(row);
            });
            $(document).ready(function() {
                $('#TrackingTable tr').click(function() {
                    if ($(this).hasClass('selected')) {
                        $(this).removeClass('selected')
                    } else {
                        $(this).addClass('selected');
                    }
                });
            });
        },

        async clickOnce() {
            $('#trackingDataLoad').one('submit', function() {
                $(this).find('input[type="submit"]').attr('disabled', 'disabled');
            });
        },

        async onMoveToExtraLandmarks() {
            var rows = $('#TrackingTable .selected');
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

TrackingTable.selected {
    background-color: blue;
    color: 	#87CEEB;
}

table#TrackingTable {
    border-collapse: separate;
    border-spacing: 4px;
}

#TrackingTable tr {
    background-color: #eee;
    border-top: 1px solid #fff;
}

#TrackingTable tr:hover {
    background-color: #ccc;
}

#TrackingTable th {
    background-color: #fff;
}

#TrackingTable th,
#TrackingTable td {
    padding: 3px 5px;
}

#TrackingTable td:hover {
    cursor: pointer;
}
</style>
