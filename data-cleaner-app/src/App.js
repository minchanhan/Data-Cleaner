import React from 'react';
import './App.css';
import Upload from './components/Upload';
import Download from './components/Download'
import Github from './components/github';

function App(){ // Create component

  return(
    <div className="App">
      <header className="App-header">
        <h1 className="Title">Data Cleaner</h1>
      </header>

      <h3 className="Desc">Upload your data sets and download a freshly cleaned one free of: Missing Values, Incorrect Data Types, etc.</h3>
      <Upload />
      <Download />
      <Github />
    </div>
    

  );
}

export default App; // Export file