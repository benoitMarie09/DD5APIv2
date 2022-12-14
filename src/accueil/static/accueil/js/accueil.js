function interactiveCall() {
  var content = document.getElementById("interactive").value;
  if (content == "") {
    content = "classes/barde";
  }
  fetch(`http://127.0.0.1:8000/api/${content}/`)
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
