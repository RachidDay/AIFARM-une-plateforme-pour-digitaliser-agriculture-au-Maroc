var N = document.forms['myform']['nitrogen'];
var P = document.forms['myform']['phosphorous'];
var K = document.forms['myform']['potassium'];
var ph = document.forms['myform']['ph'];
var rainfall = document.forms['myform']['rainfall'];
var error = document.getElementById('error');
function validation() {
    if (N.value > 155 or N.value < 3 ) {
        error.innerHRML = "Please enter valid numbers";
        error.style.display = "block";
        return false;
    }
    return true;
}