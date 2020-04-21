
<template>
    <div class="getmarkers">
    
    
    
        <h1>Non-Essential Markers</h1>
    
    
    
        <button id='nonEssentialDataLoad' @click="handleLoadDataClick()">Load Data</button>
    
        <br><br><br><br>

        <div id='container' style='margin-bottom: 500px;'>
    
            <div id="nonEssentialMarker" class="split left" style="overflow:auto; height:400px; width:10%; padding-left:400px; float:left">
    
                <table id='nonEssentialTable' class="tableClass" style="width:100%">
    
                </table>
    
            </div>
    
            <div id="Explanation" class="split right" style="width: 50%; float:right ">
    
                <h3>Lorem Ipsum</h3>
    
                <p>"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor<br> incididunt ut labore et dolore magna aliqua.
                 Ut enim ad minim veniam, quis nostrud exercitation ullamco<br> laboris nisi ut aliquip ex ea commodo consequat. Duis aute
    
 irure dolor in reprehenderit in voluptate<br> velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat<br> cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    
                </p>
    
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
            const table = document.getElementById('nonEssentialTable');
            data.markers.forEach((e) => {
                const rowContent = `<tr><td>${e}</td></tr>`;
                const row = document.createElement('tr');
                row.innerHTML = rowContent;
                table.append(row);
            });
            $(document).ready(function() {
                $('#nonEssentialTable tr').click(function() {
                    if ($(this).hasClass('selected')) {
                        $(this).removeClass('selected')
                    } else {
                        $(this).addClass('selected');
                    }
                });
            });
        },

        async clickOnce() {
            $('#nonEssentialDataLoad').one('submit', function() {
                $(this).find('input[type="submit"]').attr('disabled', 'disabled');
            });
        },

        async onMoveToExtraLandmarks() {
            var rows = $('#nonEssentialTable .selected');
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

nonEssentialTable.selected {
    background-color: blue;
    color: 	#87CEEB;
}

table#nonEssentialTable {
    border-collapse: separate;
    border-spacing: 4px;
}

#nonEssentialTable tr {
    background-color: #eee;
    border-top: 1px solid #fff;
}

#nonEssentialTable tr:hover {
    background-color: #ccc;
}

#nonEssentialTable th {
    background-color: #fff;
}

#nonEssentialTable th,
#nonEssentialTable td {
    padding: 3px 5px;
}

#nonEssentialTable td:hover {
    cursor: pointer;
}
</style>
