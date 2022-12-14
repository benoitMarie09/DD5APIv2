function interactiveCall() {
  var content = document.getElementById("interactive").value;
  if (content == "") {
    content = "classes/barde";
  }
  fetch(`https://bouduben31.pythonanywhere.com/api/${content}/`)
    .then(async (data) => {
      if (data.ok) {
        data = await data.json();
        document.getElementById("output").textContent = JSON.stringify(
          data,
          undefined,
          2
        );
      }
    })
    .catch((e) => console.log("Connection error", e));
}
