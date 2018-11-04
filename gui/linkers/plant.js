function detect_plants() {

  document.getElementById("detect").value = "Hang on..."
  var python = require("python-shell")
  var path = require("path")

    var options = {
    scriptPath : path.join(__dirname, '/../engine/'),
    pythonPath : '/Users/tobias/anaconda/python.exe'
  }

  var plant = new python("plants.py", options);

  plant.end(function(err, code, message) {
    document.getElementById("detect").value = "Detect plants";
    })

}


function add_plant(){
  var python = require("python-shell")
  var path = require("path")
  var name = document.getElementById("plant").value

    var options = {
    scriptPath : path.join(__dirname, '/../engine/'),
    pythonPath : '/Users/tobias/anaconda/python.exe',
    args : ["cam", name]
  }

  var plant = new python("add_plant.py", options);

  plant.end(function(err, code, message) {
    swal("plant added!", "We can now recognize your plant", "success")
    document.getElementsById("add").innerHTML = "Add a new plant";
  })
}
