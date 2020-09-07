
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
                <button @click="openfwForm()">Upload</button>
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
                <button @click="opentrForm()">Upload</button>
            </div>
        </div>
        <div class='class3'>
            <h1>...</h1>
        </div>
    
    
        <div class="form-popup" id="fwForm" style="overflow:auto">
            <form method=post action="http://127.0.0.1:5000/fieldworkoptions" class="form-container">
                <h2>Configure 2-Sided Lower Limb Registration</h2>
    
                <label for="pcstofit"><b>PCs to Fit:</b></label>
                <input type="number" value=1 name="pcstofit" required>
    
                <label for="mw"><b>Mahalanobis Weight</b></label>
                <input type="number" value=0.10 name="mw" step="0.001" required>
                <div style="overflow:auto; height:200px;">
                    <table id='fieldTable' class="fieldClass" style="width:100%">
                        <tr>
                            <th>Model Landmarks</th>
                            <th>Target Landmarks</th>
                        </tr>
                    </table>
                </div>
    
                <label for="markerRadius"><b>Marker Radius:</b></label>
                <input type="number" value=5.00 name="markerRadius" required>
                <label for="skinPadding"><b>Skin Padding:</b></label>
                <input type="number" value=5.00 name="skinPadding" required><br>
                <h4>Knee Options</h4>
    
                <input type="checkbox" id="kneeOptions1" name="kneeOptions1" value="DOF">
                <label for="kneeOptions1">Abd. DOF</label>
                <input type="checkbox" id="kneeOptions2" name="kneeOptions2" value="DOF">
                <label for="kneeOptions2">Abd. Correction</label><br><br>
    
    
                <div>
                    <button type="submit" id="submitButton" class="btn" style="margin-right:20px" @click="onMoveToExtraLandmarks()">Submit</button>
                    <button type="button" class="btn cancel" @click="closefwForm()">Close</button>
                </div>
            </form>
        </div>
    
        <div class="form2-popup" id="trForm" style="overflow:auto">
            <form method=post action="http://127.0.0.1:5000/opensimoptions" class="form2-container">
                <h2>Configure OpenSim Gait2392 Customisation</h2>
    
                <label for="inputUnit"><b>Input Unit:</b></label>
                <select name="inputUnit" id="inputUnit">
                                <option value="mm">mm</option>
                                <option value="cm">cm</option>
                                <option value="m">m</option>
                            </select><br>
    
                <label for="ouputUnit"><b>Ouput Unit:</b></label>
                <select name="ouputUnit" id="ouputUnit">
                                <option value="mm">mm</option>
                                <option value="cm">cm</option>
                                <option value="m">m</option>
                            </select><br>
    
                <input type="checkbox" id="scaleBody" name="scaleBody" value="DOF">
                <label for="scaleBody">Scale other bodies</label>
    
                <input type="checkbox" id="preserveMass" name="preserveMass" value="DOF">
                <label for="scaleBody">Preserve Mass Distribution:</label><br><br>
    
    
                <div style="overflow:auto; height:200px;">
                    <table id='trackTable' class="trackClass" style="width:100%">
                        <tr>
                            <th>Model Markers</th>
                            <th>Target Markers</th>
                        </tr>
                    </table>
                </div>
    
    
                <input type="checkbox" id="kneeSpline" name="kneeSpline" value="DOF">
                <label for="kneeSpline">Update Knee Spline:</label><br><br>
    
                <input type="checkbox" id="staticVastus" name="staticVastus" value="DOF">
                <label for="staticVastus">Static Vastus:</label><br><br>
    
                <input type="checkbox" id="isoForce" name="isoForce" value="DOF">
                <label for="isoForce">Update Max Isometric Forces:</label><br><br>
    
                <div>
                    <button type="submit" id="submitButton" class="btn" style="margin-right:20px" @click="submitTracking()">Submit</button>
                    <button type="button" class="btn cancel" @click="closetrForm()">Close</button>
                </div>
            </form>
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
            var resetBtn = document.getElementById("dataLoad")
            resetBtn.disabled = true;
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
        async submitTracking() {
            var trackMarkers = []
            for (i = 1; i < $('#trackTable tr').length; i++) {
                var stringi = i.toString()
                var landM = 'trackMarkers'
                var e = document.getElementById(landM.concat(stringi));
                trackMarkers[i] = e.options[e.selectedIndex].text;
            }
            $.post('http://127.0.0.1:5000/trackMarkers', $.param({ data: trackMarkers }), console.log(trackMarkers))
            var arr = [];
            var selectedRows = $('#trackingTable .selected');
            var i;
            for (i = 0; i < selectedRows.length; i++) {
                arr[i] = selectedRows[i].innerText;
            }
            $.post('http://127.0.0.1:5000/tracking', $.param({ data: arr }), console.log(arr))
            document.getElementById("trForm").style.display = "none";
        },

        async onMoveToExtraLandmarks() {
            document.getElementById("fwForm").style.display = "none";
            var fieldMarkers = []
            for (i = 1; i < $('#fieldTable tr').length; i++) {
                var stringi = i.toString()
                var landM = 'fieldLandmarks'
                var e = document.getElementById(landM.concat(stringi));
                fieldMarkers[i] = e.options[e.selectedIndex].text;
            }
            $.post('http://127.0.0.1:5000/fieldMarkers', $.param({ data: fieldMarkers }), console.log(fieldMarkers))
            
            
            
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
        openfwForm() {
            document.getElementById("fwForm").style.display = "block";
            var arr = [];
            var selectedRows = $('#MarkerTable .selected');
            var i;
            for (i = 0; i < selectedRows.length; i++) {
                arr[i] = selectedRows[i].innerText;
            }
            const fieldTable = document.getElementById('fieldTable');
            var tableRows = fieldTable.getElementsByTagName('tr');
            var rowCount = tableRows.length;

            for (var x = rowCount - 1; x > 0; x--) {
                fieldTable.removeChild(tableRows[x]);
            }
            var incre = 1;
            arr.forEach((e) => {
                const rowContent = `<tr><td>
                                            <select id="fieldLandmarks${incre}">
                                                <option value="$">--Please Select--</option>
                                                <option value="val1">femur-GT-l</option>
                                                <option value="val2">femur-GT-r</option>
                                                <option value="val3">femur-HC-l</option>
                                                <option value="val3">femur-HC-r</option>
                                                <option value="val3">femur-LEC-l</option>
                                                <option value="val3">femur-LEC-r</option>
                                                <option value="val3">femur-MEC-l</option>
                                                <option value="val3">femur-MEC-r</option>
                                                <option value="val3">femur-kneecentre-l</option>
                                                <option value="val3">femur-kneecentre-r</option>
                                                <option value="val3">pelvis-LASIS</option>
                                                <option value="val3">pelvis-LHJC</option>
                                                <option value="val3">pelvis-LIS</option>
                                                <option value="val3">pelvis-LIT</option>
                                                <option value="val3">pelvis-LPS</option>
                                                <option value="val3">pelvis-LPSIS</option>
                                                <option value="val3">pelvis-RASIS</option>
                                                <option value="val3">pelvis-RHJC</option>
                                                <option value="val3">pelvis-RIS</option>
                                                <option value="val3">pelvis-RIT</option>
                                                <option value="val3">pelvis-RPS</option>
                                                <option value="val3">pelvis-RPSIS</option>
                                                <option value="val3">tibiafibula-LC-l</option>
                                                <option value="val3">tibiafibula-LC-r</option>
                                                <option value="val3">tibiafibula-LM-l</option>
                                                <option value="val3">tibiafibula-LM-r</option>
                                                <option value="val3">tibiafibula-MC-l</option>
                                                <option value="val3">tibiafibula-MC-r</option>
                                                <option value="val3">tibiafibula-MM-l</option>
                                                <option value="val3">tibiafibula-MM-r</option>
                                                <option value="val3">tibiafibula-TT-l</option>
                                                <option value="val3">tibiafibula-TT-r</option>
                                            </select></td><td>${e}</td></tr>`;
                const row = document.createElement('tr');
                row.innerHTML = rowContent;
                fieldTable.append(row);
                incre++;

            });


        },


        closefwForm() {
            document.getElementById("fwForm").style.display = "none";
        },
        closetrForm() {
            document.getElementById("trForm").style.display = "none";
        },
        opentrForm() {
            document.getElementById("trForm").style.display = "block";
            var arr = [];
            var selectedRows = $('#MarkerTable .selected');
            var i;
            for (i = 0; i < selectedRows.length; i++) {
                arr[i] = selectedRows[i].innerText;
            }

            var unselectedRows = []
            const markerTable = document.getElementById('MarkerTable');

            for (i = 0; i < document.getElementById('MarkerTable').rows.length; i++) {
                var row = markerTable.rows[i]
                if (arr.includes(row.innerText) == false) {
                    unselectedRows.push(row.innerText)
                }
            }
            var array = [];
            var selectedRowss = $('#trackingTable .selected');
            for (i = 0; i < selectedRowss.length; i++) {
                array[i] = selectedRowss[i].innerText;
            }

            const trackTable = document.getElementById('trackTable');
            var tableRows = trackTable.getElementsByTagName('tr');
            var rowCount = tableRows.length;

            for (var x = rowCount - 1; x > 0; x--) {
                trackTable.removeChild(tableRows[x]);
            }
            var incre = 1;
            array.forEach((e) => {
                const rowContent = `<tr><td>
                                            <select id="trackMarkers${incre}">
                                                <option value="$">--Please Select--</option>
                                                <option value="val1">femur-GT-l</option>
                                                <option value="val2">femur-GT-r</option>
                                                <option value="val3">femur-HC-l</option>
                                                <option value="val3">femur-HC-r</option>
                                                <option value="val3">femur-LEC-l</option>
                                                <option value="val3">femur-LEC-r</option>
                                                <option value="val3">femur-MEC-l</option>
                                                <option value="val3">femur-MEC-r</option>
                                                <option value="val3">femur-kneecentre-l</option>
                                                <option value="val3">femur-kneecentre-r</option>
                                                <option value="val3">pelvis-LASIS</option>
                                                <option value="val3">pelvis-LHJC</option>
                                                <option value="val3">pelvis-LIS</option>
                                                <option value="val3">pelvis-LIT</option>
                                                <option value="val3">pelvis-LPS</option>
                                                <option value="val3">pelvis-LPSIS</option>
                                                <option value="val3">pelvis-RASIS</option>
                                                <option value="val3">pelvis-RHJC</option>
                                                <option value="val3">pelvis-RIS</option>
                                                <option value="val3">pelvis-RIT</option>
                                                <option value="val3">pelvis-RPS</option>
                                                <option value="val3">pelvis-RPSIS</option>
                                                <option value="val3">tibiafibula-LC-l</option>
                                                <option value="val3">tibiafibula-LC-r</option>
                                                <option value="val3">tibiafibula-LM-l</option>
                                                <option value="val3">tibiafibula-LM-r</option>
                                                <option value="val3">tibiafibula-MC-l</option>
                                                <option value="val3">tibiafibula-MC-r</option>
                                                <option value="val3">tibiafibula-MM-l</option>
                                                <option value="val3">tibiafibula-MM-r</option>
                                                <option value="val3">tibiafibula-TT-l</option>
                                                <option value="val3">tibiafibula-TT-r</option>
                                            </select></td><td>${e}</td></tr>`;
                const row = document.createElement('tr');
                row.innerHTML = rowContent;
                trackTable.append(row);
                incre++;

            });
        }
    },
}
</script>

<style>
/* The popup form - hidden by default */

.form-popup {
    display: none;
    width: 500px;
    height: 600px;
    position: fixed;
    top: calc(40% - 80px);
    left: calc(7% - 50px);
    border: 3px solid #f1f1f1;
    z-index: 9;
}

/* Add styles to the form container */

.form-container {
    max-width: 500px;
    padding: 10px;
    background-color: white;
}

.form-container input[type=number],
.form-container input[type=text] {
    width: 90%;
    padding: 10px;
    margin: 5px 0 22px 0;
    border: none;
    background: #f1f1f1;
}

.form2-popup {
    display: none;
    width: 500px;
    height: 600px;
    position: fixed;
    top: calc(40% - 80px);
    left: calc(40% - 50px);
    border: 3px solid #f1f1f1;
    z-index: 9;
}

/* Add styles to the form container */

.form2-container {
    max-width: 500px;
    padding: 10px;
    background-color: white;
}

.form2-container input[type=number],
.form2-container input[type=text] {
    width: 90%;
    padding: 10px;
    margin: 5px 0 22px 0;
    border: none;
    background: #f1f1f1;
}

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
