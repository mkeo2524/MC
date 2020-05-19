
<template>
    <div class="getmarkers">
    
        <button id='dataLoad' @click="handleLoadDataClick()">Load Data</button>
        <br><br><br><br>
        <div class='class1'>
            <h1>Choose your essential Landmarks</h1>
            <div id='container' style='margin-bottom: 430px;'>
                <div id="essentialMarker" class="split left" style="overflow:auto; height:400px; width:40%; padding-left:30%; float:left">
                    <table id='MarkerTable' class="markerClass" style="width:100%">
                    </table>
                </div>
            </div>
            <div id='nonEssentialMarker' style="position: relative;">
                <button @click="onMoveToExtraLandmarks()">Upload</button>
            </div>
        </div>
    
        <div class='class2'>
            <h1>Choose your tracking markers</h1>
            <div id='container' style='margin-bottom: 430px;'>
                <div id="trackingMarker" class="split left" style="overflow:auto; height:400px; width:40%; padding-left:30%; float:left">
                    <table id='trackingTable' class="markerClass" style="width:100%">
                    </table>
                </div>
            </div>
            <div id='nonEssentialMarker' style="position: relative;">
                <button @click="submitTracking()">Upload</button>
            </div>
        </div>
        <div class='class3'>
            <h1>hi</h1>
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
        async submitTracking(){
            var arr = [];
            var selectedRows = $('#trackingTable .selected');
            var i;
            for (i = 0; i < selectedRows.length; i++) {
                arr[i] = selectedRows[i].innerText;
            }
            $.post('http://127.0.0.1:5000/tracking', $.param({ data: arr }), console.log(arr))
        },

        async onMoveToExtraLandmarks() {
            var arr = [];
            var selectedRows = $('#MarkerTable .selected');
            var i;
            for (i = 0; i < selectedRows.length; i++) {
                arr[i] = selectedRows[i].innerText;
            }
            $.post('http://127.0.0.1:5000/markers', $.param({ data: arr }), console.log(arr))
            var unselectedRows = []
            const markerTable = document.getElementById('MarkerTable');
            for (i = 0; i < document.getElementById('MarkerTable').rows.length; i++) {
                var row = markerTable.rows[i]
                if (arr.includes(row.innerText) == false) {
                    unselectedRows.push(row.innerText)
                }
            }
            $.post('http://127.0.0.1:5000/unselected', $.param({ data: unselectedRows }), console.log(unselectedRows))
            const table = document.getElementById('trackingTable');
            unselectedRows.forEach((e) => {
                const rowContent = `<tr><td>${e}</td></tr>`;
                const row = document.createElement('tr');
                row.innerHTML = rowContent;
                table.append(row);
            });
            $(document).ready(function() {
                $('#trackingTable tr').click(function() {
                    if ($(this).hasClass('selected')) {
                        $(this).removeClass('selected')
                    } else {
                        $(this).addClass('selected');
                    }
                });
            });
        },

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

table#trackingTable {
    border-collapse: separate;
    border-spacing: 4px;
}

#trackingTable tr {
    background-color: #eee;
    border-top: 1px solid #fff;
}

#trackingTable tr:hover {
    background-color: #ccc;
}

#trackingTable th {
    background-color: #fff;
}

#trackingTable th,
#trackingTable td {
    padding: 3px 5px;
}

#trackingTable td:hover {
    cursor: pointer;
}

.class1,
.class2,
.class3 {
    width: 33.33%;
    float: left;
    height: 100px;
}
</style>
