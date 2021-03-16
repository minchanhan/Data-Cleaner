import React from 'react';

function Download(){
    return(
        <a className="Download" href="cleaneddata.csv" download>
            <button>Download</button>
        </a>


    );
}

export default Download;