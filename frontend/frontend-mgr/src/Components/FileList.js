import axios from "axios";
import React, { Component } from "react";
import DragAndDrop from "./DragAndDrop";

class FileList extends Component {
  
  constructor(props){
    super(props);
    this.state = {
      genre: "",
    };

    this.handleUploadAudio = this.handleUploadAudio.bind(this);
  }

  handleUploadAudio(ev) {
    ev.preventDefault();
    const data = new FormData();
    data.append("file", this.uploadInput.files[0]);
    data.append("filename", "sample.wav");
    axios
      .post(`http://localhost:5000/upload`, data)
      .then((response) => {
        this.setState({ genre: `Genre: ${response.data}` });
      })
      .then(() => {
        console.log(this.state);
      });
  }

  render() {
    return (
      
      <div>
        <div
          style={{
            height: 225,
            width: 450,
            alignContent: "center",
            alignSelf: "center",
          }}
        >
          <h3>{this.state.genre}</h3> 
        </div>

        <form onSubmit={this.handleUploadAudio}>
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
