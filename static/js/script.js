// console.log(document.getElementsByClassName("custom-file-upload")[0]);
// document.getElementsByClassName("custom-file-upload")[0].addEventListener("drop", dropHandler);
// document
//   .getElementsByClassName("custom-file-upload")
//   .addEventListener("dragover", dragOverHandler);

function dropHandler(ev) {
  console.log("File(s) dropped");
  ev.preventDefault();

  if (ev.dataTransfer.items) {
    //access the file
    [...ev.dataTransfer.items].forEach((item, i) => {
      // If dropped items aren't files, reject them
      if (item.kind === "file") {
        const file = item.getAsFile();
        console.log(`… file[${i}].name = ${file.name}`);
        const formData = new FormData();
        formData.append("file", file); // "file" is the name expected by the backend

        fetch("http://192.168.1.113:5000/upload", {
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(result => {
            console.log("Success:", result);
        })
        .catch(error => {
            console.error("Error:", error);
        });
        }
        
    });
  } 
  else {
    [...ev.dataTransfer.files].forEach((file, i) => {
      console.log(`… file[${i}].name = ${file.name}`);
    });
  }
}

document.getElementById('file-upload').addEventListener('change', () => {
  console.log("eyvallah")
  console.log(document.getElementsByName('data')[0].value);
  const file = document.getElementById("file-upload").files[0];
  if (file) {
    const formData = new FormData();
    formData.append("file", files); 
    fetch("http://192.168.1.113:5000/upload", {
        method: "POST",
        body: formData
    })
    
    .then(response => response.text())
    .then(result => {
        console.log("Success:", result);
    })
    
    .catch(error => {
        console.error("Error:", error);
    });
    
    }
    
});
