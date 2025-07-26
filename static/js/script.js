let link = document.getElementById("link").value;
document.getElementsByClassName("custom-file-upload")[0].addEventListener("drop", dropHandler);
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

        fetch(`${link}/upload`, {
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

document.getElementById("file-upload").addEventListener('change', () => {
  console.log(document.getElementById("file-upload").files[0])
  const file = document.getElementById("file-upload").files[0];
  if (file) {
    const formData = new FormData();
    formData.append("file", file); 
    fetch(`${link}/upload`, {
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
