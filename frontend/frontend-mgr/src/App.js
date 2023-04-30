import "./App.css";
import FileList from "./Components/FileList";
import FileUpload from "./Components/FileUpload";
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1> Genre Guesser </h1>
        <FileList />
      </header>
    </div>
  );
}

export default App;
