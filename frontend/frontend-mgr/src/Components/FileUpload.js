import React, { Component } from "react";
import DragAndDrop from "./DragAndDrop";
class FileList extends Component {
  constructor(props) {
    super(props);

    this.state = {
      genre: "",
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append("file", this.uploadInput.files[0]);
    data.append("filename", "sample.wav");
    fetch("http://localhost:5000/upload", {
      method: "POST",
      body: data,
    })
      .then((body) => {
        this.setState({ genre: `http://localhost:5000/upload/${body}` });
      });
    };
  

  
  
  render() {
    return (
      <div>
        <div style={{ height: 225, width: 450, alignContent: "center", alignSelf: "center"}}>
        <h3>Genre: classical </h3> 
        </div>
        
        <form onSubmit={this.handleUploadImage}>
          <div>
            <input
              ref={(ref) => {
                this.uploadInput = ref;
              }}
              type="file"
            />
          </div>
          <button>Upload</button>
        </form>
      </div>
    );
  }
}
export default FileList;
